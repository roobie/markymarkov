#!/usr/bin/env python3
"""
Semantic Pattern Extractor for Python Code
Detects high-level coding patterns (50+ semantic patterns) from AST.
"""

import ast
from typing import List, Dict, Optional, Set
from enum import Enum
from dataclasses import dataclass


class CodePattern(Enum):
    """High-level semantic patterns in Python code."""

    # Control flow patterns (5)
    IF_NONE_CHECK = "if-none-check"
    IF_NOT_NONE = "if-not-none"
    IF_EMPTY_CHECK = "if-empty-check"
    IF_TYPE_CHECK = "if-type-check"
    GUARD_CLAUSE = "guard-clause"
    EARLY_RETURN_SUCCESS = "early-return-success"
    EARLY_RETURN_FAILURE = "early-return-failure"

    # Loop patterns (6)
    LOOP_ACCUMULATE = "loop-accumulate"
    LOOP_TRANSFORM = "loop-transform"
    LOOP_FILTER = "loop-filter"
    LOOP_ENUMERATE = "loop-enumerate"
    LOOP_ZIP = "loop-zip"
    LOOP_DICT_ITEMS = "loop-dict-items"

    # Return patterns (5)
    RETURN_NONE = "return-none"
    RETURN_BOOL = "return-bool"
    RETURN_LIST = "return-list"
    RETURN_DICT = "return-dict"
    RETURN_COMPUTED = "return-computed"

    # Data structure patterns (8)
    INIT_EMPTY_LIST = "init-empty-list"
    INIT_EMPTY_DICT = "init-empty-dict"
    INIT_COUNTER = "init-counter"
    INIT_DEFAULT_VALUE = "init-default-value"
    APPEND_TO_LIST = "append-to-list"
    DICT_UPDATE = "dict-update"
    DICT_GET_DEFAULT = "dict-get-default"
    DEFAULT_DICT_PATTERN = "defaultdict-pattern"

    # Error handling patterns (5)
    TRY_EXCEPT_PASS = "try-except-pass"
    TRY_EXCEPT_LOG = "try-except-log"
    TRY_EXCEPT_RERAISE = "try-except-reraise"
    TRY_FINALLY = "try-finally"
    CONTEXT_MANAGER = "context-manager"

    # Function patterns (6)
    FUNCTION_VALIDATOR = "function-validator"
    FUNCTION_TRANSFORMER = "function-transformer"
    FUNCTION_FACTORY = "function-factory"
    INIT_METHOD = "init-method"
    PROPERTY_GETTER = "property-getter"
    PROPERTY_SETTER = "property-setter"

    # Class patterns (3)
    CLASS_METHOD = "class-method"
    STATIC_METHOD = "static-method"
    FUNCTION_DECORATOR = "function-decorator"

    # Comprehension patterns (3)
    LIST_COMPREHENSION = "list-comprehension"
    DICT_COMPREHENSION = "dict-comprehension"
    GENERATOR_EXPRESSION = "generator-expression"

    # API patterns (3)
    API_VALIDATION = "api-validation"
    API_ERROR_RESPONSE = "api-error-response"
    API_SUCCESS_RESPONSE = "api-success-response"

    # Other idioms (5)
    TERNARY_EXPRESSION = "ternary-expression"
    STRING_FORMAT = "string-format"
    LOGGING_CALL = "logging-call"
    UNPACKING = "unpacking"
    BOOLEAN_EXPRESSION = "boolean-expression"

    # Generic fallback
    UNKNOWN = "unknown"


@dataclass
class SemanticNode:
    """Represents a detected semantic pattern."""

    pattern: CodePattern
    context: Dict = None
    lineno: Optional[int] = None  # Line number in source file
    col_offset: Optional[int] = None  # Column offset in source file
    end_lineno: Optional[int] = None  # End line number
    end_col_offset: Optional[int] = None  # End column offset

    def __post_init__(self):
        if self.context is None:
            self.context = {}

    def __hash__(self):
        return hash(self.pattern)

    def __eq__(self, other):
        return isinstance(other, SemanticNode) and self.pattern == other.pattern

    def __repr__(self):
        return f"SemanticNode({self.pattern.value})"


