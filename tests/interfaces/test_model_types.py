#!/usr/bin/env python3
"""
Tests for Model Types and Interfaces

Comprehensive test coverage for:
- NextNodeSuggestion
- NextPatternSuggestion
- ASTContext
- ValidationResult
- SemanticNode
"""

import pytest
from src.interfaces.model_types import (
    NextNodeSuggestion,
    NextPatternSuggestion,
    ASTContext,
    ValidationResult,
    SemanticNode,
)
from src.trainers.semantic_pattern_extractor import CodePattern


class TestNextNodeSuggestion:
    """Test NextNodeSuggestion dataclass."""

    def test_creation(self):
        """Test creating a NextNodeSuggestion."""
        suggestion = NextNodeSuggestion(
            node_type="If",
            probability=0.65,
            confidence="HIGH",
            common_patterns=["if-none-check", "guard-clause"],
        )
        assert suggestion.node_type == "If"
        assert suggestion.probability == 0.65
        assert suggestion.confidence == "HIGH"
        assert len(suggestion.common_patterns) == 2

    def test_default_patterns(self):
        """Test that common_patterns defaults to empty list."""
        suggestion = NextNodeSuggestion(
            node_type="Return", probability=0.5, confidence="MEDIUM"
        )
        assert suggestion.common_patterns == []

    def test_probability_validation_min(self):
        """Test that probability < 0 raises error."""
        with pytest.raises(ValueError, match="Probability must be in"):
            NextNodeSuggestion(node_type="If", probability=-0.1, confidence="HIGH")

    def test_probability_validation_max(self):
        """Test that probability > 1 raises error."""
        with pytest.raises(ValueError, match="Probability must be in"):
            NextNodeSuggestion(node_type="If", probability=1.5, confidence="HIGH")

    def test_confidence_validation(self):
        """Test that invalid confidence raises error."""
        with pytest.raises(ValueError, match="Confidence must be"):
            NextNodeSuggestion(node_type="If", probability=0.5, confidence="SUPER_HIGH")

    def test_empty_node_type(self):
        """Test that empty node_type raises error."""
        with pytest.raises(ValueError, match="node_type cannot be empty"):
            NextNodeSuggestion(node_type="", probability=0.5, confidence="HIGH")

    def test_is_high_confidence(self):
        """Test is_high_confidence method."""
        high = NextNodeSuggestion("If", 0.5, "HIGH")
        medium = NextNodeSuggestion("If", 0.5, "MEDIUM")
        low = NextNodeSuggestion("If", 0.5, "LOW")

        assert high.is_high_confidence() is True
        assert medium.is_high_confidence() is False
        assert low.is_high_confidence() is False

    def test_repr(self):
        """Test string representation."""
        suggestion = NextNodeSuggestion("If", 0.654, "HIGH")
        repr_str = repr(suggestion)
        assert "NextNodeSuggestion" in repr_str
        assert "If" in repr_str
        assert "0.654" in repr_str


