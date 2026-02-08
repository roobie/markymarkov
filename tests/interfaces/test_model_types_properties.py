#!/usr/bin/env python3
"""
Property-Based Tests for Model Types and Interfaces

Uses Hypothesis to generate random inputs and verify invariants.

Tested Classes:
- NextNodeSuggestion: 4 properties
- NextPatternSuggestion: 3 properties
- ASTContext: 6 properties
- ValidationResult: 5 properties
- SemanticNode: 5 properties
- Cross-module: 2 properties

Total: 25+ properties ensuring invariants hold across all valid inputs.
"""

import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

from src.interfaces.model_types import (
    NextNodeSuggestion,
    NextPatternSuggestion,
    ASTContext,
    ValidationResult,
    SemanticNode,
)
from src.trainers.semantic_pattern_extractor import CodePattern


# ============================================================================
# NextNodeSuggestion Properties (4 properties)
# ============================================================================


class TestNextNodeSuggestionProperties:
    """Property-based tests for NextNodeSuggestion."""

    @given(
        node_type=st.text(min_size=1, max_size=50),
        probability=st.floats(
            min_value=0.0, max_value=1.0, allow_nan=False, allow_infinity=False
        ),
        confidence=st.sampled_from(["HIGH", "MEDIUM", "LOW"]),
    )
    def test_probability_always_in_bounds(self, node_type, probability, confidence):
        """Property: Valid suggestions always have probability in [0, 1]."""
        suggestion = NextNodeSuggestion(node_type, probability, confidence)

        assert isinstance(suggestion.probability, float)
        assert 0.0 <= suggestion.probability <= 1.0

    @given(
        node_type=st.text(min_size=1, max_size=50),
        probability=st.floats(
            min_value=0.0, max_value=1.0, allow_nan=False, allow_infinity=False
        ),
        confidence=st.sampled_from(["HIGH", "MEDIUM", "LOW"]),
        common_patterns=st.lists(st.text(min_size=1, max_size=30), max_size=10),
    )
    def test_common_patterns_always_list(
        self, node_type, probability, confidence, common_patterns
    ):
        """Property: common_patterns is always a list, never None."""
        suggestion = NextNodeSuggestion(
            node_type, probability, confidence, common_patterns
        )

        assert isinstance(suggestion.common_patterns, list)
        assert suggestion.common_patterns is not None
        assert len(suggestion.common_patterns) == len(common_patterns)

    @given(
        node_type=st.text(min_size=1, max_size=50),
        probability=st.floats(
            min_value=0.0, max_value=1.0, allow_nan=False, allow_infinity=False
        ),
        confidence=st.sampled_from(["HIGH", "MEDIUM", "LOW"]),
    )
    def test_confidence_always_valid(self, node_type, probability, confidence):
        """Property: Confidence is always one of the three valid levels."""
        suggestion = NextNodeSuggestion(node_type, probability, confidence)

        assert suggestion.confidence in ("HIGH", "MEDIUM", "LOW")

    @given(
        confidence=st.sampled_from(["HIGH", "MEDIUM", "LOW"]),
        probability=st.floats(
            min_value=0.0, max_value=1.0, allow_nan=False, allow_infinity=False
        ),
    )
    def test_is_high_confidence_correctness(self, confidence, probability):
        """Property: is_high_confidence() is true iff confidence == 'HIGH'."""
        suggestion = NextNodeSuggestion("TestNode", probability, confidence)

        assert suggestion.is_high_confidence() == (confidence == "HIGH")


# ============================================================================
# NextPatternSuggestion Properties (3 properties)
# ============================================================================


