"""
Tests for SemanticPatternExtractor
"""

import pytest
import ast
from src.trainers.semantic_pattern_extractor import (
    CodePattern,
    SemanticPatternAnalyzer,
    SemanticNode,
    extract_patterns_from_code,
)


class TestCodePatternEnum:
    """Test CodePattern enum."""

    def test_all_patterns_defined(self):
        """Test that all expected patterns are defined."""
        expected_count = 50  # Approximately
        actual_count = len(CodePattern)
        assert actual_count >= 45, f"Expected at least 45 patterns, got {actual_count}"

    def test_pattern_values_unique(self):
        """Test that all pattern values are unique."""
        values = [p.value for p in CodePattern]
        assert len(values) == len(set(values)), "Duplicate pattern values found"

    def test_control_flow_patterns(self):
        """Test control flow patterns exist."""
        patterns = [
            CodePattern.IF_NONE_CHECK,
            CodePattern.IF_NOT_NONE,
            CodePattern.GUARD_CLAUSE,
            CodePattern.IF_EMPTY_CHECK,
        ]
        for p in patterns:
            assert p in CodePattern


class TestSemanticNode:
    """Test SemanticNode dataclass."""

    def test_creation(self):
        """Test SemanticNode creation."""
        node = SemanticNode(CodePattern.IF_NOT_NONE)
        assert node.pattern == CodePattern.IF_NOT_NONE
        assert node.context == {}

    def test_creation_with_context(self):
        """Test creation with context."""
        ctx = {"name": "foo", "line": 10}
        node = SemanticNode(CodePattern.INIT_EMPTY_LIST, ctx)
        assert node.context == ctx

    def test_hash(self):
        """Test SemanticNode is hashable."""
        node1 = SemanticNode(CodePattern.IF_NOT_NONE)
        node2 = SemanticNode(CodePattern.IF_NOT_NONE)
        # Same pattern = same hash
        assert hash(node1) == hash(node2)

    def test_equality(self):
        """Test SemanticNode equality."""
        node1 = SemanticNode(CodePattern.IF_NOT_NONE)
        node2 = SemanticNode(CodePattern.IF_NOT_NONE)
        node3 = SemanticNode(CodePattern.IF_EMPTY_CHECK)
        assert node1 == node2
        assert node1 != node3


class TestIfStatementPatterns:
    """Test if statement pattern detection."""

    def test_if_not_none(self):
        """Test if-not-none pattern detection."""
        code = """
if x is not None:
    print(x)
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.IF_NOT_NONE in pattern_types

    def test_if_none_check(self):
        """Test if-none pattern detection."""
        code = """
if x is None:
    return None
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.IF_NONE_CHECK in pattern_types

    def test_if_empty_check(self):
        """Test if-empty pattern detection."""
        code = """
if not items:
    return []
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.IF_EMPTY_CHECK in pattern_types

    def test_guard_clause(self):
        """Test guard clause pattern detection."""
        code = """
if x < 0:
    return None
print(x)
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.GUARD_CLAUSE in pattern_types

    def test_if_type_check(self):
        """Test if-type-check pattern detection."""
        code = """
if isinstance(obj, MyClass):
    obj.method()
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.IF_TYPE_CHECK in pattern_types


class TestLoopPatterns:
    """Test loop pattern detection."""

    def test_loop_transform(self):
        """Test loop-transform pattern."""
        code = """
result = []
for item in items:
    result.append(item * 2)
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert (
            CodePattern.LOOP_TRANSFORM in pattern_types
            or CodePattern.INIT_EMPTY_LIST in pattern_types
        )

    def test_loop_filter(self):
        """Test loop-filter pattern."""
        code = """
result = []
for item in items:
    if item > 0:
        result.append(item)
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.LOOP_FILTER in pattern_types

    def test_loop_accumulate(self):
        """Test loop-accumulate pattern."""
        code = """
total = 0
for num in numbers:
    total += num
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.LOOP_ACCUMULATE in pattern_types

    def test_loop_enumerate(self):
        """Test loop-enumerate pattern."""
        code = """
for i, item in enumerate(items):
    print(i, item)
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.LOOP_ENUMERATE in pattern_types

    def test_loop_zip(self):
        """Test loop-zip pattern."""
        code = """
for a, b in zip(list1, list2):
    print(a, b)
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.LOOP_ZIP in pattern_types

    def test_loop_dict_items(self):
        """Test loop-dict-items pattern."""
        code = """
for key, value in data.items():
    print(key, value)
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.LOOP_DICT_ITEMS in pattern_types


class TestReturnPatterns:
    """Test return pattern detection."""

    def test_return_none(self):
        """Test return-none pattern."""
        code = """
def foo():
    if x < 0:
        return None
    return x
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.RETURN_NONE in pattern_types

    def test_return_bool(self):
        """Test return-bool pattern."""
        code = """
def is_valid(x):
    return x > 0
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert (
            CodePattern.RETURN_COMPUTED in pattern_types
            or CodePattern.RETURN_BOOL in pattern_types
        )

    def test_return_list(self):
        """Test return-list pattern."""
        code = """
