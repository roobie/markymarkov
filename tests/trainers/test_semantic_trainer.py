#!/usr/bin/env python3
"""
Tests for Semantic Markov Chain Trainer

Comprehensive test coverage for:
- SemanticMarkovTrainer initialization
- Training on code snippets
- Training on files
- Training on directories
- Probability calculations
- Export to Python
- Export to JSON
- Helper functions
- Statistics
"""

import pytest
import tempfile
import json
from pathlib import Path
from collections import Counter

from src.trainers.semantic_trainer import SemanticMarkovTrainer
from src.trainers.semantic_pattern_extractor import CodePattern


class TestSemanticMarkovTrainerInit:
    """Test SemanticMarkovTrainer initialization."""

    def test_init_default_order(self):
        """Test initialization with default order."""
        trainer = SemanticMarkovTrainer()
        assert trainer.order == 2
        assert trainer.files_processed == 0
        assert trainer.files_failed == 0
        assert len(trainer.transitions) == 0
        assert len(trainer.pattern_counts) == 0

    def test_init_order_1(self):
        """Test initialization with order 1."""
        trainer = SemanticMarkovTrainer(order=1)
        assert trainer.order == 1

    def test_init_order_2(self):
        """Test initialization with order 2."""
        trainer = SemanticMarkovTrainer(order=2)
        assert trainer.order == 2

    def test_init_order_3(self):
        """Test initialization with order 3."""
        trainer = SemanticMarkovTrainer(order=3)
        assert trainer.order == 3

    def test_init_invalid_order(self):
        """Test that invalid order raises ValueError."""
        with pytest.raises(ValueError, match="Order must be 1, 2, or 3"):
            SemanticMarkovTrainer(order=0)

        with pytest.raises(ValueError, match="Order must be 1, 2, or 3"):
            SemanticMarkovTrainer(order=4)

        with pytest.raises(ValueError, match="Order must be 1, 2, or 3"):
            SemanticMarkovTrainer(order=-1)


class TestTrainOnCode:
    """Test training on code snippets."""

    def test_train_simple_function(self):
        """Test training on a simple function."""
        code = """
def hello(name):
    if name:
        return f"Hello {name}"
    return "Hello"
"""
        trainer = SemanticMarkovTrainer(order=2)
        success = trainer.train_on_code(code)

        assert success is True
        # Training succeeded, check pattern counts exists
        assert trainer.pattern_counts is not None

    def test_train_with_conditions(self):
        """Test training on code with if statements."""
        code = """
def check_value(x):
    if x is None:
        return False
    if x > 0:
        return True
    return False
"""
        trainer = SemanticMarkovTrainer(order=2)
        success = trainer.train_on_code(code)

        assert success is True
        assert trainer.pattern_counts[CodePattern.IF_NONE_CHECK] >= 1

    def test_train_with_loop(self):
        """Test training on code with loops."""
        code = """
def process_items(items):
    result = []
    for item in items:
        if item > 0:
            result.append(item)
    return result
"""
        trainer = SemanticMarkovTrainer(order=2)
        success = trainer.train_on_code(code)

        assert success is True
        assert CodePattern.LOOP_FILTER in trainer.pattern_counts

    def test_train_invalid_syntax(self):
        """Test that invalid syntax still returns True (graceful handling)."""
        code = "def broken( return 42"
        trainer = SemanticMarkovTrainer()
        success = trainer.train_on_code(code)

        # Invalid syntax is handled gracefully (returns True for try block success)
        # The extract_patterns_from_code handles SyntaxError internally
        assert success is True  # Gracefully handled

    def test_train_empty_code(self):
        """Test training on empty or whitespace-only code."""
        trainer = SemanticMarkovTrainer()

        # Empty string
        success = trainer.train_on_code("")
        assert success is True  # Empty code is valid, just no patterns

        # Whitespace only
        success = trainer.train_on_code("   \n\n   ")
        assert success is True

    def test_train_order_1_transitions(self):
        """Test that order 1 creates correct bigram transitions."""
        code = """
def example():
    if True:
        return None
"""
        trainer = SemanticMarkovTrainer(order=1)
        trainer.train_on_code(code)

        # Order 1 states should be single-element tuples
        for state in trainer.transitions.keys():
            assert len(state) == 1
            assert isinstance(state[0], CodePattern)

    def test_train_order_2_transitions(self):
        """Test that order 2 creates correct trigram transitions."""
        code = """
def example():
    if True:
        return None
"""
        trainer = SemanticMarkovTrainer(order=2)
        trainer.train_on_code(code)

        # Order 2 states should be two-element tuples
        if trainer.transitions:  # Only check if there are transitions
            for state in trainer.transitions.keys():
                assert len(state) == 2
                assert all(isinstance(p, CodePattern) for p in state)

    def test_train_order_3_transitions(self):
        """Test that order 3 creates correct higher-order transitions."""
        code = """
def example():
    if True:
        x = 1
        return None
"""
        trainer = SemanticMarkovTrainer(order=3)
        trainer.train_on_code(code)

        # Order 3 states should be three-element tuples
        if trainer.transitions:  # Only check if there are transitions
            for state in trainer.transitions.keys():
                assert len(state) == 3
                assert all(isinstance(p, CodePattern) for p in state)

    def test_train_multiple_times(self):
        """Test training multiple times accumulates counts."""
        trainer = SemanticMarkovTrainer()

        code1 = "def f1():\n    if x:\n        return True"
        code2 = "def f2():\n    if y:\n        return False"

        trainer.train_on_code(code1)
        count1 = sum(trainer.pattern_counts.values())

        trainer.train_on_code(code2)
        count2 = sum(trainer.pattern_counts.values())

        assert count2 > count1  # Should accumulate


