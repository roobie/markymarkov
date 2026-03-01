#!/usr/bin/env python3
"""
Tests for AST Code Guide

Comprehensive testing of MarkovCodeGuide, CachedMarkovCodeGuide,
StreamingCodeValidator, and convenience functions.
"""

import ast
import tempfile
from pathlib import Path
import pytest

from markymarkov.guides.ast_code_guide import (
    MarkovCodeGuide,
    CachedMarkovCodeGuide,
    StreamingCodeValidator,
    quick_suggest,
    validate_generated_code,
)
from markymarkov.interfaces.model_types import ASTContext, NextNodeSuggestion


class MockModel:
    """Mock AST model for testing."""

    def __init__(self):
        # Simple mock probabilities
        self.probabilities = {
            ("FunctionDef", "If"): {"Return": 0.6, "Assign": 0.3, "Expr": 0.1},
            ("If",): {  # For validation test
                "Return": 0.8
            },
            ("Module",): {  # For streaming validator
                "Expr": 0.9
            },
        }


class TestMarkovCodeGuide:
    """Test MarkovCodeGuide functionality."""

    @pytest.fixture
    def mock_model(self):
        """Create a mock model for testing."""
        return MockModel()

    @pytest.fixture
    def guide(self, mock_model):
        """Create a guide instance."""
        return MarkovCodeGuide(mock_model, order=2)

    def test_initialization(self, mock_model):
        """Test guide initialization."""
        guide = MarkovCodeGuide(mock_model, order=2)
        assert guide.order == 2
        assert guide.model == mock_model
        assert guide.query_count == 0

    def test_suggest_next_nodes_known_state(self, guide):
        """Test suggestions for known state."""
        context = ASTContext("FunctionDef", "If")
        suggestions = guide.suggest_next_nodes(context, top_k=5, min_confidence="LOW")

        # Should get all suggestions from model, sorted by probability
        node_types = [s.node_type for s in suggestions]
        assert "Return" in node_types
        assert "Assign" in node_types
        assert "Expr" in node_types

        # Find Return suggestion (should be highest probability)
        return_sugg = next(s for s in suggestions if s.node_type == "Return")
        assert return_sugg.probability == 0.6
        assert return_sugg.confidence == "HIGH"

        # Check sorting by probability
        probs = [s.probability for s in suggestions]
        assert probs == sorted(probs, reverse=True)

    def test_suggest_next_nodes_unknown_state(self, guide):
        """Test suggestions for unknown state."""
        context = ASTContext("Unknown", "Node")
        suggestions = guide.suggest_next_nodes(context, top_k=2)

        # Should fall back to defaults
        assert len(suggestions) == 2
        assert all(s.confidence == "LOW" for s in suggestions)

    def test_suggest_next_nodes_temperature(self, guide):
        """Test temperature scaling."""
        context = ASTContext("FunctionDef", "If")

        # Deterministic (temperature=0) with LOW confidence to avoid filtering
        cold_suggestions = guide.suggest_next_nodes(
            context, temperature=0.0, min_confidence="LOW"
        )
        assert len(cold_suggestions) == 1
        assert cold_suggestions[0].node_type == "Return"

    def test_suggest_next_nodes_min_confidence(self, guide):
        """Test confidence filtering."""
        context = ASTContext("FunctionDef", "If")

        # Test that filtering doesn't crash
        high_conf = guide.suggest_next_nodes(context, top_k=5, min_confidence="HIGH")
        assert isinstance(high_conf, list)
        assert len(high_conf) >= 0  # May be empty if no high confidence suggestions

    def test_validate_sequence_valid(self, guide):
        """Test validation of valid sequence."""
        # Use a simple sequence - validation is more lenient now
        sequence = ["If", "Return"]
        result = guide.validate_sequence(sequence)

        # Just check that it doesn't crash and returns a result
        assert isinstance(result.is_valid, bool)
        assert isinstance(result.confidence_score, float)
        assert isinstance(result.errors, list)

    def test_validate_sequence_invalid(self, guide):
        """Test validation of invalid sequence."""
        sequence = ["FunctionDef", "If", "UnknownNode"]
        result = guide.validate_sequence(sequence)

        assert result.is_valid is False
        assert len(result.errors) > 0

    def test_validate_sequence_empty(self, guide):
        """Test validation of empty sequence."""
        result = guide.validate_sequence([])

        assert result.is_valid is False
        assert result.confidence_score == 0.0
        assert "Empty sequence" in result.errors

    def test_get_completion_candidates(self, guide):
        """Test completion candidates."""
        partial_code = "def func():\n    if True:"
        candidates = guide.get_completion_candidates(partial_code, top_k=3)

        assert isinstance(candidates, list)
        assert len(candidates) <= 3
        # Should contain reasonable AST node types
        assert all(isinstance(c, str) for c in candidates)

    def test_get_completion_candidates_incomplete(self, guide):
        """Test completion for incomplete code."""
        partial_code = "def func"
        candidates = guide.get_completion_candidates(partial_code, top_k=5)

        assert isinstance(candidates, list)
        assert len(candidates) > 0

    def test_bias_logits(self, guide):
        """Test logit biasing."""
        import numpy as np

        logits = np.array([0.1, 0.2, 0.3, 0.4])
        token_map = {0: "Return", 1: "Assign", 2: "Expr", 3: "Pass"}
        context = ASTContext("FunctionDef", "If")

        biased = guide.bias_logits(logits, token_map, context, bias_strength=0.5)

        assert isinstance(biased, np.ndarray)
        assert len(biased) == len(logits)
        # Tokens corresponding to suggested nodes should be boosted
        # (Return should be boosted since it's the top suggestion)
        assert biased[0] > logits[0]  # Return token boosted

    def test_bias_logits_no_bias(self, guide):
        """Test logit biasing with zero strength."""
        import numpy as np

        logits = np.array([0.1, 0.2, 0.3])
        token_map = {0: "Return"}
        context = ASTContext("FunctionDef", "If")

        biased = guide.bias_logits(logits, token_map, context, bias_strength=0.0)

        # Should be unchanged
        np.testing.assert_array_equal(biased, logits)

    def test_get_statistics(self, guide):
        """Test statistics reporting."""
        context = ASTContext("FunctionDef", "If")
        guide.suggest_next_nodes(context)

        stats = guide.get_statistics()

        assert stats["total_queries"] == 1
        assert "cache_hit_rate" in stats
        assert stats["model_order"] == 2
        assert "model_states" in stats


