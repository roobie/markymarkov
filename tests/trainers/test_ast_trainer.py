"""
Comprehensive tests for ASTMarkovTrainer
"""

import pytest
import ast
from pathlib import Path
from collections import Counter
from src.trainers.ast_trainer import ASTMarkovTrainer
import tempfile
import sys


class TestASTMarkovTrainerInit:
    """Test initialization and configuration."""

    def test_init_default_order(self):
        """Test default order is 2 (trigram)."""
        trainer = ASTMarkovTrainer()
        assert trainer.order == 2

    def test_init_order_1(self):
        """Test order 1 (bigram) initialization."""
        trainer = ASTMarkovTrainer(order=1)
        assert trainer.order == 1

    def test_init_order_2(self):
        """Test order 2 (trigram) initialization."""
        trainer = ASTMarkovTrainer(order=2)
        assert trainer.order == 2

    def test_init_order_3(self):
        """Test order 3 initialization."""
        trainer = ASTMarkovTrainer(order=3)
        assert trainer.order == 3

    def test_init_invalid_order(self):
        """Test that invalid order raises ValueError."""
        with pytest.raises(ValueError):
            ASTMarkovTrainer(order=4)

        with pytest.raises(ValueError):
            ASTMarkovTrainer(order=0)

    def test_init_counters(self):
        """Test that counters are initialized."""
        trainer = ASTMarkovTrainer()
        assert trainer.transitions == {}
        assert trainer.files_processed == 0
        assert trainer.files_failed == 0


class TestASTSequenceExtraction:
    """Test AST sequence extraction."""

    def test_extract_simple_function(self):
        """Test extraction from simple function definition."""
        code = "def foo(): pass"
        tree = ast.parse(code)
        trainer = ASTMarkovTrainer()

        sequence = trainer.extract_ast_sequence(tree, "start")

        # Should have Module, FunctionDef, Pass nodes
        assert len(sequence) > 0
        assert sequence[0] == ("start", "Module")
        # Should contain FunctionDef
        node_types = [t[1] for t in sequence]
        assert "FunctionDef" in node_types

    def test_extract_sequence_with_parent_tracking(self):
        """Test that parent context is properly tracked."""
        code = "def foo(): return 42"
        tree = ast.parse(code)
        trainer = ASTMarkovTrainer()

        sequence = trainer.extract_ast_sequence(tree, "start")

        # Check parent context is maintained
        assert sequence[0] == ("start", "Module")

        # FunctionDef should come from Module
        func_pairs = [s for s in sequence if s[1] == "FunctionDef"]
        assert len(func_pairs) > 0
        assert func_pairs[0][0] == "Module"

    def test_extract_nested_structure(self):
        """Test extraction from nested AST structure."""
        code = """
def foo(x):
    if x > 0:
        return x
    else:
        return -x
"""
        tree = ast.parse(code)
        trainer = ASTMarkovTrainer()

        sequence = trainer.extract_ast_sequence(tree)

        # Should have If, Compare, Return, etc.
        node_types = [t[1] for t in sequence]
        assert "If" in node_types
        assert "Return" in node_types
        assert "Compare" in node_types

    def test_extract_empty_module(self):
        """Test extraction from empty module."""
        code = ""
        tree = ast.parse(code)
        trainer = ASTMarkovTrainer()

        sequence = trainer.extract_ast_sequence(tree)

        # Should at least have Module
        assert len(sequence) >= 1
        assert sequence[0][1] == "Module"


class TestTrainOnCode:
    """Test code training."""

    def test_train_on_simple_code(self):
        """Test training on simple Python code."""
        trainer = ASTMarkovTrainer(order=1)
        code = "x = 1"

        success = trainer.train_on_code(code)

        assert success is True
        assert len(trainer.transitions) > 0

    def test_train_on_multiple_calls(self):
        """Test that multiple training calls accumulate."""
        trainer = ASTMarkovTrainer(order=1)
        code1 = "x = 1"
        code2 = "y = 2"

        success1 = trainer.train_on_code(code1)
        success2 = trainer.train_on_code(code2)

        assert success1 is True
        assert success2 is True
        assert len(trainer.transitions) > 0

    def test_train_on_invalid_syntax(self):
        """Test that invalid syntax returns False."""
        trainer = ASTMarkovTrainer()
        code = "def foo(: pass"  # Invalid syntax

        success = trainer.train_on_code(code)

        assert success is False

    def test_train_updates_transitions_order_1(self):
        """Test that training updates transitions dict (bigram)."""
        trainer = ASTMarkovTrainer(order=1)
        code = "def foo(): pass"

        initial_count = len(trainer.transitions)
        trainer.train_on_code(code)

        assert len(trainer.transitions) > initial_count

    def test_train_updates_transitions_order_2(self):
        """Test that training updates transitions dict (trigram)."""
        trainer = ASTMarkovTrainer(order=2)
        code = "def foo(): pass"

        initial_count = len(trainer.transitions)
        trainer.train_on_code(code)

        assert len(trainer.transitions) > initial_count

    def test_train_counter_increment(self):
        """Test that transitions counter increments properly."""
        trainer = ASTMarkovTrainer(order=1)
        code = "x = 1"

        trainer.train_on_code(code)

        # Each transition should be counted at least once
        for state, counter in trainer.transitions.items():
            for node_type, count in counter.items():
                assert count >= 1

    def test_train_on_function_with_loop(self):
        """Test training on code with loops."""
        trainer = ASTMarkovTrainer(order=1)
        code = """
for i in range(10):
    print(i)
"""
        success = trainer.train_on_code(code)

        assert success is True
        # Should have For, Call nodes
        node_types = set()
        for state, counter in trainer.transitions.items():
            node_types.update(counter.keys())
        assert "For" in node_types

    def test_train_on_function_with_if(self):
        """Test training on code with conditionals."""
        trainer = ASTMarkovTrainer(order=1)
        code = """
if x > 0:
    y = x
else:
    y = -x
"""
        success = trainer.train_on_code(code)

        assert success is True