class SemanticPatternAnalyzer(ast.NodeVisitor):
    """
    AST visitor that extracts semantic patterns from Python code.
    Detects 50+ high-level coding patterns.
    """

    def __init__(self):
        """Initialize the pattern analyzer."""
        self.patterns: List[SemanticNode] = []
        self.current_function: Optional[ast.FunctionDef] = None
        self.in_loop = False
        self.in_try = False

    def _add_pattern(self, pattern: CodePattern, node: ast.AST = None, context: Dict = None):
        """Add a pattern with location information."""
        if context is None:
            context = {}
        
        lineno = getattr(node, 'lineno', None) if node else None
        col_offset = getattr(node, 'col_offset', None) if node else None
        end_lineno = getattr(node, 'end_lineno', None) if node else None
        end_col_offset = getattr(node, 'end_col_offset', None) if node else None
        
        self.patterns.append(SemanticNode(
            pattern=pattern,
            context=context,
            lineno=lineno,
            col_offset=col_offset,
            end_lineno=end_lineno,
            end_col_offset=end_col_offset
        ))

    def visit_FunctionDef(self, node: ast.FunctionDef):
        """Analyze function definitions."""
        old_function = self.current_function
        self.current_function = node

        # Detect function type
        func_pattern = self._classify_function(node)
        if func_pattern:
            self._add_pattern(func_pattern, node, {"name": node.name})

        # Visit body
        self.generic_visit(node)

        self.current_function = old_function

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        """Treat async functions same as regular functions."""
        self.visit_FunctionDef(node)

    def visit_If(self, node: ast.If):
        """Detect conditional patterns."""
        pattern = self._classify_if_statement(node)
        if pattern:
            self._add_pattern(pattern, node)

        self.generic_visit(node)

    def visit_For(self, node: ast.For):
        """Detect loop patterns."""
        old_in_loop = self.in_loop
        self.in_loop = True

        pattern = self._classify_loop(node)
        if pattern:
            self._add_pattern(pattern, node)

        self.generic_visit(node)

        self.in_loop = old_in_loop

    def visit_While(self, node: ast.While):
        """Detect while loop patterns."""
        old_in_loop = self.in_loop
        self.in_loop = True

        # While loops are generally accumulation/filter patterns
        self.patterns.append(SemanticNode(CodePattern.LOOP_ACCUMULATE, {}))

        self.generic_visit(node)

        self.in_loop = old_in_loop

    def visit_Return(self, node: ast.Return):
        """Detect return patterns."""
        pattern = self._classify_return(node)
        if pattern:
            self._add_pattern(pattern, node)

        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign):
        """Detect assignment patterns."""
        pattern = self._classify_assignment(node)
        if pattern:
            self.patterns.append(SemanticNode(pattern, {}))

        self.generic_visit(node)

    def visit_AugAssign(self, node: ast.AugAssign):
        """Detect augmented assignment (+=, -=, etc)."""
        self.patterns.append(SemanticNode(CodePattern.LOOP_ACCUMULATE, {}))
        self.generic_visit(node)

    def visit_Try(self, node: ast.Try):
        """Detect error handling patterns."""
        old_in_try = self.in_try
        self.in_try = True

        pattern = self._classify_try_except(node)
        if pattern:
            self.patterns.append(SemanticNode(pattern, {}))

        self.generic_visit(node)

        self.in_try = old_in_try

    def visit_With(self, node: ast.With):
        """Detect context manager patterns."""
        self.patterns.append(SemanticNode(CodePattern.CONTEXT_MANAGER, {}))
        self.generic_visit(node)

    def visit_IfExp(self, node: ast.IfExp):
        """Detect ternary expressions."""
        self.patterns.append(SemanticNode(CodePattern.TERNARY_EXPRESSION, {}))
        self.generic_visit(node)

    def visit_ListComp(self, node: ast.ListComp):
        """Detect list comprehensions."""
        self.patterns.append(SemanticNode(CodePattern.LIST_COMPREHENSION, {}))
        self.generic_visit(node)

    def visit_DictComp(self, node: ast.DictComp):
        """Detect dict comprehensions."""
        self.patterns.append(SemanticNode(CodePattern.DICT_COMPREHENSION, {}))
        self.generic_visit(node)

    def visit_GeneratorExp(self, node: ast.GeneratorExp):
        """Detect generator expressions."""
        self.patterns.append(SemanticNode(CodePattern.GENERATOR_EXPRESSION, {}))
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call):
        """Detect function calls and their patterns."""
        # Detect logging calls
        if isinstance(node.func, ast.Attribute):
            # Check for logger.method() or logging.method()
            attr_lower = node.func.attr.lower()
            logging_methods = {"debug", "info", "warning", "warn", "error", "critical", "fatal", "log"}
            if "log" in attr_lower or attr_lower in logging_methods:
                self.patterns.append(SemanticNode(CodePattern.LOGGING_CALL, {}))

        # Detect string formatting
        if isinstance(node.func, ast.Attribute):
            if node.func.attr in ["format", "join"]:
                self.patterns.append(SemanticNode(CodePattern.STRING_FORMAT, {}))

        self.generic_visit(node)

    # Classification methods

    def _classify_function(self, node: ast.FunctionDef) -> Optional[CodePattern]:
        """Determine function type from structure."""
        # Check decorators
        for decorator in node.decorator_list:
            if isinstance(decorator, ast.Name):
                if decorator.id == "property":
                    return CodePattern.PROPERTY_GETTER
                elif decorator.id == "classmethod":
                    return CodePattern.CLASS_METHOD
                elif decorator.id == "staticmethod":
                    return CodePattern.STATIC_METHOD

        # Check name patterns
        if node.name == "__init__":
            return CodePattern.INIT_METHOD

        if node.name.startswith("__") and node.name.endswith("__"):
            # Other dunder methods - don't classify
            return None

        # Analyze body structure
        if not node.body:
            return None

        # Check if it's a validator (early returns with checks)
        early_returns = sum(
            1
            for stmt in node.body
            if isinstance(stmt, ast.If)
            and any(isinstance(s, ast.Return) for s in stmt.body)
        )
        if early_returns >= 2:
            return CodePattern.FUNCTION_VALIDATOR

        # Check if it's a transformer (takes input, returns transformed)
        has_param = len(node.args.args) > 0
        has_return = any(isinstance(stmt, ast.Return) for stmt in ast.walk(node))
        if has_param and has_return:
            return CodePattern.FUNCTION_TRANSFORMER

        return None

    def _classify_if_statement(self, node: ast.If) -> Optional[CodePattern]:
        """Classify the semantic meaning of an if statement."""
        test = node.test

        # Check for None checks
        if isinstance(test, ast.Compare):
            if any(isinstance(op, (ast.Is, ast.IsNot)) for op in test.ops):
                # Check if comparing to None
                if any(
                    isinstance(comp, ast.Constant) and comp.value is None
                    for comp in test.comparators
                ):
                    # is None or is not None?
                    if any(isinstance(op, ast.IsNot) for op in test.ops):
                        return CodePattern.IF_NOT_NONE
                    else:
                        return CodePattern.IF_NONE_CHECK

        # Check for empty checks (if not x, if len(x) == 0, etc.)
        if isinstance(test, ast.UnaryOp) and isinstance(test.op, ast.Not):
            return CodePattern.IF_EMPTY_CHECK

        if isinstance(test, ast.Compare):
            # Check for len(x) == 0
            if isinstance(test.left, ast.Call):
                if isinstance(test.left.func, ast.Name):
                    if test.left.func.id == "len":
                        return CodePattern.IF_EMPTY_CHECK

        # Check for type checks
        if isinstance(test, ast.Call):
            if isinstance(test.func, ast.Name) and test.func.id == "isinstance":
                return CodePattern.IF_TYPE_CHECK

        # Check for guard clause (early return)
        if any(isinstance(stmt, ast.Return) for stmt in node.body):
            if any(isinstance(stmt, ast.Return) for stmt in node.orelse):
                # if-else with returns in both branches
                return CodePattern.EARLY_RETURN_SUCCESS
            return CodePattern.GUARD_CLAUSE

        return None

    def _classify_loop(self, node: ast.For) -> Optional[CodePattern]:
        """Classify loop patterns."""
        # Check what we're iterating over
        iter_node = node.iter

        # enumerate pattern
        if isinstance(iter_node, ast.Call):
            if isinstance(iter_node.func, ast.Name):
                if iter_node.func.id == "enumerate":
                    return CodePattern.LOOP_ENUMERATE
                elif iter_node.func.id == "zip":
                    return CodePattern.LOOP_ZIP

        # dict.items() pattern
        if isinstance(iter_node, ast.Call):
            if isinstance(iter_node.func, ast.Attribute):
                if iter_node.func.attr == "items":
                    return CodePattern.LOOP_DICT_ITEMS

        # Analyze body to determine purpose
        has_append = False
        has_accumulate = False
        has_conditional = False

        for stmt in ast.walk(node):
            if isinstance(stmt, ast.Call):
                if isinstance(stmt.func, ast.Attribute):
                    if stmt.func.attr == "append":
                        has_append = True

            if isinstance(stmt, ast.AugAssign):
                has_accumulate = True

            if isinstance(stmt, ast.If):
                has_conditional = True

        # Classify based on body
        if has_append and has_conditional:
            return CodePattern.LOOP_FILTER
        elif has_append:
            return CodePattern.LOOP_TRANSFORM
        elif has_accumulate:
            return CodePattern.LOOP_ACCUMULATE

        return None

    def _classify_return(self, node: ast.Return) -> Optional[CodePattern]:
        """Classify return statement patterns."""
        if node.value is None:
            return CodePattern.RETURN_NONE

        value = node.value

        # Check for None constant
        if isinstance(value, ast.Constant) and value.value is None:
            return CodePattern.RETURN_NONE

        # Check literal types
        if isinstance(value, ast.Constant):
            if isinstance(value.value, bool):
                return CodePattern.RETURN_BOOL

        # Check data structure returns
        if isinstance(value, ast.List):
            return CodePattern.RETURN_LIST
        elif isinstance(value, ast.Dict):
            return CodePattern.RETURN_DICT

        # Check for computed returns
        if isinstance(value, (ast.BinOp, ast.Call, ast.Name, ast.Subscript, ast.Compare)):
            return CodePattern.RETURN_COMPUTED

        return None

    def _classify_assignment(self, node: ast.Assign) -> Optional[CodePattern]:
        """Classify assignment patterns."""
        if not node.targets:
            return None

        target = node.targets[0]
        value = node.value

        # Unpacking pattern (x, y = data or [a, b] = data)
        if isinstance(target, (ast.Tuple, ast.List)):
            return CodePattern.UNPACKING

        # Everything below requires a simple Name target
        if not isinstance(target, ast.Name):
            return None

        # Empty list initialization
        if isinstance(value, ast.List) and len(value.elts) == 0:
            return CodePattern.INIT_EMPTY_LIST

        # Empty dict initialization
        if isinstance(value, ast.Dict) and len(value.keys) == 0:
            return CodePattern.INIT_EMPTY_DICT

        # Counter/number initialization (x = 0)
        if isinstance(value, ast.Constant):
            if value.value == 0:
                return CodePattern.INIT_COUNTER

        # dict.get() with default
        if isinstance(value, ast.Call):
            if isinstance(value.func, ast.Attribute):
                if value.func.attr == "get":
                    return CodePattern.DICT_GET_DEFAULT

        # Default values (string, None, etc)
        if isinstance(value, ast.Constant):
            if value.value is not None:
                return CodePattern.INIT_DEFAULT_VALUE

        return None

    def _classify_try_except(self, node: ast.Try) -> Optional[CodePattern]:
        """Classify try-except patterns."""
        if not node.handlers:
            if node.finalbody:
                return CodePattern.TRY_FINALLY
            return None

        # Check what happens in except block
        for handler in node.handlers:
            if not handler.body:
                continue

            first_stmt = handler.body[0]

            # pass in except
            if isinstance(first_stmt, ast.Pass):
                return CodePattern.TRY_EXCEPT_PASS

            # logging in except
            if isinstance(first_stmt, ast.Expr):
                if isinstance(first_stmt.value, ast.Call):
                    if isinstance(first_stmt.value.func, ast.Attribute):
                        if "log" in first_stmt.value.func.attr.lower():
                            return CodePattern.TRY_EXCEPT_LOG

            # raise in except
            if isinstance(first_stmt, ast.Raise):
                return CodePattern.TRY_EXCEPT_RERAISE

        return None


def extract_patterns_from_code(code: str) -> List[SemanticNode]:
    """
    Extract semantic patterns from Python code string.

    Args:
        code: Python source code

    Returns:
        List of detected semantic patterns
    """
    try:
        tree = ast.parse(code)
        analyzer = SemanticPatternAnalyzer()
        analyzer.visit(tree)
        return analyzer.patterns
    except SyntaxError:
        return []
    except Exception as e:
        import sys

        print(f"Warning: Error extracting patterns: {e}", file=sys.stderr)
        return []


def extract_patterns_from_file(filepath) -> List[SemanticNode]:
    """
    Extract semantic patterns from a Python file.

    Args:
        filepath: Path to Python file

    Returns:
        List of detected semantic patterns
    """
    try:
        from pathlib import Path

        code = Path(filepath).read_text(encoding="utf-8")
        return extract_patterns_from_code(code)
    except Exception as e:
        import sys

        print(
            f"Warning: Could not extract patterns from {filepath}: {e}", file=sys.stderr
        )
        return []