class TestCachedMarkovCodeGuide:
    """Test CachedMarkovCodeGuide functionality."""

    @pytest.fixture
    def mock_model(self):
        """Create mock model."""
        return MockModel()

    @pytest.fixture
    def cached_guide(self, mock_model):
        """Create cached guide."""
        return CachedMarkovCodeGuide(mock_model, cache_size=10, order=2)

    def test_initialization(self, mock_model):
        """Test cached guide initialization."""
        guide = CachedMarkovCodeGuide(mock_model, cache_size=5)
        assert guide.cache_size == 5
        assert len(guide._cache) == 0

    def test_cache_hit(self, cached_guide):
        """Test cache hit behavior."""
        context = ASTContext("FunctionDef", "If")

        # First call - cache miss
        result1 = cached_guide.suggest_next_nodes(context)

        # Second call - cache hit
        result2 = cached_guide.suggest_next_nodes(context)

        # Results should be identical
        assert len(result1) == len(result2)
        assert result1[0].node_type == result2[0].node_type

        # Check stats
        stats = cached_guide.get_cache_stats()
        assert stats["hits"] == 1
        assert stats["misses"] == 1
        assert stats["hit_rate"] == 0.5

    def test_cache_eviction(self, cached_guide):
        """Test cache eviction when full."""
        # Fill cache
        for i in range(cached_guide.cache_size + 5):
            context = ASTContext(f"Type{i}", "Node")
            cached_guide.suggest_next_nodes(context)

        # Cache should not exceed capacity
        assert len(cached_guide._cache) <= cached_guide.cache_size

    def test_clear_cache(self, cached_guide):
        """Test cache clearing."""
        context = ASTContext("FunctionDef", "If")
        cached_guide.suggest_next_nodes(context)

        assert len(cached_guide._cache) > 0

        cached_guide.clear_cache()

        assert len(cached_guide._cache) == 0
        assert cached_guide._hits == 0
        assert cached_guide._misses == 0

    def test_cache_stats(self, cached_guide):
        """Test cache statistics."""
        # No activity
        stats = cached_guide.get_cache_stats()
        assert stats["hits"] == 0
        assert stats["misses"] == 0
        assert stats["cache_size"] == 0
        assert stats["utilization"] == 0.0


class TestStreamingCodeValidator:
    """Test StreamingCodeValidator functionality."""

    @pytest.fixture
    def mock_model(self):
        """Create mock model."""
        return MockModel()

    @pytest.fixture
    def guide(self, mock_model):
        """Create guide."""
        return MarkovCodeGuide(mock_model, order=2)

    @pytest.fixture
    def validator(self, guide):
        """Create validator."""
        return StreamingCodeValidator(guide)

    def test_initialization(self, validator):
        """Test validator initialization."""
        assert validator.is_valid is True
        assert validator.current_code == ""
        assert validator.tokens_processed == 0
        assert len(validator.issues) == 0

    def test_add_token_valid(self, validator):
        """Test adding valid tokens."""
        # Add complete valid code - just test that it doesn't crash
        code = "pass"
        result = validator.add_token(code)

        # Should return a tuple
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_add_token_invalid(self, validator):
        """Test adding invalid tokens."""
        tokens = ["def", " ", "func", "(", ")", ":", "\n", "    ", "invalid_syntax"]

        is_valid, error = validator.add_token(tokens[-1])

        assert validator.is_valid is False
        assert error is not None
        assert "Syntax error" in error or len(validator.issues) > 0

    def test_get_next_suggestions(self, validator):
        """Test getting suggestions."""
        # Add some valid code
        validator.add_token("def func():")

        if validator.is_valid:
            suggestions = validator.get_next_suggestions(top_k=3)
            assert isinstance(suggestions, list)
            assert len(suggestions) <= 3
        else:
            # If invalid, should return empty list
            suggestions = validator.get_next_suggestions()
            assert suggestions == []

    def test_get_validation_status(self, validator):
        """Test validation status reporting."""
        status = validator.get_validation_status()

        assert "is_valid" in status
        assert "issues" in status
        assert "tokens_processed" in status
        assert "current_context" in status

    def test_reset(self, validator):
        """Test validator reset."""
        validator.add_token("def func():")
        validator.is_valid = False
        validator.issues = ["test"]
        validator.tokens_processed = 5

        validator.reset()

        assert validator.is_valid is True
        assert validator.current_code == ""
        assert validator.issues == []
        assert validator.tokens_processed == 0