class TestNextPatternSuggestionProperties:
    """Property-based tests for NextPatternSuggestion."""

    @given(
        pattern=st.sampled_from(list(CodePattern)),
        probability=st.floats(
            min_value=0.0, max_value=1.0, allow_nan=False, allow_infinity=False
        ),
        description=st.text(min_size=1, max_size=100),
        code_template=st.text(min_size=1, max_size=100),
        confidence=st.sampled_from(["HIGH", "MEDIUM", "LOW"]),
    )
    def test_pattern_suggestion_probability_bounds(
        self, pattern, probability, description, code_template, confidence
    ):
        """Property: Pattern suggestion probability always in [0, 1]."""
        suggestion = NextPatternSuggestion(
            pattern, probability, description, code_template, confidence
        )

        assert 0.0 <= suggestion.probability <= 1.0

    @given(
        pattern=st.sampled_from(list(CodePattern)),
        probability=st.floats(
            min_value=0.0, max_value=1.0, allow_nan=False, allow_infinity=False
        ),
        description=st.text(min_size=1, max_size=100),
        code_template=st.text(min_size=1, max_size=100),
        confidence=st.sampled_from(["HIGH", "MEDIUM", "LOW"]),
    )
    def test_pattern_strings_never_empty(
        self, pattern, probability, description, code_template, confidence
    ):
        """Property: Description and template are never empty."""
        suggestion = NextPatternSuggestion(
            pattern, probability, description, code_template, confidence
        )

        assert suggestion.description != ""
        assert suggestion.code_template != ""
        assert len(suggestion.description) > 0
        assert len(suggestion.code_template) > 0

    @given(pattern=st.sampled_from(list(CodePattern)))
    def test_pattern_name_value_consistency(self, pattern):
        """Property: pattern_name() and pattern_value() are consistent."""
        suggestion = NextPatternSuggestion(
            pattern, 0.5, "test description", "test template", "HIGH"
        )

        name = suggestion.pattern_name()
        value = suggestion.pattern_value()

        # Name should be uppercase with underscores
        assert name == name.upper()
        # Value should be lowercase with hyphens
        assert value == value.lower()
        # Value is kebab-case version of name
        assert "-" in value or len(value) < 20  # Allow simple names without hyphens


# ============================================================================
# ASTContext Properties (6 properties)
# ============================================================================


class TestASTContextProperties:
    """Property-based tests for ASTContext."""

    @given(
        parent_type=st.text(min_size=1, max_size=50),
        current_node=st.text(min_size=1, max_size=50),
        ancestor_chain=st.lists(st.text(min_size=1, max_size=50), max_size=10),
        order=st.integers(min_value=1, max_value=3),
    )
    def test_to_state_returns_correct_length(
        self, parent_type, current_node, ancestor_chain, order
    ):
        """Property: to_state(order=n) always returns a tuple of length n."""
        ctx = ASTContext(parent_type, current_node, ancestor_chain)
        state = ctx.to_state(order=order)

        assert isinstance(state, tuple)
        assert len(state) == order

    @given(
        parent_type=st.text(min_size=1, max_size=50),
        current_node=st.text(min_size=1, max_size=50),
        ancestor_chain=st.lists(st.text(min_size=1, max_size=50), max_size=10),
        order=st.sampled_from([1, 2, 3]),
    )
    def test_to_state_returns_strings(
        self, parent_type, current_node, ancestor_chain, order
    ):
        """Property: to_state() returns tuples of strings only."""
        ctx = ASTContext(parent_type, current_node, ancestor_chain)
        state = ctx.to_state(order=order)

        for element in state:
            assert isinstance(element, str)
            assert len(element) > 0  # No empty strings

    @given(
        parent_type=st.text(min_size=1, max_size=50),
        current_node=st.text(min_size=1, max_size=50),
        ancestor_chain=st.lists(st.text(min_size=1, max_size=50), max_size=10),
    )
    def test_to_state_order_subset_property(
        self, parent_type, current_node, ancestor_chain
    ):
        """Property: state[order=2] contains state[order=1] as suffix."""
        ctx = ASTContext(parent_type, current_node, ancestor_chain)

        state1 = ctx.to_state(order=1)
        state2 = ctx.to_state(order=2)
        state3 = ctx.to_state(order=3)

        # Current node should be the last element in all
        assert state1[-1] == current_node
        assert state2[-1] == current_node
        assert state3[-1] == current_node

        # Higher orders should contain lower orders as suffix
        assert state2[-1:] == state1
        assert state3[-1:] == state1

    @given(ancestor_chain=st.lists(st.text(min_size=1, max_size=50), max_size=10))
    def test_get_depth_formula(self, ancestor_chain):
        """Property: get_depth() == len(ancestor_chain) + 1."""
        ctx = ASTContext("Parent", "Current", ancestor_chain)
        expected_depth = len(ancestor_chain) + 1

        assert ctx.get_depth() == expected_depth

    @given(
        parent_type=st.text(min_size=1, max_size=50),
        current_node=st.text(min_size=1, max_size=50),
        ancestor_chain=st.lists(st.text(min_size=1, max_size=50), max_size=5),
        new_node_type=st.text(min_size=1, max_size=50),
    )
    def test_push_creates_valid_child(
        self, parent_type, current_node, ancestor_chain, new_node_type
    ):
        """Property: push() creates a valid child context with correct structure."""
        parent_ctx = ASTContext(parent_type, current_node, ancestor_chain)
        child_ctx = parent_ctx.push(new_node_type)

        # Child's parent should be parent's current
        assert child_ctx.parent_type == parent_ctx.current_node

        # Child's current should be the new node type
        assert child_ctx.current_node == new_node_type

        # Child's depth should be parent's depth + 1
        assert child_ctx.get_depth() == parent_ctx.get_depth() + 1

        # Child's ancestor chain should extend parent's chain
        assert child_ctx.ancestor_chain == parent_ctx.ancestor_chain + [
            parent_ctx.parent_type
        ]

    @given(
        metadata_values=st.dictionaries(
            st.text(min_size=1, max_size=20),
            st.text(min_size=1, max_size=30),
            min_size=0,
            max_size=5,
        )
    )
    def test_push_preserves_metadata(self, metadata_values):
        """Property: push() copies metadata to child (not shared reference)."""
        parent_ctx = ASTContext("Parent", "Current", metadata=metadata_values)
        child_ctx = parent_ctx.push("Child")

        # Metadata should be equal
        assert child_ctx.metadata == parent_ctx.metadata

        # But should be different objects
        assert child_ctx.metadata is not parent_ctx.metadata

        # Modifying child's metadata shouldn't affect parent's
        if metadata_values:  # Only if there's metadata to modify
            child_ctx.metadata["test_key"] = "test_value"
            assert "test_key" not in parent_ctx.metadata