class TestProbabilityComputation:
    """Test probability computation."""

    def test_get_probabilities_filters_rare(self):
        """Test that rare transitions are filtered."""
        trainer = ASTMarkovTrainer(order=1)

        # Manually set up transitions
        state = ("Module", "FunctionDef")
        trainer.transitions[state][("FunctionDef", "Return")] = 100
        trainer.transitions[state][("FunctionDef", "Expr")] = 2  # Rare

        probs = trainer.get_probabilities(min_count=5)

        # Rare transition should be filtered
        if state in probs:
            assert ("FunctionDef", "Return") in probs[state]
            assert ("FunctionDef", "Expr") not in probs[state]

    def test_get_probabilities_sums_to_one(self):
        """Test that probabilities sum to approximately 1.0."""
        trainer = ASTMarkovTrainer(order=1)

        # Set up transitions
        state = ("Module", "FunctionDef")
        trainer.transitions[state]["Return"] = 100
        trainer.transitions[state]["Expr"] = 50
        trainer.transitions[state]["Assign"] = 50

        probs = trainer.get_probabilities(min_count=1)

        # Probabilities should sum to 1.0
        total = sum(probs[state].values())
        assert abs(total - 1.0) < 0.001

    def test_get_probabilities_correct_values(self):
        """Test that probability values are correct."""
        trainer = ASTMarkovTrainer(order=1)

        state = ("Module", "FunctionDef")
        trainer.transitions[state]["Return"] = 60
        trainer.transitions[state]["Expr"] = 40

        probs = trainer.get_probabilities(min_count=1)

        assert probs[state]["Return"] == pytest.approx(0.6, abs=0.001)
        assert probs[state]["Expr"] == pytest.approx(0.4, abs=0.001)

    def test_get_probabilities_empty_result(self):
        """Test that all rare transitions returns empty."""
        trainer = ASTMarkovTrainer(order=1)

        state = ("Module", "FunctionDef")
        trainer.transitions[state]["Return"] = 2
        trainer.transitions[state]["Expr"] = 1

        probs = trainer.get_probabilities(min_count=10)

        # All transitions filtered, state should not be in result
        assert state not in probs


class TestFileTraining:
    """Test training on files."""

    def test_train_on_file_success(self):
        """Test successful file training."""
        trainer = ASTMarkovTrainer()

        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            f.write("x = 1\ny = 2")
            temp_path = Path(f.name)

        try:
            success = trainer.train_on_file(temp_path)
            assert success is True
            assert trainer.files_processed == 1
            assert trainer.files_failed == 0
        finally:
            temp_path.unlink()

    def test_train_on_file_invalid_syntax(self):
        """Test file training with invalid syntax."""
        trainer = ASTMarkovTrainer()

        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            f.write("def foo(: pass")  # Invalid
            temp_path = Path(f.name)

        try:
            success = trainer.train_on_file(temp_path)
            assert success is False
            assert trainer.files_processed == 0
            assert trainer.files_failed == 1
        finally:
            temp_path.unlink()

    def test_train_on_nonexistent_file(self):
        """Test training on nonexistent file."""
        trainer = ASTMarkovTrainer()

        success = trainer.train_on_file(Path("/nonexistent/file.py"))

        assert success is False
        assert trainer.files_failed == 1