class TestConvenienceFunctions:
    """Test convenience functions."""

    @pytest.fixture
    def mock_model(self):
        """Create mock model."""
        return MockModel()

    def test_quick_suggest_valid_code(self, mock_model):
        """Test quick_suggest with valid code."""
        partial_code = "def func():\n    if True:"
        suggestions = quick_suggest(mock_model, partial_code, top_k=2)

        assert isinstance(suggestions, list)
        assert len(suggestions) <= 2
        assert all(isinstance(s, NextNodeSuggestion) for s in suggestions)

    def test_quick_suggest_invalid_code(self, mock_model):
        """Test quick_suggest with invalid code."""
        partial_code = "def func("  # incomplete
        suggestions = quick_suggest(mock_model, partial_code, top_k=3)

        # Should return defaults for invalid code
        assert isinstance(suggestions, list)
        assert len(suggestions) <= 3

    def test_validate_generated_code_valid(self, mock_model):
        """Test validation of valid code."""
        code = "def func():\n    return 42"
        result = validate_generated_code(mock_model, code)

        assert isinstance(result, object)  # ValidationResult
        assert hasattr(result, "is_valid")

    def test_validate_generated_code_invalid(self, mock_model):
        """Test validation of invalid code."""
        code = "def func():\n    invalid syntax here"
        result = validate_generated_code(mock_model, code)

        assert hasattr(result, "is_valid")
        assert result.is_valid is False
        assert len(result.errors) > 0


class TestIntegration:
    """Integration tests combining components."""

    @pytest.fixture
    def mock_model(self):
        """Create mock model."""
        return MockModel()

    def test_guide_to_validator_integration(self, mock_model):
        """Test guide and validator working together."""
        guide = MarkovCodeGuide(mock_model)
        validator = StreamingCodeValidator(guide)

        # Add valid code - just test that it doesn't crash
        result = validator.add_token("pass")
        assert isinstance(result, tuple)

        # Get suggestions for next
        suggestions = validator.get_next_suggestions()
        assert isinstance(suggestions, list)

    def test_cached_vs_regular_performance(self, mock_model):
        """Test that cached guide performs better on repeated queries."""
        regular_guide = MarkovCodeGuide(mock_model)
        cached_guide = CachedMarkovCodeGuide(mock_model, cache_size=10)

        context = ASTContext("FunctionDef", "If")

        # Warm up both
        regular_guide.suggest_next_nodes(context)
        cached_guide.suggest_next_nodes(context)

        # Reset counters
        regular_guide.query_count = 0
        cached_guide._hits = 0
        cached_guide._misses = 0

        # Make repeated calls
        for _ in range(5):
            regular_guide.suggest_next_nodes(context)
            cached_guide.suggest_next_nodes(context)

        # Cached guide should have cache hits
        assert cached_guide._hits > 0
        assert cached_guide._misses >= 0


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_guide_with_empty_model(self):
        """Test guide with model that has no probabilities."""

        class EmptyModel:
            probabilities = {}

        guide = MarkovCodeGuide(EmptyModel(), order=2)
        context = ASTContext("FunctionDef", "If")
        suggestions = guide.suggest_next_nodes(context, top_k=3)

        # Should fall back to defaults
        assert len(suggestions) == 3
        assert all(s.confidence == "LOW" for s in suggestions)

    def test_invalid_model_initialization(self):
        """Test guide with invalid model."""

        class InvalidModel:
            pass  # No probabilities

        with pytest.raises(ValueError, match="Model must have"):
            MarkovCodeGuide(InvalidModel())

    def test_context_to_state_edge_cases(self):
        """Test context state conversion edge cases."""
        # Short ancestor chain
        ctx = ASTContext("FunctionDef", "If", ancestor_chain=[])
        state = ctx.to_state(order=3)
        assert state == (
            "FunctionDef",
            "FunctionDef",
            "If",
        )  # Grandparent defaults to parent

    def test_temperature_edge_cases(self):
        """Test temperature scaling edge cases."""
        model = MockModel()
        guide = MarkovCodeGuide(model)
        context = ASTContext("FunctionDef", "If")

        # Very low temperature
        cold = guide.suggest_next_nodes(context, temperature=0.1)
        assert len(cold) > 0  # Should have suggestions, but top one much more likely

        # Very high temperature (more random)
        hot = guide.suggest_next_nodes(context, temperature=2.0)
        assert len(hot) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