class TestNextPatternSuggestion:
    """Test NextPatternSuggestion dataclass."""

    def test_creation(self):
        """Test creating a NextPatternSuggestion."""
        suggestion = NextPatternSuggestion(
            pattern=CodePattern.IF_NONE_CHECK,
            probability=0.75,
            description="Check if value is None",
            code_template="if value is None:\n    return None",
            confidence="HIGH",
        )
        assert suggestion.pattern == CodePattern.IF_NONE_CHECK
        assert suggestion.probability == 0.75
        assert suggestion.confidence == "HIGH"

    def test_probability_validation(self):
        """Test probability validation."""
        with pytest.raises(ValueError):
            NextPatternSuggestion(
                pattern=CodePattern.LOOP_FILTER,
                probability=1.5,
                description="test",
                code_template="for x in y",
                confidence="HIGH",
            )

    def test_empty_description(self):
        """Test that empty description raises error."""
        with pytest.raises(ValueError, match="description cannot be empty"):
            NextPatternSuggestion(
                pattern=CodePattern.LOOP_FILTER,
                probability=0.5,
                description="",
                code_template="for x in y",
                confidence="HIGH",
            )

    def test_empty_template(self):
        """Test that empty code_template raises error."""
        with pytest.raises(ValueError, match="code_template cannot be empty"):
            NextPatternSuggestion(
                pattern=CodePattern.LOOP_FILTER,
                probability=0.5,
                description="Filter items",
                code_template="",
                confidence="HIGH",
            )

    def test_pattern_name(self):
        """Test pattern_name method."""
        suggestion = NextPatternSuggestion(
            pattern=CodePattern.LOOP_FILTER,
            probability=0.5,
            description="test",
            code_template="test",
            confidence="HIGH",
        )
        assert suggestion.pattern_name() == "LOOP_FILTER"

    def test_pattern_value(self):
        """Test pattern_value method."""
        suggestion = NextPatternSuggestion(
            pattern=CodePattern.LOOP_FILTER,
            probability=0.5,
            description="test",
            code_template="test",
            confidence="HIGH",
        )
        assert suggestion.pattern_value() == "loop-filter"

    def test_is_high_confidence(self):
        """Test is_high_confidence method."""
        high = NextPatternSuggestion(
            CodePattern.IF_NONE_CHECK, 0.5, "desc", "template", "HIGH"
        )
        assert high.is_high_confidence() is True

    def test_repr(self):
        """Test string representation."""
        suggestion = NextPatternSuggestion(
            CodePattern.IF_NONE_CHECK, 0.654, "test", "test", "HIGH"
        )
        repr_str = repr(suggestion)
        assert "NextPatternSuggestion" in repr_str
        assert "IF_NONE_CHECK" in repr_str


class TestASTContext:
    """Test ASTContext dataclass."""

    def test_creation(self):
        """Test creating an ASTContext."""
        ctx = ASTContext(
            parent_type="FunctionDef",
            current_node="If",
            ancestor_chain=["Module", "FunctionDef"],
        )
        assert ctx.parent_type == "FunctionDef"
        assert ctx.current_node == "If"
        assert ctx.ancestor_chain == ["Module", "FunctionDef"]

    def test_default_fields(self):
        """Test default field values."""
        ctx = ASTContext(parent_type="FunctionDef", current_node="If")
        assert ctx.ancestor_chain == []
        assert ctx.metadata == {}

    def test_empty_parent_type(self):
        """Test that empty parent_type raises error."""
        with pytest.raises(ValueError, match="parent_type cannot be empty"):
            ASTContext(parent_type="", current_node="If")

    def test_empty_current_node(self):
        """Test that empty current_node raises error."""
        with pytest.raises(ValueError, match="current_node cannot be empty"):
            ASTContext(parent_type="FunctionDef", current_node="")

    def test_to_state_order_1(self):
        """Test to_state with order=1."""
        ctx = ASTContext(
            parent_type="FunctionDef",
            current_node="If",
            ancestor_chain=["Module", "FunctionDef"],
        )
        state = ctx.to_state(order=1)
        assert state == ("If",)

    def test_to_state_order_2(self):
        """Test to_state with order=2."""
        ctx = ASTContext(
            parent_type="FunctionDef",
            current_node="If",
            ancestor_chain=["Module", "FunctionDef"],
        )
        state = ctx.to_state(order=2)
        assert state == ("FunctionDef", "If")

    def test_to_state_order_3(self):
        """Test to_state with order=3."""
        ctx = ASTContext(
            parent_type="FunctionDef",
            current_node="If",
            ancestor_chain=["Module", "FunctionDef"],
        )
        state = ctx.to_state(order=3)
        assert state == ("FunctionDef", "FunctionDef", "If")

    def test_to_state_order_3_short_chain(self):
        """Test to_state with order=3 and short ancestor chain."""
        ctx = ASTContext(
            parent_type="FunctionDef", current_node="If", ancestor_chain=["Module"]
        )
        state = ctx.to_state(order=3)
        assert state == ("Module", "FunctionDef", "If")

    def test_to_state_invalid_order(self):
        """Test to_state with invalid order."""
        ctx = ASTContext(parent_type="FunctionDef", current_node="If")
        with pytest.raises(ValueError, match="Order must be 1, 2, or 3"):
            ctx.to_state(order=4)

    def test_get_depth(self):
        """Test get_depth method."""
        ctx1 = ASTContext("Module", "FunctionDef")
        assert ctx1.get_depth() == 1

        ctx2 = ASTContext("FunctionDef", "If", ancestor_chain=["Module"])
        assert ctx2.get_depth() == 2

        ctx3 = ASTContext("If", "Return", ancestor_chain=["Module", "FunctionDef"])
        assert ctx3.get_depth() == 3

    def test_push(self):
        """Test push method for descending into child."""
        ctx1 = ASTContext(
            parent_type="Module", current_node="FunctionDef", ancestor_chain=[]
        )

        ctx2 = ctx1.push("If")

        assert ctx2.parent_type == "FunctionDef"
        assert ctx2.current_node == "If"
        assert ctx2.ancestor_chain == ["Module"]

    def test_push_preserves_metadata(self):
        """Test that push preserves metadata."""
        ctx1 = ASTContext(
            parent_type="FunctionDef",
            current_node="If",
            metadata={"function_name": "test_func"},
        )

        ctx2 = ctx1.push("Return")

        assert ctx2.metadata == {"function_name": "test_func"}

    def test_repr(self):
        """Test string representation."""
        ctx = ASTContext("FunctionDef", "If", ancestor_chain=["Module", "FunctionDef"])
        repr_str = repr(ctx)
        assert "ASTContext" in repr_str
        assert "depth=3" in repr_str