class TestDirectoryTraining:
    """Test training on directories."""

    def test_train_on_directory(self):
        """Test training on directory with multiple files."""
        trainer = ASTMarkovTrainer()

        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)

            # Create test files
            (tmppath / "file1.py").write_text("x = 1")
            (tmppath / "file2.py").write_text("y = 2")

            trainer.train_on_directory(tmppath, recursive=False)

            assert trainer.files_processed == 2
            assert trainer.files_failed == 0

    def test_train_on_directory_recursive(self):
        """Test recursive directory training."""
        trainer = ASTMarkovTrainer()

        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)

            # Create nested structure
            (tmppath / "file1.py").write_text("x = 1")
            subdir = tmppath / "subdir"
            subdir.mkdir()
            (subdir / "file2.py").write_text("y = 2")

            trainer.train_on_directory(tmppath, recursive=True)

            assert trainer.files_processed == 2

    def test_train_on_directory_non_recursive(self):
        """Test non-recursive directory training."""
        trainer = ASTMarkovTrainer()

        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)

            # Create nested structure
            (tmppath / "file1.py").write_text("x = 1")
            subdir = tmppath / "subdir"
            subdir.mkdir()
            (subdir / "file2.py").write_text("y = 2")

            trainer.train_on_directory(tmppath, recursive=False)

            # Should only process top-level file
            assert trainer.files_processed == 1


class TestExportPython:
    """Test Python export."""

    def test_export_creates_file(self):
        """Test that export creates output file."""
        trainer = ASTMarkovTrainer()
        trainer.train_on_code("x = 1")

        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            output_path = Path(f.name)

        try:
            trainer.export_to_python(output_path)
            assert output_path.exists()
            assert output_path.stat().st_size > 0
        finally:
            output_path.unlink()

    def test_export_valid_python(self):
        """Test that exported model is valid Python."""
        trainer = ASTMarkovTrainer()
        trainer.train_on_code("x = 1")

        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            output_path = Path(f.name)

        try:
            trainer.export_to_python(output_path)

            # Try to import the model
            import importlib.util

            spec = importlib.util.spec_from_file_location("model", output_path)
            model = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(model)

            # Check it has required attributes
            assert hasattr(model, "transitions")
            assert hasattr(model, "probabilities")
            assert hasattr(model, "MARKOV_ORDER")
            assert hasattr(model, "FILES_PROCESSED")
        finally:
            output_path.unlink()

    def test_export_has_helper_functions(self):
        """Test that exported model has helper functions."""
        trainer = ASTMarkovTrainer()
        trainer.train_on_code("x = 1")

        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            output_path = Path(f.name)

        try:
            trainer.export_to_python(output_path)

            import importlib.util

            spec = importlib.util.spec_from_file_location("model", output_path)
            model = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(model)

            assert hasattr(model, "get_next_node_probabilities")
            assert hasattr(model, "get_top_k_next_nodes")
            assert callable(model.get_next_node_probabilities)
            assert callable(model.get_top_k_next_nodes)
        finally:
            output_path.unlink()


class TestExportJSON:
    """Test JSON export."""

    def test_export_json_creates_file(self):
        """Test that JSON export creates file."""
        trainer = ASTMarkovTrainer()
        trainer.train_on_code("x = 1")

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            output_path = Path(f.name)

        try:
            trainer.export_to_json(output_path)
            assert output_path.exists()
        finally:
            output_path.unlink()

    def test_export_json_valid(self):
        """Test that JSON export is valid JSON."""
        trainer = ASTMarkovTrainer()
        trainer.train_on_code("x = 1")

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            output_path = Path(f.name)

        try:
            trainer.export_to_json(output_path)

            import json

            with open(output_path) as f:
                data = json.load(f)

            assert "markov_order" in data
            assert "files_processed" in data
            assert "transitions" in data
        finally:
            output_path.unlink()


class TestFormatStateKey:
    """Test state key formatting."""

    def test_format_state_key_order_1(self):
        """Test formatting for order 1."""
        trainer = ASTMarkovTrainer(order=1)
        state = ("Module", "FunctionDef")

        result = trainer._format_state_key(state)

        assert result == "('Module', 'FunctionDef')"

    def test_format_state_key_order_2(self):
        """Test formatting for order 2."""
        trainer = ASTMarkovTrainer(order=2)
        state = (("Module", "FunctionDef"), ("FunctionDef", "Return"))

        result = trainer._format_state_key(state)

        assert "('Module', 'FunctionDef')" in result
        assert "('FunctionDef', 'Return')" in result


class TestIntegration:
    """Integration tests."""

    def test_full_training_pipeline(self):
        """Test complete training pipeline."""
        trainer = ASTMarkovTrainer(order=2)

        # Train on some code
        code1 = "def foo(x): return x + 1"
        code2 = "def bar(y): return y * 2"

        trainer.train_on_code(code1)
        trainer.train_on_code(code2)

        # Export
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            output_path = Path(f.name)

        try:
            trainer.export_to_python(output_path)

            # Import and use
            import importlib.util

            spec = importlib.util.spec_from_file_location("model", output_path)
            model = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(model)

            # Test helper functions
            if model.probabilities:
                state = list(model.probabilities.keys())[0]
                probs = model.get_next_node_probabilities(state)
                assert probs is not None

                top_k = model.get_top_k_next_nodes(state, k=3)
                assert isinstance(top_k, list)
        finally:
            output_path.unlink()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