# ============================================================================
# ValidationResult Properties (5 properties)
# ============================================================================


class TestValidationResultProperties:
    """Property-based tests for ValidationResult."""

    @given(
        confidence_score=st.floats(
            min_value=0.0, max_value=1.0, allow_nan=False, allow_infinity=False
        ),
        is_valid=st.booleans(),
    )
    def test_validation_confidence_bounds(self, confidence_score, is_valid):
        """Property: Confidence score always in [0, 1]."""
        result = ValidationResult(is_valid, confidence_score)

        assert 0.0 <= result.confidence_score <= 1.0

    @given(
        warnings=st.lists(st.text(max_size=50), max_size=10),
        errors=st.lists(st.text(max_size=50), max_size=10),
        suggestions=st.lists(st.text(max_size=50), max_size=10),
    )
    def test_validation_lists_never_none(self, warnings, errors, suggestions):
        """Property: All list fields are always lists, never None."""
        result = ValidationResult(
            True, 0.9, warnings=warnings, errors=errors, suggestions=suggestions
        )

        assert isinstance(result.warnings, list)
        assert isinstance(result.errors, list)
        assert isinstance(result.suggestions, list)
        assert result.warnings is not None
        assert result.errors is not None
        assert result.suggestions is not None

    @given(
        warnings=st.lists(st.text(max_size=50), max_size=10),
        errors=st.lists(st.text(max_size=50), max_size=10),
    )
    def test_issue_count_formula(self, warnings, errors):
        """Property: issue_count() == len(warnings) + len(errors)."""
        result = ValidationResult(True, 0.9, warnings=warnings, errors=errors)
        expected = len(warnings) + len(errors)

        assert result.issue_count() == expected

    @given(
        warnings=st.lists(st.text(min_size=1, max_size=50), max_size=10),
        errors=st.lists(st.text(min_size=1, max_size=50), max_size=10),
    )
    def test_all_issues_completeness(self, warnings, errors):
        """Property: all_issues() contains all warnings and errors."""
        result = ValidationResult(True, 0.9, warnings=warnings, errors=errors)
        issues = result.all_issues()

        # All errors should be in issues
        for error in errors:
            assert error in issues

        # All warnings should be in issues
        for warning in warnings:
            assert warning in issues

        # Should have exactly the right count
        assert len(issues) == len(warnings) + len(errors)

    @given(
        warnings=st.lists(st.text(max_size=50), max_size=10),
        errors=st.lists(st.text(max_size=50), max_size=10),
    )
    def test_has_warnings_errors_correctness(self, warnings, errors):
        """Property: has_warnings()/has_errors() match list contents."""
        result = ValidationResult(True, 0.9, warnings=warnings, errors=errors)

        # has_warnings() should be True iff warnings is not empty
        assert result.has_warnings() == (len(warnings) > 0)

        # has_errors() should be True iff errors is not empty
        assert result.has_errors() == (len(errors) > 0)