class TestValidationResult:
    """Test ValidationResult dataclass."""

    def test_creation_valid(self):
        """Test creating a valid result."""
        result = ValidationResult(
            is_valid=True, confidence_score=0.95, warnings=["Minor issue"]
        )
        assert result.is_valid is True
        assert result.confidence_score == 0.95
        assert len(result.warnings) == 1

    def test_creation_invalid(self):
        """Test creating an invalid result."""
        result = ValidationResult(
            is_valid=False, confidence_score=0.65, errors=["Missing None check"]
        )
        assert result.is_valid is False
        assert len(result.errors) == 1

    def test_confidence_validation_low(self):
        """Test confidence_score < 0 raises error."""
        with pytest.raises(ValueError, match="confidence_score must be"):
            ValidationResult(False, -0.1)

    def test_confidence_validation_high(self):
        """Test confidence_score > 1 raises error."""
        with pytest.raises(ValueError, match="confidence_score must be"):
            ValidationResult(False, 1.5)

    def test_has_warnings(self):
        """Test has_warnings method."""
        with_warnings = ValidationResult(True, 0.9, warnings=["test"])
        without_warnings = ValidationResult(True, 0.9)

        assert with_warnings.has_warnings() is True
        assert without_warnings.has_warnings() is False

    def test_has_errors(self):
        """Test has_errors method."""
        with_errors = ValidationResult(False, 0.5, errors=["test"])
        without_errors = ValidationResult(True, 0.9)

        assert with_errors.has_errors() is True
        assert without_errors.has_errors() is False

    def test_issue_count(self):
        """Test issue_count method."""
        result = ValidationResult(
            False, 0.7, warnings=["warning1", "warning2"], errors=["error1"]
        )
        assert result.issue_count() == 3

    def test_all_issues(self):
        """Test all_issues method."""
        result = ValidationResult(
            False, 0.7, warnings=["w1", "w2"], errors=["e1", "e2"]
        )
        issues = result.all_issues()
        assert len(issues) == 4
        assert "e1" in issues
        assert "w1" in issues

    def test_repr(self):
        """Test string representation."""
        valid_result = ValidationResult(True, 0.95)
        invalid_result = ValidationResult(False, 0.65, errors=["test"])

        assert "✓ VALID" in repr(valid_result)
        assert "✗ INVALID" in repr(invalid_result)


