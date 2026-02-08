#!/usr/bin/env python3
"""
Data Types and Interfaces for Marky Code Guidance System

Defines the core data structures used across all phases:
- Query results (NextNodeSuggestion, NextPatternSuggestion)
- Context tracking (ASTContext)
- Validation output (ValidationResult)
- Pattern extraction results (SemanticNode)
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from enum import Enum


# Forward import for type hints
try:
    from ..trainers.semantic_pattern_extractor import CodePattern
except ImportError:
    # Allow standalone usage
    CodePattern = None


@dataclass
class NextNodeSuggestion:
    """
    Suggestion for the next AST node type.

    Generated when querying an AST-level Markov model.
    Helps agents understand what syntactic structures should come next.

    Attributes:
        node_type: Name of the AST node type (e.g., 'FunctionDef', 'If', 'For')
        probability: Estimated probability [0.0, 1.0]
        confidence: Confidence level (HIGH, MEDIUM, LOW)
        common_patterns: List of semantic patterns often associated with this node

    Example:
        NextNodeSuggestion(
            node_type='If',
            probability=0.45,
            confidence='HIGH',
            common_patterns=['if-none-check', 'guard-clause']
        )
    """

    node_type: str
    probability: float
    confidence: str  # 'HIGH', 'MEDIUM', 'LOW'
    common_patterns: List[str] = field(default_factory=list)

    def __post_init__(self):
        """Validate fields after initialization."""
        if not 0.0 <= self.probability <= 1.0:
            raise ValueError(
                f"Probability must be in [0.0, 1.0], got {self.probability}"
            )

        if self.confidence not in ("HIGH", "MEDIUM", "LOW"):
            raise ValueError(
                f"Confidence must be HIGH/MEDIUM/LOW, got {self.confidence}"
            )

        if not self.node_type:
            raise ValueError("node_type cannot be empty")

    def is_high_confidence(self) -> bool:
        """Check if this suggestion has high confidence."""
        return self.confidence == "HIGH"

    def __repr__(self) -> str:
        """Pretty representation."""
        return (
            f"NextNodeSuggestion(node_type={self.node_type!r}, "
            f"probability={self.probability:.3f}, confidence={self.confidence})"
        )


@dataclass
class NextPatternSuggestion:
    """
    Suggestion for the next semantic code pattern.

    Generated when querying a semantic-level Markov model.
    Helps agents understand what high-level patterns should come next.

    Attributes:
        pattern: CodePattern enum value
        probability: Estimated probability [0.0, 1.0]
        description: Human-readable description of the pattern
        code_template: Example code snippet showing the pattern
        confidence: Confidence level (HIGH, MEDIUM, LOW)

    Example:
        NextPatternSuggestion(
            pattern=CodePattern.IF_NONE_CHECK,
            probability=0.65,
            description='Check if value is None before use',
            code_template='if value is None:\\n    return None',
            confidence='HIGH'
        )
    """

    pattern: "CodePattern"
    probability: float
    description: str
    code_template: str
    confidence: str  # 'HIGH', 'MEDIUM', 'LOW'

    def __post_init__(self):
        """Validate fields after initialization."""
        if not 0.0 <= self.probability <= 1.0:
            raise ValueError(
                f"Probability must be in [0.0, 1.0], got {self.probability}"
            )

        if self.confidence not in ("HIGH", "MEDIUM", "LOW"):
            raise ValueError(
                f"Confidence must be HIGH/MEDIUM/LOW, got {self.confidence}"
            )

        if not self.description:
            raise ValueError("description cannot be empty")

        if not self.code_template:
            raise ValueError("code_template cannot be empty")

    def is_high_confidence(self) -> bool:
        """Check if this suggestion has high confidence."""
        return self.confidence == "HIGH"

    def pattern_name(self) -> str:
        """Get the pattern name as a string."""
        if self.pattern is None:
            return "UNKNOWN"
        return self.pattern.name if hasattr(self.pattern, "name") else str(self.pattern)

    def pattern_value(self) -> str:
        """Get the pattern value (kebab-case name)."""
        if self.pattern is None:
            return "unknown"
        return (
            self.pattern.value
            if hasattr(self.pattern, "value")
            else str(self.pattern).lower()
        )

    def __repr__(self) -> str:
        """Pretty representation."""
        pattern_str = self.pattern_name() if self.pattern else "None"
        return (
            f"NextPatternSuggestion(pattern={pattern_str}, "
            f"probability={self.probability:.3f}, confidence={self.confidence})"
        )


@dataclass
class ASTContext:
    """
    Context information for tracking position in AST.

    Used to build the current state for querying Markov models.
    Tracks the path through the AST and recent node types.

    Attributes:
        parent_type: Type of parent node (e.g., 'FunctionDef', 'If')
        current_node: Type of current node (e.g., 'Return', 'Assign')
        ancestor_chain: List of ancestor node types from root to parent
        metadata: Additional context (line number, scope, etc.)

    Example:
        ASTContext(
            parent_type='FunctionDef',
            current_node='If',
            ancestor_chain=['Module', 'FunctionDef'],
            metadata={'function_name': 'validate', 'line': 42}
        )
    """

    parent_type: str
    current_node: str
    ancestor_chain: List[str] = field(default_factory=list)
    metadata: Dict = field(default_factory=dict)

    def __post_init__(self):
        """Validate fields after initialization."""
        if not self.parent_type:
            raise ValueError("parent_type cannot be empty")

        if not self.current_node:
            raise ValueError("current_node cannot be empty")

        if not isinstance(self.ancestor_chain, list):
            raise ValueError("ancestor_chain must be a list")

    def to_state(self, order: int = 2) -> Tuple:
        """
        Convert context to a Markov state tuple.

        Args:
            order: Markov chain order (1, 2, or 3)
                - 1: Just current node
                - 2: Parent + current
                - 3: Grandparent + parent + current

        Returns:
            Tuple of node types representing the state

        Raises:
            ValueError: If order not in [1, 2, 3]

        Examples:
            >>> ctx = ASTContext(
            ...     parent_type='FunctionDef',
            ...     current_node='If',
            ...     ancestor_chain=['Module', 'FunctionDef']
            ... )
            >>> ctx.to_state(order=1)
            ('If',)
            >>> ctx.to_state(order=2)
            ('FunctionDef', 'If')
            >>> ctx.to_state(order=3)
            ('FunctionDef', 'FunctionDef', 'If')
        """
        if order not in (1, 2, 3):
            raise ValueError(f"Order must be 1, 2, or 3, got {order}")

        if order == 1:
            # Just current node
            return (self.current_node,)

        elif order == 2:
            # Parent + current
            return (self.parent_type, self.current_node)

        else:  # order == 3
            # Grandparent + parent + current
            grandparent = (
                self.ancestor_chain[-1] if self.ancestor_chain else self.parent_type
            )
            return (grandparent, self.parent_type, self.current_node)

    def get_depth(self) -> int:
        """Get the depth in the AST (length of ancestor chain + 1)."""
        return len(self.ancestor_chain) + 1

    def push(self, new_node_type: str) -> "ASTContext":
        """
        Create a new context by descending into a child node.

        Args:
            new_node_type: Type of the new current node

        Returns:
            New ASTContext with updated state
        """
        new_ancestors = self.ancestor_chain + [self.parent_type]
        return ASTContext(
            parent_type=self.current_node,
            current_node=new_node_type,
            ancestor_chain=new_ancestors,
            metadata=self.metadata.copy(),
        )

    def __repr__(self) -> str:
        """Pretty representation."""
        depth = self.get_depth()
        return (
            f"ASTContext(depth={depth}, parent={self.parent_type!r}, "
            f"current={self.current_node!r})"
        )


@dataclass
class ValidationResult:
    """
    Result of code validation.

    Used to report whether generated/suggested code is valid according
    to the learned patterns and models.

    Attributes:
        is_valid: Whether the code is considered valid
        confidence_score: Confidence in the validation [0.0, 1.0]
        warnings: List of warning messages
        errors: List of error messages
        suggestions: List of suggestions for improvement
        metadata: Additional validation metadata

    Example:
        ValidationResult(
            is_valid=False,
            confidence_score=0.85,
            warnings=['Unusual pattern detected'],
            errors=['Missing None check for optional parameter'],
            suggestions=['Add: if value is None: return None'],
            metadata={'matched_patterns': ['if-none-check']}
        )
    """

    is_valid: bool
    confidence_score: float
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    suggestions: List[str] = field(default_factory=list)
    metadata: Dict = field(default_factory=dict)

    def __post_init__(self):
        """Validate fields after initialization."""
        if not 0.0 <= self.confidence_score <= 1.0:
            raise ValueError(
                f"confidence_score must be in [0.0, 1.0], got {self.confidence_score}"
            )

        if not isinstance(self.warnings, list):
            raise ValueError("warnings must be a list")

        if not isinstance(self.errors, list):
            raise ValueError("errors must be a list")

        if not isinstance(self.suggestions, list):
            raise ValueError("suggestions must be a list")

    def has_warnings(self) -> bool:
        """Check if there are any warnings."""
        return len(self.warnings) > 0

    def has_errors(self) -> bool:
        """Check if there are any errors."""
        return len(self.errors) > 0

    def issue_count(self) -> int:
        """Get total number of warnings and errors."""
        return len(self.warnings) + len(self.errors)

    def all_issues(self) -> List[str]:
        """Get all warnings and errors combined."""
        return self.errors + self.warnings

    def __repr__(self) -> str:
        """Pretty representation."""
        status = "✓ VALID" if self.is_valid else "✗ INVALID"
        issues = self.issue_count()
        return (
            f"ValidationResult({status}, confidence={self.confidence_score:.2f}, "
            f"issues={issues})"
        )


@dataclass
class SemanticNode:
    """
    A semantic pattern node extracted from code.

    Used by the SemanticPatternExtractor to represent detected patterns.
    Can be used standalone or collected into sequences for training.

    Attributes:
        pattern: CodePattern enum identifying the pattern type
        context: Optional dict with additional context about the pattern
                (e.g., line number, variable names, condition details)

    Example:
        SemanticNode(
            pattern=CodePattern.IF_NONE_CHECK,
            context={
                'line': 42,
                'variable': 'value',
                'parent_function': 'process_data',
                'is_guard_clause': True
            }
        )
    """

    pattern: "CodePattern"
    context: Optional[Dict] = None

    def __post_init__(self):
        """Validate fields after initialization."""
        if self.pattern is None:
            raise ValueError("pattern cannot be None")

        if self.context is None:
            self.context = {}

        if not isinstance(self.context, dict):
            raise ValueError("context must be a dict or None")

    def pattern_name(self) -> str:
        """Get pattern name (enum member name)."""
        return self.pattern.name if hasattr(self.pattern, "name") else str(self.pattern)

    def pattern_value(self) -> str:
        """Get pattern value (kebab-case string)."""
        return (
            self.pattern.value
            if hasattr(self.pattern, "value")
            else str(self.pattern).lower()
        )

    def get_context(self, key: str, default=None):
        """Get a context value by key."""
        return self.context.get(key, default) if self.context else default

    def has_context(self, key: str) -> bool:
        """Check if a context key exists."""
        return bool(self.context and key in self.context)

    def __hash__(self):
        """Allow SemanticNode to be used in sets and as dict keys."""
        return hash(
            (self.pattern, frozenset(self.context.items()) if self.context else None)
        )

    def __eq__(self, other):
        """Check equality with other SemanticNode."""
        if not isinstance(other, SemanticNode):
            return NotImplemented
        return self.pattern == other.pattern and self.context == other.context

    def __repr__(self) -> str:
        """Pretty representation."""
        pattern_str = self.pattern_value()
        has_ctx = len(self.context) > 0 if self.context else False
        ctx_str = f", context_items={len(self.context)}" if has_ctx else ""
        return f"SemanticNode(pattern={pattern_str!r}{ctx_str})"


# Type aliases for convenience
NodeSequence = List[str]  # Sequence of AST node type names
PatternSequence = List[SemanticNode]  # Sequence of semantic patterns
State = Tuple[str, ...]  # Markov chain state (tuple of node types)
ModelQuery = Tuple[str, ...]  # Query to a Markov model


__all__ = [
    "NextNodeSuggestion",
    "NextPatternSuggestion",
    "ASTContext",
    "ValidationResult",
    "SemanticNode",
    "NodeSequence",
    "PatternSequence",
    "State",
    "ModelQuery",
]