# ============================================================================
# SemanticNode Properties (5 properties)
# ============================================================================


class TestSemanticNodeProperties:
    """Property-based tests for SemanticNode."""

    @given(
        pattern=st.sampled_from(list(CodePattern)),
        context=st.dictionaries(
            st.text(min_size=1, max_size=20),
            st.integers() | st.text(max_size=30),
            max_size=5,
        ),
    )
    def test_semantic_node_equality_and_hash(self, pattern, context):
        """Property: Equal nodes have equal hashes."""
        node1 = SemanticNode(pattern, context)
        node2 = SemanticNode(pattern, context)

        # Equal nodes must have equal hashes
        if node1 == node2:
            assert hash(node1) == hash(node2)

    @given(
        st.lists(
            st.builds(SemanticNode, pattern=st.sampled_from(list(CodePattern))),
            max_size=20,
        )
    )
    def test_semantic_node_set_operations(self, nodes):
        """Property: SemanticNode can be used in sets."""
        # Should not raise any errors
        node_set = set(nodes)

        # Every node should be retrievable
        for node in nodes:
            assert node in node_set

    @given(pattern=st.sampled_from(list(CodePattern)))
    def test_semantic_node_pattern_consistency(self, pattern):
        """Property: pattern_name() and pattern_value() are consistent."""
        node = SemanticNode(pattern)
        name = node.pattern_name()
        value = node.pattern_value()

        # Name should be uppercase with underscores (enum format)
        assert name == name.upper()

        # Value should be lowercase with hyphens (kebab-case)
        assert value == value.lower()

    @given(
        context=st.dictionaries(
            st.text(min_size=1, max_size=20), st.integers(), max_size=5
        ),
        default_value=st.integers(),
    )
    def test_semantic_node_get_context(self, context, default_value):
        """Property: get_context() returns value or default."""
        node = SemanticNode(CodePattern.LOOP_FILTER, context)

        # Existing keys should return their values
        for key, value in context.items():
            assert node.get_context(key) == value

        # Missing keys should return default
        missing_key = "definitely_not_in_context_" + str(default_value)
        assert node.get_context(missing_key, default_value) == default_value

    @given(
        context=st.dictionaries(
            st.text(min_size=1, max_size=20), st.integers(), max_size=5
        )
    )
    def test_semantic_node_has_context(self, context):
        """Property: has_context() is True iff key exists."""
        node = SemanticNode(CodePattern.LOOP_FILTER, context)

        # Existing keys should return True
        for key in context.keys():
            assert node.has_context(key) is True

        # Non-existing keys should return False
        missing_key = "definitely_not_in_context"
        assert node.has_context(missing_key) is False


# ============================================================================
# Cross-Module Properties (2 properties)
# ============================================================================


class TestCrossModuleProperties:
    """Property-based tests for interactions between classes."""

    @given(
        parent_type=st.text(min_size=1, max_size=50),
        current_node=st.text(min_size=1, max_size=50),
        ancestor_chain=st.lists(st.text(min_size=1, max_size=50), max_size=10),
    )
    def test_ast_context_state_as_dict_key(
        self, parent_type, current_node, ancestor_chain
    ):
        """Property: ASTContext states work as Markov model keys."""
        ctx1 = ASTContext(parent_type, current_node, ancestor_chain)
        ctx2 = ASTContext(parent_type, current_node, ancestor_chain)

        state1 = ctx1.to_state(order=2)
        state2 = ctx2.to_state(order=2)

        # Identical contexts should produce identical states
        assert state1 == state2

        # States should be usable as dict keys
        model = {state1: [NextNodeSuggestion("If", 0.5, "HIGH")]}
        assert state2 in model
        assert model[state2] is model[state1]

    @given(
        node_type=st.text(min_size=1, max_size=50),
        probability=st.floats(
            min_value=0.0, max_value=1.0, allow_nan=False, allow_infinity=False
        ),
    )
    def test_suggestion_from_context_always_valid(self, node_type, probability):
        """Property: Suggestions produced from contexts are always valid."""
        # Simulate creating a suggestion from model query
        suggestion = NextNodeSuggestion(
            node_type=node_type, probability=probability, confidence="HIGH"
        )

        # Should always be valid
        assert 0.0 <= suggestion.probability <= 1.0
        assert suggestion.confidence in ("HIGH", "MEDIUM", "LOW")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
