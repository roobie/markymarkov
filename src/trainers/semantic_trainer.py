#!/usr/bin/env python3
"""
Semantic Markov Chain Trainer for Python Code Patterns
Trains on high-level semantic patterns extracted from Python code.
"""

import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import sys

from .semantic_pattern_extractor import (
    CodePattern,
    SemanticPatternAnalyzer,
    extract_patterns_from_code,
    extract_patterns_from_file,
)


class SemanticMarkovTrainer:
    """Trains a Markov chain model on semantic pattern sequences."""

    def __init__(self, order: int = 2):
        """
        Initialize Semantic Markov trainer.

        Args:
            order: Markov chain order (1=bigram, 2=trigram, 3=higher). Default 2.

        Raises:
            ValueError: If order not in [1, 2, 3]
        """
        if order not in [1, 2, 3]:
            raise ValueError(f"Order must be 1, 2, or 3, got {order}")

        self.order = order
        self.transitions: Dict[Tuple, Counter] = defaultdict(Counter)
        self.files_processed = 0
        self.files_failed = 0
        self.pattern_counts: Counter = Counter()

    def train_on_code(self, code: str) -> bool:
        """
        Parse Python code and train on semantic pattern sequences.

        Args:
            code: Python source code string

        Returns:
            True if successful, False if parsing failed
        """
        try:
            # Extract patterns
            patterns = extract_patterns_from_code(code)
            pattern_sequence = [node.pattern for node in patterns]

            # Count individual patterns
            for pattern in pattern_sequence:
                self.pattern_counts[pattern] += 1

            # Build n-grams based on order
            if self.order == 1:
                # Bigram: pattern → next_pattern
                for i in range(len(pattern_sequence) - 1):
                    current_pattern = pattern_sequence[i]
                    next_pattern = pattern_sequence[i + 1]
                    self.transitions[(current_pattern,)][next_pattern] += 1

            elif self.order == 2:
                # Trigram: (pattern1, pattern2) → next_pattern
                for i in range(1, len(pattern_sequence) - 1):
                    context = (pattern_sequence[i - 1], pattern_sequence[i])
                    next_pattern = pattern_sequence[i + 1]
                    self.transitions[context][next_pattern] += 1

            elif self.order == 3:
                # Higher-order: use last 3 patterns
                for i in range(2, len(pattern_sequence) - 1):
                    context = (
                        pattern_sequence[i - 2],
                        pattern_sequence[i - 1],
                        pattern_sequence[i],
                    )
                    next_pattern = pattern_sequence[i + 1]
                    self.transitions[context][next_pattern] += 1

            return True

        except SyntaxError:
            return False
        except Exception as e:
            print(f"Warning: Error processing code: {e}", file=sys.stderr)
            return False

    def train_on_file(self, filepath: Path) -> bool:
        """
        Train on a single Python file.

        Args:
            filepath: Path to Python file

        Returns:
            True if successful, False otherwise
        """
        try:
            success = extract_patterns_from_file(filepath) is not None
            if success:
                code = filepath.read_text(encoding="utf-8")
                success = self.train_on_code(code)

            if success:
                self.files_processed += 1
            else:
                self.files_failed += 1
            return success
        except Exception as e:
            print(f"Warning: Could not read {filepath}: {e}", file=sys.stderr)
            self.files_failed += 1
            return False

    def train_on_directory(self, directory: Path, recursive: bool = True) -> None:
        """
        Train on all Python files in a directory.

        Args:
            directory: Path to directory containing Python files
            recursive: If True, search recursively; otherwise only in directory
        """
        pattern = "**/*.py" if recursive else "*.py"
        python_files = list(directory.glob(pattern))

        print(f"Found {len(python_files)} Python files in {directory}")

        for i, filepath in enumerate(python_files, 1):
            if i % 100 == 0:
                print(f"Processing file {i}/{len(python_files)}...", file=sys.stderr)
            self.train_on_file(filepath)

        print(f"\nTraining complete!")
        print(f"  Successfully processed: {self.files_processed}")
        print(f"  Failed to process: {self.files_failed}")
        print(f"  Unique pattern sequences: {len(self.transitions)}")
        print(f"  Total transitions: {sum(len(v) for v in self.transitions.values())}")

    def get_probabilities(self, min_count: int = 3) -> Dict:
        """
        Convert raw counts to probabilities, filtering rare transitions.

        Args:
            min_count: Minimum occurrence count to include a transition

        Returns:
            Dictionary mapping states to probability distributions
        """
        probabilities = {}

        for state, next_counts in self.transitions.items():
            # Filter out rare transitions
            filtered_counts = {k: v for k, v in next_counts.items() if v >= min_count}

            if not filtered_counts:
                continue

            total = sum(filtered_counts.values())
            probabilities[state] = {
                pattern: count / total for pattern, count in filtered_counts.items()
            }

        return probabilities

    def export_to_python(self, output_path: Path, min_count: int = 3) -> None:
        """
        Export the trained model as executable Python code.

        Args:
            output_path: Where to save the Python file
            min_count: Minimum occurrence count to include a transition
        """
        with output_path.open("w", encoding="utf-8") as f:
            f.write('"""Auto-generated Semantic Markov model for code patterns"""\n')
            f.write("from collections import Counter\n")
            f.write("from enum import Enum\n\n")

            # Write CodePattern enum
            f.write("class CodePattern(Enum):\n")
            f.write('    """High-level semantic patterns."""\n')
            for pattern in CodePattern:
                f.write(f'    {pattern.name} = "{pattern.value}"\n')
            f.write("\n\n")

            # Write raw transition counts
            f.write("# Pattern transition counts\n")
            f.write("transitions = {\n")

            for state, next_counts in self.transitions.items():
                # Filter rare transitions
                filtered = {k: v for k, v in next_counts.items() if v >= min_count}
                if not filtered:
                    continue

                # Format state
                state_str = self._format_state_key(state)

                # Format counter
                counter_items = ", ".join(
                    f"CodePattern.{k.name}: {v}"
                    for k, v in sorted(
                        filtered.items(), key=lambda x: x[1], reverse=True
                    )
                )
                f.write(f"    {state_str}: Counter({{{counter_items}}}),\n")

            f.write("}\n\n")

            # Write probabilities
            probabilities = self.get_probabilities(min_count)
            f.write("# Pattern transition probabilities\n")
            f.write("probabilities = {\n")

            for state, probs in probabilities.items():
                state_str = self._format_state_key(state)

                prob_items = ", ".join(
                    f"CodePattern.{k.name}: {v:.4f}"
                    for k, v in sorted(probs.items(), key=lambda x: x[1], reverse=True)
                )
                f.write(f"    {state_str}: {{{prob_items}}},\n")

            f.write("}\n\n")

            # Add helper functions
            f.write(self._get_helper_functions())

            # Add metadata
            f.write(f"\n# Model metadata\n")
            f.write(f"MARKOV_ORDER = {self.order}\n")
            f.write(f"FILES_PROCESSED = {self.files_processed}\n")
            f.write(f"UNIQUE_SEQUENCES = {len(probabilities)}\n")
            f.write(f"MIN_COUNT_THRESHOLD = {min_count}\n")
            f.write(f"TOTAL_PATTERNS_TRAINED = {sum(self.pattern_counts.values())}\n")

        print(f"\nModel exported to {output_path}")
        print(f"  Pattern sequences: {len(probabilities)}")
        print(f"  Pattern types used: {len(self.pattern_counts)}")

    def export_to_json(self, output_path: Path, min_count: int = 3) -> None:
        """
        Export the trained model as JSON.

        Args:
            output_path: Where to save the JSON file
            min_count: Minimum occurrence count to include a transition
        """
        probabilities = self.get_probabilities(min_count)

        # Convert enum keys to strings for JSON serialization
        json_data = {
            "markov_order": self.order,
            "files_processed": self.files_processed,
            "files_failed": self.files_failed,
            "min_count_threshold": min_count,
            "unique_sequences": len(probabilities),
            "transitions": {
                str(state): {k.value: v for k, v in probs.items()}
                for state, probs in probabilities.items()
            },
            "pattern_statistics": {
                pattern.value: count
                for pattern, count in self.pattern_counts.most_common()
            },
        }

        with output_path.open("w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=2)

        print(f"Model exported to {output_path}")
        print(f"  Sequences: {len(probabilities)}")
        print(f"  File size: {output_path.stat().st_size / 1024:.1f} KB")

    def _format_state_key(self, state: Tuple) -> str:
        """Format a state tuple as a Python expression."""
        if self.order == 1:
            # Single pattern
            pattern = state[0]
            return f"(CodePattern.{pattern.name},)"
        else:
            # Multiple patterns
            parts = ", ".join(f"CodePattern.{p.name}" for p in state)
            return f"({parts})"

    def _get_helper_functions(self) -> str:
        """Get helper function definitions for the exported model."""
        return '''
def get_next_pattern_probabilities(pattern_sequence):
    """
    Get probability distribution for next semantic pattern.
    
    Args:
        pattern_sequence: Tuple of CodePattern enums representing current context
    
    Returns:
        Dictionary mapping CodePattern to probabilities, or None if state unknown
    """
    return probabilities.get(pattern_sequence)


def get_top_k_patterns(pattern_sequence, k=5):
    """
    Get top-k most likely next patterns.
    
    Args:
        pattern_sequence: Tuple of CodePattern enums representing current context
        k: Number of top predictions to return
    
    Returns:
        List of (CodePattern, probability) tuples, sorted by probability descending
    """
    probs = get_next_pattern_probabilities(pattern_sequence)
    if probs is None:
        return []
    
    return sorted(probs.items(), key=lambda x: x[1], reverse=True)[:k]


def suggest_next_patterns(current_patterns, k=5):
    """
    Convenience function: given recent patterns, suggest what comes next.
    
    Args:
        current_patterns: List of recent CodePattern enums
        k: Number of suggestions
    
    Returns:
        List of (CodePattern, probability) tuples
    """
    if not current_patterns:
        return []
    
    # Try with full context
    if len(current_patterns) >= MARKOV_ORDER:
        context = tuple(current_patterns[-MARKOV_ORDER:])
    else:
        context = tuple(current_patterns)
    
    suggestions = get_top_k_patterns(context, k)
    
    # If no suggestions, try with shorter context
    if not suggestions and len(current_patterns) > 1:
        context = (current_patterns[-1],)
        suggestions = get_top_k_patterns(context, k)
    
    return suggestions
'''

    def print_statistics(self) -> None:
        """Print interesting statistics about learned patterns."""
        print("\n=== Semantic Pattern Statistics ===")

        print("\nMost common patterns:")
        for pattern, count in self.pattern_counts.most_common(15):
            print(f"  {pattern.value}: {count}")

        # Most common transitions
        print("\nMost common pattern sequences:")
        all_transitions = []
        for state, next_counts in self.transitions.items():
            for next_pattern, count in next_counts.items():
                all_transitions.append((state, next_pattern, count))

        all_transitions.sort(key=lambda x: x[2], reverse=True)

        for state, next_pattern, count in all_transitions[:15]:
            state_str = " → ".join(p.value for p in state)
            print(f"  {state_str} → {next_pattern.value}: {count}")


def main():
    """CLI interface for training the semantic Markov model."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Train a semantic Markov model on code patterns"
    )
    parser.add_argument(
        "input_path", type=Path, help="Path to Python file or directory to train on"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("semantic_markov_model.py"),
        help="Output path for the trained model (default: semantic_markov_model.py)",
    )
    parser.add_argument(
        "--format",
        choices=["python", "json"],
        default="python",
        help="Output format (default: python)",
    )
    parser.add_argument(
        "--order",
        type=int,
        default=2,
        choices=[1, 2, 3],
        help="Markov chain order: 1=bigram, 2=trigram, 3=higher (default: 2)",
    )
    parser.add_argument(
        "--min-count",
        type=int,
        default=3,
        help="Minimum occurrence count to include transition (default: 3)",
    )
    parser.add_argument(
        "--no-recursive",
        action="store_true",
        help="Do not recursively search directories",
    )
    parser.add_argument(
        "--stats", action="store_true", help="Print pattern statistics after training"
    )

    args = parser.parse_args()

    # Initialize trainer
    trainer = SemanticMarkovTrainer(order=args.order)

    # Train on input
    input_path = args.input_path
    if not input_path.exists():
        print(f"Error: {input_path} does not exist", file=sys.stderr)
        sys.exit(1)

    if input_path.is_file():
        print(f"Training on single file: {input_path}")
        trainer.train_on_file(input_path)
    elif input_path.is_dir():
        print(f"Training on directory: {input_path}")
        trainer.train_on_directory(input_path, recursive=not args.no_recursive)
    else:
        print(f"Error: {input_path} is neither a file nor directory", file=sys.stderr)
        sys.exit(1)

    # Print statistics if requested
    if args.stats:
        trainer.print_statistics()

    # Export model
    if args.format == "python":
        trainer.export_to_python(args.output, min_count=args.min_count)
    else:
        trainer.export_to_json(args.output, min_count=args.min_count)

    print(f"\n✅ Training complete. Model saved to {args.output}")


if __name__ == "__main__":
    main()