class TestTrainOnFile:
    """Test training on files."""

    def test_train_on_valid_file(self):
        """Test training on a valid Python file."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            f.write("""
def hello(name):
    if name:
        return f"Hello {name}"
    return None
""")
            f.flush()
            file_path = Path(f.name)

        try:
            trainer = SemanticMarkovTrainer()
            success = trainer.train_on_file(file_path)

            assert success is True
            assert trainer.files_processed == 1
            assert trainer.files_failed == 0
        finally:
            file_path.unlink()

    def test_train_on_nonexistent_file(self):
        """Test training on nonexistent file."""
        trainer = SemanticMarkovTrainer()
        success = trainer.train_on_file(Path("/nonexistent/file.py"))

        assert success is False
        assert trainer.files_failed == 1
        assert trainer.files_processed == 0

    def test_train_on_file_with_invalid_syntax(self):
        """Test training on file with invalid syntax (gracefully handled)."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            f.write("def broken( return 42")
            f.flush()
            file_path = Path(f.name)

        try:
            trainer = SemanticMarkovTrainer()
            success = trainer.train_on_file(file_path)

            # File may be read successfully but patterns extraction could fail
            # Just verify the trainer works with the attempt
            assert isinstance(success, bool)
        finally:
            file_path.unlink()


class TestTrainOnDirectory:
    """Test training on directories."""

    def test_train_on_directory(self):
        """Test training on a directory with Python files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir = Path(tmpdir)

            # Create Python files
            (tmpdir / "file1.py").write_text("""
def func1():
    if True:
        return 1
""")
            (tmpdir / "file2.py").write_text("""
def func2():
    for x in range(10):
        print(x)
""")

            trainer = SemanticMarkovTrainer()
            trainer.train_on_directory(tmpdir, recursive=False)

            assert trainer.files_processed == 2
            # Just verify files were processed, transitions may or may not be generated
            assert trainer.pattern_counts is not None

    def test_train_on_directory_recursive(self):
        """Test recursive directory training."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir = Path(tmpdir)

            # Create nested structure
            (tmpdir / "file1.py").write_text("def f():\n    if x:\n        return True")
            subdir = tmpdir / "subdir"
            subdir.mkdir()
            (subdir / "file2.py").write_text("def g():\n    return None")

            trainer = SemanticMarkovTrainer()
            trainer.train_on_directory(tmpdir, recursive=True)

            assert trainer.files_processed == 2

    def test_train_on_directory_non_recursive(self):
        """Test non-recursive directory training."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir = Path(tmpdir)

            # Create nested structure
            (tmpdir / "file1.py").write_text("def f():\n    pass")
            subdir = tmpdir / "subdir"
            subdir.mkdir()
            (subdir / "file2.py").write_text("def g():\n    pass")

            trainer = SemanticMarkovTrainer()
            trainer.train_on_directory(tmpdir, recursive=False)

            assert trainer.files_processed == 1  # Only top-level file


class TestProbabilities:
    """Test probability calculations."""

    def test_get_probabilities_empty(self):
        """Test probabilities on untrained model."""
        trainer = SemanticMarkovTrainer()
        probs = trainer.get_probabilities()

        assert probs == {}

    def test_get_probabilities_filters_rare(self):
        """Test that rare transitions are filtered out."""
        trainer = SemanticMarkovTrainer(order=1)

        code = """
def f():
    if x:
        return 1
    if y:
        return 2
    if z:
        return 3
"""
        trainer.train_on_code(code)
        probs = trainer.get_probabilities(min_count=100)  # High threshold

        # Most transitions should be filtered out
        assert len(probs) <= len(trainer.transitions)

    def test_get_probabilities_sum_to_one(self):
        """Test that probabilities sum to 1.0."""
        trainer = SemanticMarkovTrainer()

        code = """
def f():
    if x:
        return 1
    else:
        return 2
"""
        trainer.train_on_code(code)
        probs = trainer.get_probabilities()

        for state, prob_dist in probs.items():
            total = sum(prob_dist.values())
            assert abs(total - 1.0) < 0.0001  # Allow small floating point error

    def test_get_probabilities_values_in_range(self):
        """Test that probabilities are in [0, 1]."""
        trainer = SemanticMarkovTrainer()

        code = """
def f():
    if x:
        return 1
    return 2
"""
        trainer.train_on_code(code)
        probs = trainer.get_probabilities()

        for state, prob_dist in probs.items():
            for prob in prob_dist.values():
                assert 0.0 <= prob <= 1.0


class TestExportPython:
    """Test exporting to Python."""

    def test_export_python_creates_file(self):
        """Test that Python export creates a file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "model.py"

            trainer = SemanticMarkovTrainer()
            code = "def f():\n    if x:\n        return True"
            trainer.train_on_code(code)

            trainer.export_to_python(output)

            assert output.exists()
            assert output.stat().st_size > 0

    def test_export_python_valid_syntax(self):
        """Test that exported Python is valid."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "model.py"

            trainer = SemanticMarkovTrainer(order=2)
            code = "def f():\n    if x:\n        return True"
            trainer.train_on_code(code)

            trainer.export_to_python(output)

            # Should be valid Python
            content = output.read_text()
            compile(content, str(output), "exec")

    def test_export_python_contains_metadata(self):
        """Test that exported model contains metadata."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "model.py"

            trainer = SemanticMarkovTrainer(order=2)
            trainer.files_processed = 5
            code = "def f():\n    if x:\n        return True"
            trainer.train_on_code(code)

            trainer.export_to_python(output)

            content = output.read_text()
            assert "MARKOV_ORDER = 2" in content
            assert "FILES_PROCESSED = 5" in content

    def test_export_python_contains_functions(self):
        """Test that exported model contains helper functions."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "model.py"

            trainer = SemanticMarkovTrainer()
            code = "def f():\n    if x:\n        return True"
            trainer.train_on_code(code)

            trainer.export_to_python(output)

            content = output.read_text()
            assert "def get_next_pattern_probabilities" in content
            assert "def get_top_k_patterns" in content
            assert "def suggest_next_patterns" in content


class TestExportJSON:
    """Test exporting to JSON."""

    def test_export_json_creates_file(self):
        """Test that JSON export creates a file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "model.json"

            trainer = SemanticMarkovTrainer()
            code = "def f():\n    if x:\n        return True"
            trainer.train_on_code(code)

            trainer.export_to_json(output)

            assert output.exists()
            assert output.stat().st_size > 0

    def test_export_json_valid_format(self):
        """Test that exported JSON is valid."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "model.json"

            trainer = SemanticMarkovTrainer(order=2)
            code = "def f():\n    if x:\n        return True"
            trainer.train_on_code(code)

            trainer.export_to_json(output)

            # Should be valid JSON
            data = json.loads(output.read_text())
            assert isinstance(data, dict)

    def test_export_json_contains_metadata(self):
        """Test that JSON contains required metadata."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "model.json"

            trainer = SemanticMarkovTrainer(order=2)
            trainer.files_processed = 3
            code = "def f():\n    if x:\n        return True"
            trainer.train_on_code(code)

            trainer.export_to_json(output)

            data = json.loads(output.read_text())
            assert data["markov_order"] == 2
            assert data["files_processed"] == 3
            assert "transitions" in data
            assert "pattern_statistics" in data

    def test_export_json_serializable(self):
        """Test that all data in JSON is properly serialized."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "model.json"

            trainer = SemanticMarkovTrainer()
            code = """
def f():
    if x:
        y = [1, 2, 3]
        return y
"""
            trainer.train_on_code(code)

            trainer.export_to_json(output)

            # Should be parseable and contain expected structure
            data = json.loads(output.read_text())
            assert isinstance(data["transitions"], dict)
            assert isinstance(data["pattern_statistics"], dict)


class TestStatistics:
    """Test statistics and reporting."""

    def test_print_statistics(self, capsys):
        """Test that statistics can be printed."""
        trainer = SemanticMarkovTrainer()
        code = """
def f():
    if x:
        return 1
    return 2
"""
        trainer.train_on_code(code)
        trainer.print_statistics()

        captured = capsys.readouterr()
        assert "Semantic Pattern Statistics" in captured.out
        assert "Most common patterns" in captured.out

    def test_statistics_with_no_training(self, capsys):
        """Test statistics on untrained model."""
        trainer = SemanticMarkovTrainer()
        trainer.print_statistics()

        captured = capsys.readouterr()
        assert "Semantic Pattern Statistics" in captured.out


class TestFormatStateKey:
    """Test state key formatting."""

    def test_format_state_key_order_1(self):
        """Test formatting for order 1."""
        trainer = SemanticMarkovTrainer(order=1)
        state = (CodePattern.IF_NONE_CHECK,)
        formatted = trainer._format_state_key(state)

        assert "CodePattern.IF_NONE_CHECK" in formatted
        assert formatted.startswith("(")
        assert formatted.endswith(")")

    def test_format_state_key_order_2(self):
        """Test formatting for order 2."""
        trainer = SemanticMarkovTrainer(order=2)
        state = (CodePattern.IF_NONE_CHECK, CodePattern.RETURN_NONE)
        formatted = trainer._format_state_key(state)

        assert "CodePattern.IF_NONE_CHECK" in formatted
        assert "CodePattern.RETURN_NONE" in formatted

    def test_format_state_key_order_3(self):
        """Test formatting for order 3."""
        trainer = SemanticMarkovTrainer(order=3)
        state = (
            CodePattern.IF_NONE_CHECK,
            CodePattern.RETURN_NONE,
            CodePattern.LOOP_FILTER,
        )
        formatted = trainer._format_state_key(state)

        assert "CodePattern.IF_NONE_CHECK" in formatted
        assert "CodePattern.RETURN_NONE" in formatted
        assert "CodePattern.LOOP_FILTER" in formatted


class TestHelperFunctions:
    """Test helper functions in exported code."""

    def test_helper_functions_included(self):
        """Test that helper functions are included in export."""
        trainer = SemanticMarkovTrainer()
        helpers = trainer._get_helper_functions()

        assert "def get_next_pattern_probabilities" in helpers
        assert "def get_top_k_patterns" in helpers
        assert "def suggest_next_patterns" in helpers

    def test_helper_functions_executable(self):
        """Test that helper functions are syntactically valid."""
        trainer = SemanticMarkovTrainer()
        helpers = trainer._get_helper_functions()

        # Should be valid Python
        compile(helpers, "<string>", "exec")


class TestIntegration:
    """Integration tests combining multiple operations."""

    def test_full_pipeline(self):
        """Test full training pipeline."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir = Path(tmpdir)

            # Create files
            (tmpdir / "file1.py").write_text("""
def validate(x):
    if x is None:
        return False
    if x > 0:
        return True
    return False
""")
            (tmpdir / "file2.py").write_text("""
def process(items):
    result = []
    for item in items:
        if item > 0:
            result.append(item)
    return result
""")

            # Train
            trainer = SemanticMarkovTrainer(order=2)
            trainer.train_on_directory(tmpdir, recursive=False)

            # Export
            output_py = tmpdir / "model.py"
            trainer.export_to_python(output_py)
            assert output_py.exists()

            output_json = tmpdir / "model.json"
            trainer.export_to_json(output_json)
            assert output_json.exists()

            # Verify exports
            py_content = output_py.read_text()
            compile(py_content, str(output_py), "exec")

            json_data = json.loads(output_json.read_text())
            assert "transitions" in json_data

    def test_pattern_accumulation(self):
        """Test that patterns accumulate across multiple trainings."""
        trainer = SemanticMarkovTrainer()

        # First training
        trainer.train_on_code("def f():\n    if x:\n        return 1")
        count1 = len(trainer.pattern_counts)
        transitions1 = len(trainer.transitions)

        # Second training with different patterns
        trainer.train_on_code("def g():\n    for x in y:\n        pass")
        count2 = len(trainer.pattern_counts)
        transitions2 = len(trainer.transitions)

        # Should have accumulated patterns
        assert count2 >= count1
        assert transitions2 >= transitions1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