class TestSemanticNode:
    """Test SemanticNode dataclass."""

    def test_creation(self):
        """Test creating a SemanticNode."""
        node = SemanticNode(
            pattern=CodePattern.IF_NONE_CHECK, context={"line": 42, "variable": "x"}
        )
        assert node.pattern == CodePattern.IF_NONE_CHECK
        assert node.context == {"line": 42, "variable": "x"}

    def test_default_context(self):
        """Test that context defaults to empty dict."""
        node = SemanticNode(pattern=CodePattern.LOOP_FILTER)
        assert node.context == {}

    def test_none_pattern(self):
        """Test that None pattern raises error."""
        with pytest.raises(ValueError, match="pattern cannot be None"):
            SemanticNode(pattern=None)

    def test_non_dict_context(self):
        """Test that non-dict context raises error."""
        with pytest.raises(ValueError, match="context must be a dict"):
            SemanticNode(pattern=CodePattern.LOOP_FILTER, context="not a dict")

    def test_pattern_name(self):
        """Test pattern_name method."""
        node = SemanticNode(pattern=CodePattern.LOOP_FILTER)
        assert node.pattern_name() == "LOOP_FILTER"

    def test_pattern_value(self):
        """Test pattern_value method."""
        node = SemanticNode(pattern=CodePattern.LOOP_FILTER)
        assert node.pattern_value() == "loop-filter"

    def test_get_context(self):
        """Test get_context method."""
        node = SemanticNode(CodePattern.IF_NONE_CHECK, context={"line": 42, "var": "x"})
        assert node.get_context("line") == 42
        assert node.get_context("var") == "x"
        assert node.get_context("missing", "default") == "default"

    def test_has_context(self):
        """Test has_context method."""
        node = SemanticNode(CodePattern.LOOP_FILTER, context={"line": 42})
        assert node.has_context("line") is True
        assert node.has_context("missing") is False

    def test_hashable(self):
        """Test that SemanticNode is hashable."""
        node1 = SemanticNode(CodePattern.IF_NONE_CHECK)
        node2 = SemanticNode(CodePattern.IF_NONE_CHECK)

        # Should be able to use in set
        s = {node1, node2}
        assert len(s) == 1

        # Should be able to use as dict key
        d = {node1: "value"}
        assert d[node2] == "value"

    def test_equality(self):
        """Test equality comparison."""
        node1 = SemanticNode(CodePattern.LOOP_FILTER, context={"line": 42})
        node2 = SemanticNode(CodePattern.LOOP_FILTER, context={"line": 42})
        node3 = SemanticNode(CodePattern.LOOP_FILTER, context={"line": 43})

        assert node1 == node2
        assert node1 != node3

    def test_repr(self):
        """Test string representation."""
        node = SemanticNode(CodePattern.IF_NONE_CHECK, context={"line": 42})
        repr_str = repr(node)
        assert "SemanticNode" in repr_str
        assert "if-none-check" in repr_str


class TestIntegration:
    """Integration tests combining multiple types."""

    def test_context_to_state_usage(self):
        """Test using ASTContext.to_state for model queries."""
        ctx = ASTContext(
            parent_type="FunctionDef",
            current_node="If",
            ancestor_chain=["Module", "FunctionDef"],
        )

        state = ctx.to_state(order=2)

        # Should be a valid tuple for use as dict key
        states = {state: "value"}
        assert states[("FunctionDef", "If")] == "value"

    def test_suggestion_workflow(self):
        """Test a typical suggestion workflow."""
        # Start with context
        ctx = ASTContext("FunctionDef", "If")
        state = ctx.to_state(order=2)

        # Get a suggestion
        suggestion = NextNodeSuggestion(
            node_type="Return",
            probability=0.75,
            confidence="HIGH",
            common_patterns=["return-none", "early-return-success"],
        )

        # Validate suggestion
        assert suggestion.is_high_confidence()
        assert suggestion.probability > 0.5

    def test_semantic_pattern_workflow(self):
        """Test a typical semantic pattern workflow."""
        # Extract patterns
        nodes = [
            SemanticNode(CodePattern.FUNCTION_VALIDATOR),
            SemanticNode(CodePattern.IF_NONE_CHECK),
            SemanticNode(CodePattern.RETURN_BOOL),
        ]

        # Get suggestion for next pattern
        suggestion = NextPatternSuggestion(
            pattern=CodePattern.IF_EMPTY_CHECK,
            probability=0.55,
            description="Check if collection is empty",
            code_template="if not items:\n    return",
            confidence="MEDIUM",
        )

        # Validate
        assert suggestion.pattern_value() == "if-empty-check"
        assert not suggestion.is_high_confidence()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
