#!/usr/bin/env python3
"""
AST Markov Chain Trainer for Python Code Patterns
Ingests Python code and outputs transition probabilities between AST node types.
"""

import ast
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import sys


class ASTMarkovTrainer:
    """Trains a Markov chain model on Python AST transition patterns."""

    def __init__(self, order: int = 2):
        """
        Initialize AST Markov trainer.

        Args:
            order: Markov chain order (1=bigram, 2=trigram, 3=higher). Default 2 for better context.

        Raises:
            ValueError: If order not in [1, 2, 3]
        """
        if order not in [1, 2, 3]:
            raise ValueError(f"Order must be 1, 2, or 3, got {order}")

        self.order = order
        self.transitions: Dict[Tuple, Counter] = defaultdict(Counter)
        self.files_processed = 0
        self.files_failed = 0

    def extract_ast_sequence(
        self, node: ast.AST, parent_type: str = "start"
    ) -> List[Tuple[str, str]]:
        """
        Extract sequence of (parent_context, node_type) pairs from AST via DFS.

        Args:
            node: AST node to process
            parent_type: Type name of parent node (for context)

        Returns:
            List of (parent_type, node_type) tuples representing traversal
        """
        sequence = []
        node_type = type(node).__name__

        # Record this node with its parent context
        sequence.append((parent_type, node_type))

        # Recursively process children in order
        for child in ast.iter_child_nodes(node):
            sequence.extend(self.extract_ast_sequence(child, node_type))

        return sequence

    def train_on_code(self, code: str) -> bool:
        """
        Parse Python code and update transition counts.

        Args:
            code: Python source code string

        Returns:
            True if successful, False if parsing failed
        """
        try:
            tree = ast.parse(code)
            sequence = self.extract_ast_sequence(tree, "start")

            # Build n-grams based on order
            if self.order == 1:
                # Bigram: (parent, node) → next_node_type
                for i in range(len(sequence) - 1):
                    current_state = sequence[i]  # (parent_type, node_type) tuple
                    next_node_type = sequence[i + 1][1]  # Just the node type of next
                    self.transitions[current_state][next_node_type] += 1

            elif self.order == 2:
                # Trigram: ((p1,n1), (p2,n2)) → next_node_type
                for i in range(1, len(sequence) - 1):
                    # Use previous two (parent, node) pairs as context
                    context = (sequence[i - 1], sequence[i])
                    next_node_type = sequence[i + 1][1]
                    self.transitions[context][next_node_type] += 1

            elif self.order == 3:
                # Higher-order: use last 3 nodes
                for i in range(2, len(sequence) - 1):
                    context = (sequence[i - 2], sequence[i - 1], sequence[i])
                    next_node_type = sequence[i + 1][1]
                    self.transitions[context][next_node_type] += 1

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
        print(f"  Unique states: {len(self.transitions)}")
        print(f"  Total transitions: {sum(len(v) for v in self.transitions.values())}")

    def get_probabilities(self, min_count: int = 5) -> Dict:
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
                node: count / total for node, count in filtered_counts.items()
            }

        return probabilities

    def export_to_python(self, output_path: Path, min_count: int = 5) -> None:
        """
        Export the trained model as executable Python code.

        Args:
            output_path: Where to save the Python file
            min_count: Minimum occurrence count to include a transition
        """
        with output_path.open("w", encoding="utf-8") as f:
            f.write('"""Auto-generated Markov chain model for Python AST patterns"""\n')
            f.write("from collections import Counter\n\n")

            # Write raw transition counts
            f.write("# Raw transition counts\n")
            f.write("transitions = {\n")

            for state, next_counts in sorted(self.transitions.items()):
                # Filter rare transitions
                filtered = {k: v for k, v in next_counts.items() if v >= min_count}
                if not filtered:
                    continue

                # Format state key based on order
                state_str = self._format_state_key(state)

                # Format counter
                counter_items = ", ".join(
                    f"'{k}': {v}" for k, v in sorted(filtered.items())
                )
                f.write(f"    {state_str}: Counter({{{counter_items}}}),\n")

            f.write("}\n\n")

            # Write probabilities
            probabilities = self.get_probabilities(min_count)
            f.write("# Transition probabilities\n")
            f.write("probabilities = {\n")

            for state, probs in sorted(probabilities.items()):
                state_str = self._format_state_key(state)

                prob_items = ", ".join(
                    f"'{k}': {v:.4f}"
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
            f.write(f"UNIQUE_STATES = {len(probabilities)}\n")
            f.write(f"MIN_COUNT_THRESHOLD = {min_count}\n")

        print(f"\nModel exported to {output_path}")
        print(f"  States with transitions: {len(probabilities)}")
        print(f"  Total transitions: {sum(len(v) for v in probabilities.values())}")

    def export_to_json(self, output_path: Path, min_count: int = 5) -> None:
        """
        Export the trained model as JSON.

        Args:
            output_path: Where to save the JSON file
            min_count: Minimum occurrence count to include a transition
        """
        probabilities = self.get_probabilities(min_count)

        # Convert tuple keys to strings for JSON serialization
        json_data = {
            "markov_order": self.order,
            "files_processed": self.files_processed,
            "files_failed": self.files_failed,
            "min_count_threshold": min_count,
            "unique_states": len(probabilities),
            "transitions": {
                str(state): probs for state, probs in probabilities.items()
            },
        }

        with output_path.open("w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=2)

        print(f"Model exported to {output_path}")
        print(f"  States: {len(probabilities)}")
        print(f"  File size: {output_path.stat().st_size / 1024:.1f} KB")

    def _format_state_key(self, state: Tuple) -> str:
        """Format a state tuple as a Python expression."""
        if self.order == 1:
            # Single (parent, node) tuple
            parent, node = state
            return f"('{parent}', '{node}')"
        else:
            # Multiple (parent, node) tuples
            parts = ", ".join(f"('{parent}', '{node}')" for parent, node in state)
            return f"({parts})"

    def _get_helper_functions(self) -> str:
        """Get helper function definitions for the exported model."""
        return '''
def get_next_node_probabilities(state):
    """
    Get probability distribution for next AST node type given current state.
    
    Args:
        state: Tuple representing current state context
    
    Returns:
        Dictionary mapping node types to probabilities, or None if state unknown
    """
    return probabilities.get(state)


def get_top_k_next_nodes(state, k=5):
    """
    Get top-k most likely next AST node types.
    
    Args:
        state: Tuple representing current state context
        k: Number of top predictions to return
    
    Returns:
        List of (node_type, probability) tuples, sorted by probability descending
    """
    probs = get_next_node_probabilities(state)
    if probs is None:
        return []
    
    return sorted(probs.items(), key=lambda x: x[1], reverse=True)[:k]
'''


def main():
    """CLI interface for training the Markov model."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Train a Markov chain model on Python AST patterns"
    )
    parser.add_argument(
        "input_path", type=Path, help="Path to Python file or directory to train on"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("ast_markov_model.py"),
        help="Output path for the trained model (default: ast_markov_model.py)",
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
        default=5,
        help="Minimum occurrence count to include transition (default: 5)",
    )
    parser.add_argument(
        "--no-recursive",
        action="store_true",
        help="Do not recursively search directories",
    )

    args = parser.parse_args()

    # Initialize trainer
    trainer = ASTMarkovTrainer(order=args.order)

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

    # Export model
    if args.format == "python":
        trainer.export_to_python(args.output, min_count=args.min_count)
    else:
        trainer.export_to_json(args.output, min_count=args.min_count)

    print(f"\n✅ Training complete. Model saved to {args.output}")


if __name__ == "__main__":
    main()