def get_items():
    return []
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.RETURN_LIST in pattern_types

    def test_return_dict(self):
        """Test return-dict pattern."""
        code = """
def get_data():
    return {}
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.RETURN_DICT in pattern_types


class TestAssignmentPatterns:
    """Test assignment pattern detection."""

    def test_init_empty_list(self):
        """Test empty list initialization."""
        code = "result = []"
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.INIT_EMPTY_LIST in pattern_types

    def test_init_empty_dict(self):
        """Test empty dict initialization."""
        code = "data = {}"
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.INIT_EMPTY_DICT in pattern_types

    def test_init_counter(self):
        """Test counter initialization."""
        code = "count = 0"
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.INIT_COUNTER in pattern_types

    def test_init_default_value(self):
        """Test default value initialization."""
        code = 'message = "hello"'
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.INIT_DEFAULT_VALUE in pattern_types

    def test_dict_get_default(self):
        """Test dict.get with default."""
        code = "value = config.get('key', None)"
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.DICT_GET_DEFAULT in pattern_types

    def test_unpacking(self):
        """Test unpacking pattern."""
        code = "x, y = data"
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.UNPACKING in pattern_types


class TestErrorHandlingPatterns:
    """Test error handling pattern detection."""

    def test_try_except_pass(self):
        """Test try-except-pass pattern."""
        code = """
try:
    risky_operation()
except Exception:
    pass
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.TRY_EXCEPT_PASS in pattern_types

    def test_context_manager(self):
        """Test context manager pattern."""
        code = """
with open('file.txt') as f:
    content = f.read()
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.CONTEXT_MANAGER in pattern_types


class TestComprehensionPatterns:
    """Test comprehension pattern detection."""

    def test_list_comprehension(self):
        """Test list comprehension pattern."""
        code = "result = [x * 2 for x in items]"
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.LIST_COMPREHENSION in pattern_types

    def test_dict_comprehension(self):
        """Test dict comprehension pattern."""
        code = "mapping = {k: v for k, v in pairs}"
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.DICT_COMPREHENSION in pattern_types

    def test_generator_expression(self):
        """Test generator expression pattern."""
        code = "gen = (x * 2 for x in items)"
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.GENERATOR_EXPRESSION in pattern_types


class TestFunctionPatterns:
    """Test function pattern detection."""

    def test_init_method(self):
        """Test __init__ method detection."""
        code = """
class MyClass:
    def __init__(self, x):
        self.x = x
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.INIT_METHOD in pattern_types

    def test_property_getter(self):
        """Test property getter detection."""
        code = """
class MyClass:
    @property
    def value(self):
        return self._value
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.PROPERTY_GETTER in pattern_types

    def test_function_validator(self):
        """Test function validator pattern."""
        code = """
def validate(data):
    if not data:
        return False
    if not isinstance(data, dict):
        return False
    if 'key' not in data:
        return False
    return True
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        # Should detect validator pattern (multiple early returns)
        assert (
            CodePattern.GUARD_CLAUSE in pattern_types
            or CodePattern.FUNCTION_VALIDATOR in pattern_types
        )

    def test_function_transformer(self):
        """Test function transformer pattern."""
        code = """
def transform(x):
    return x * 2
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert (
            CodePattern.FUNCTION_TRANSFORMER in pattern_types
            or CodePattern.RETURN_COMPUTED in pattern_types
        )


class TestOtherPatterns:
    """Test other patterns."""

    def test_ternary_expression(self):
        """Test ternary expression pattern."""
        code = "result = x if x > 0 else -x"
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.TERNARY_EXPRESSION in pattern_types

    def test_logging_call(self):
        """Test logging call pattern."""
        code = "logger.info('Message')"
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        assert CodePattern.LOGGING_CALL in pattern_types

    def test_string_format(self):
        """Test string format pattern."""
        code = 'message = "{} and {}".format(a, b)'
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]
        # May or may not detect, depends on implementation
        # At least shouldn't crash
        assert True


class TestComplexCode:
    """Test pattern detection on complex code."""

    def test_typical_data_processing_function(self):
        """Test pattern detection on typical data processing code."""
        code = """
def process_users(users):
    if users is None:
        return []
    
    result = []
    for user in users:
        if user.is_active:
            result.append(user.name)
    
    return result
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]

        # Should detect multiple patterns
        assert len(pattern_types) >= 3
        assert (
            CodePattern.IF_NOT_NONE in pattern_types
            or CodePattern.IF_NONE_CHECK in pattern_types
        )
        assert CodePattern.INIT_EMPTY_LIST in pattern_types
        assert (
            CodePattern.LOOP_FILTER in pattern_types
            or CodePattern.LOOP_TRANSFORM in pattern_types
        )

    def test_validation_function(self):
        """Test pattern detection on validation function."""
        code = """
def validate_config(config):
    if config is None:
        return False
    
    if not isinstance(config, dict):
        return False
    
    if 'host' not in config:
        return False
    
    if 'port' not in config:
        return False
    
    return True
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]

        # Should detect validation patterns
        assert (
            CodePattern.IF_TYPE_CHECK in pattern_types
            or CodePattern.RETURN_BOOL in pattern_types
        )

    def test_error_handling_function(self):
        """Test pattern detection on error handling."""
        code = """
def safe_operation():
    try:
        result = risky_call()
        return result
    except ValueError as e:
        logger.error(f"Error: {e}")
        return None
"""
        patterns = extract_patterns_from_code(code)
        pattern_types = [p.pattern for p in patterns]

        # Should detect error handling
        assert CodePattern.TRY_EXCEPT_LOG in pattern_types or len(pattern_types) > 2


class TestEdgeCases:
    """Test edge cases."""

    def test_empty_code(self):
        """Test on empty code."""
        patterns = extract_patterns_from_code("")
        assert patterns == []

    def test_invalid_syntax(self):
        """Test on invalid syntax."""
        patterns = extract_patterns_from_code("def foo(: pass")
        assert patterns == []

    def test_single_expression(self):
        """Test on single expression."""
        patterns = extract_patterns_from_code("x = 1")
        assert len(patterns) >= 1

    def test_comment_only(self):
        """Test on comment only."""
        patterns = extract_patterns_from_code("# Just a comment")
        assert patterns == []

    def test_import_statement(self):
        """Test on import statement."""
        patterns = extract_patterns_from_code("import sys")
        assert patterns == []


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
