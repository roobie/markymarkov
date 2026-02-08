#!/usr/bin/env python3
"""
Marky - Markov Chain Guidance System for LLM Code Generation

Command-line interface for training and querying Markov models for code guidance.

Usage:
    python -m src train <code_path> <output_dir> [--model-type {ast,semantic,both}]
    python -m src query <model_path> <code_context> [--top-k 5] [--temperature 1.0]
    python -m src validate <model_path> <code_file>
    python -m src stats <model_path>
    python -m src demo

Examples:
    # Train AST model on a Python file
    python -m src train my_code.py ./models --model-type ast

    # Query model for next node suggestions
    python -m src query ./models/ast_model.py "def func():\n    if x > 0:"

    # Validate code against model
    python -m src validate ./models/ast_model.py code_to_validate.py

    # Show model statistics
    python -m src stats ./models/ast_model.py

    # Run interactive demo
    python -m src demo
"""

import argparse
import sys
import os
import glob
from pathlib import Path
from typing import List, Optional, Dict, Any
import ast
import importlib.util

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from .trainers.ast_trainer import ASTMarkovTrainer
from .trainers.semantic_pattern_extractor import SemanticPatternAnalyzer, extract_patterns_from_code
from .trainers.semantic_trainer import SemanticMarkovTrainer
from .guides.ast_code_guide import MarkovCodeGuide, CachedMarkovCodeGuide
from .interfaces.model_types import ASTContext


class MarkyCLI:
    """Command-line interface for the Marky system."""

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="Marky - Markov Chain Guidance System for LLM Code Generation",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=__doc__
        )
        self.subparsers = self.parser.add_subparsers(dest='command', help='Available commands')

        self._setup_train_parser()
        self._setup_query_parser()
        self._setup_validate_parser()
        self._setup_stats_parser()
        self._setup_demo_parser()

    def _setup_train_parser(self):
        """Setup train command parser."""
        parser = self.subparsers.add_parser('train', help='Train Markov models from code')
        parser.add_argument('code_path', help='Path to Python code file or directory')
        parser.add_argument('output_dir', help='Directory to save trained models')
        parser.add_argument(
            '--model-type',
            choices=['ast', 'semantic', 'both'],
            default='both',
            help='Type of model to train (default: both)'
        )
        parser.add_argument(
            '--order',
            type=int,
            default=2,
            choices=[1, 2, 3],
            help='Markov chain order (default: 2)'
        )

    def _setup_query_parser(self):
        """Setup query command parser."""
        parser = self.subparsers.add_parser('query', help='Query model for suggestions')
        parser.add_argument('model_path', help='Path to trained model file')
        parser.add_argument('code_context', help='Partial code context for suggestions')
        parser.add_argument('--top-k', type=int, default=5, help='Number of suggestions to return')
        parser.add_argument('--temperature', type=float, default=1.0, help='Sampling temperature')
        parser.add_argument('--min-confidence', choices=['LOW', 'MEDIUM', 'HIGH'], default='MEDIUM',
                          help='Minimum confidence level')

    def _setup_validate_parser(self):
        """Setup validate command parser."""
        parser = self.subparsers.add_parser('validate', help='Validate code against model')
        parser.add_argument('model_path', help='Path to trained model file')
        parser.add_argument('code_file', help='Python code file to validate')

    def _setup_stats_parser(self):
        """Setup stats command parser."""
        parser = self.subparsers.add_parser('stats', help='Show model statistics')
        parser.add_argument('model_path', help='Path to trained model file')

    def _setup_demo_parser(self):
        """Setup demo command parser."""
        parser = self.subparsers.add_parser('demo', help='Run interactive demo')

    def run(self):
        """Run the CLI."""
        args = self.parser.parse_args()

        if not args.command:
            self.parser.print_help()
            return

        try:
            if args.command == 'train':
                self._train(args)
            elif args.command == 'query':
                self._query(args)
            elif args.command == 'validate':
                self._validate(args)
            elif args.command == 'stats':
                self._stats(args)
            elif args.command == 'demo':
                self._demo()
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    def _find_python_files(self, path: str) -> List[str]:
        """Find all Python files in path."""
        if os.path.isfile(path):
            if path.endswith('.py'):
                return [path]
            else:
                raise ValueError(f"Not a Python file: {path}")

        if os.path.isdir(path):
            pattern = os.path.join(path, '**', '*.py')
            return glob.glob(pattern, recursive=True)

        raise ValueError(f"Path does not exist: {path}")

    def _train(self, args):
        """Train models from code."""
        print(f"Training {args.model_type} model(s) from: {args.code_path}")
        print(f"Output directory: {args.output_dir}")
        print(f"Markov order: {args.order}")
        print()

        # Find Python files
        python_files = self._find_python_files(args.code_path)
        if not python_files:
            print("No Python files found!")
            return

        print(f"Found {len(python_files)} Python files")
        print()

        # Create output directory
        os.makedirs(args.output_dir, exist_ok=True)

        # Train AST model if requested
        if args.model_type in ['ast', 'both']:
            print("Training AST model...")
            ast_trainer = ASTMarkovTrainer(order=args.order)

            for file_path in python_files:
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        code = f.read()
                    ast_trainer.train_on_code(code)
                    print(f"✓ Processed: {file_path}")
                except Exception as e:
                    print(f"✗ Failed: {file_path} - {e}")

            # Export AST model
            ast_model_path = os.path.join(args.output_dir, 'ast_model.py')
            ast_trainer.export_to_python(Path(ast_model_path))
            print(f"✓ AST model saved to: {ast_model_path}")
            print(f"  States: {len(ast_trainer.get_model().probabilities)}")
            print()

        # Train semantic model if requested
        if args.model_type in ['semantic', 'both']:
            print("Training semantic model...")
            semantic_trainer = SemanticMarkovTrainer(order=args.order)

            for file_path in python_files:
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        code = f.read()
                    semantic_trainer.train_on_code(code)
                    print(f"✓ Processed: {file_path}")
                except Exception as e:
                    print(f"✗ Failed: {file_path} - {e}")

            # Export semantic model
            semantic_model_path = os.path.join(args.output_dir, 'semantic_model.py')
            semantic_trainer.export_to_python(Path(semantic_model_path))
            print(f"✓ Semantic model saved to: {semantic_model_path}")
            print(f"  States: {len(semantic_trainer.get_model().probabilities)}")
            print()

        print("Training complete! 🎉")

    def _load_model(self, model_path: str):
        """Load a model module dynamically."""
        spec = importlib.util.spec_from_file_location("model", model_path)
        if spec is None or spec.loader is None:
            raise ValueError(f"Could not load model from: {model_path}")

        model_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(model_module)
        return model_module

    def _query(self, args):
        """Query model for suggestions."""
        print(f"Loading model: {args.model_path}")

        # Load model
        model_module = self._load_model(args.model_path)

        # Create guide
        guide = CachedMarkovCodeGuide(model_module, cache_size=1000)

        print(f"Querying with context: {repr(args.code_context[:50])}...")
        print()

        # Parse context to get AST state
        try:
            context = self._extract_context_from_code(args.code_context)
            print(f"Extracted context: {context}")
            print()
        except Exception as e:
            print(f"Could not parse context: {e}")
            print("Trying with simple context...")
            context = ASTContext('Module', 'Expr')  # Fallback

        # Get suggestions
        suggestions = guide.suggest_next_nodes(
            context=context,
            top_k=args.top_k,
            temperature=args.temperature,
            min_confidence=args.min_confidence
        )

        print("Suggestions:")
        for i, s in enumerate(suggestions, 1):
            print(f"{i}. {s.node_type} (prob: {s.probability:.3f}, conf: {s.confidence})")

        print()
        print(f"Cache stats: {guide.get_cache_stats()}")

    def _extract_context_from_code(self, code: str) -> ASTContext:
        """Extract AST context from partial code."""
        try:
            tree = ast.parse(code)
            # Find the last meaningful node
            last_node = None
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.If, ast.For, ast.While)):
                    last_node = node
                elif isinstance(node, (ast.Return, ast.Assign, ast.Expr)):
                    last_node = node

            if last_node:
                parent_type = type(tree.body[0]).__name__ if tree.body else 'Module'
                current_type = type(last_node).__name__
                return ASTContext(parent_type, current_type)
            else:
                return ASTContext('Module', 'Expr')
        except:
            return ASTContext('Module', 'Expr')

    def _validate(self, args):
        """Validate code against model."""
        print(f"Loading model: {args.model_path}")
        print(f"Validating code: {args.code_file}")
        print()

        # Load code
        with open(args.code_file, 'r', encoding='utf-8') as f:
            code = f.read()

        # Load model
        model_module = self._load_model(args.model_path)

        # Create guide
        guide = MarkovCodeGuide(model_module)

        # Extract AST sequence
        try:
            tree = ast.parse(code)
            sequence = []
            for node in ast.walk(tree):
                if hasattr(node, '__class__'):
                    sequence.append(node.__class__.__name__)

            if sequence:
                result = guide.validate_sequence(sequence[:10])  # First 10 nodes
                print("Validation Result:")
                print(f"  Valid: {result.is_valid}")
                print(f"  Confidence: {result.confidence_score:.3f}")
                if result.errors:
                    print(f"  Issues: {len(result.errors)}")
                    for error in result.errors[:3]:  # Show first 3
                        print(f"    - {error}")
            else:
                print("Could not extract AST sequence from code")

        except Exception as e:
            print(f"Validation failed: {e}")

    def _stats(self, args):
        """Show model statistics."""
        print(f"Loading model: {args.model_path}")

        # Load model
        model_module = self._load_model(args.model_path)

        # Create guide
        guide = MarkovCodeGuide(model_module)

        # Get statistics
        stats = guide.get_statistics()

        print("\nModel Statistics:")
        print(f"  States: {stats.get('num_states', 'N/A')}")
        print(f"  Total transitions: {stats.get('total_transitions', 'N/A')}")
        print(f"  Average transitions per state: {stats.get('avg_transitions', 'N/A')}")
        print(f"  Model type: {getattr(model_module, '__model_type__', 'Unknown')}")

        # Show sample states
        if hasattr(model_module, 'probabilities'):
            print(f"\nSample states ({min(5, len(model_module.probabilities))} of {len(model_module.probabilities)}):")
            for i, (state, probs) in enumerate(list(model_module.probabilities.items())[:5]):
                top_prob = max(probs.items(), key=lambda x: x[1])
                print(f"  {state} → {top_prob[0]} ({top_prob[1]:.3f})")

    def _demo(self):
        """Run interactive demo."""
        print("🎉 Welcome to Marky - Markov Chain Code Guidance Demo!")
        print("=" * 60)
        print()

        # Create a simple demo model
        print("Creating demo AST model...")
        trainer = ASTMarkovTrainer(order=2)

        # Train on some example code
        demo_code = """
def hello_world():
    print("Hello, World!")

def calculate_sum(a, b):
    if a is None or b is None:
        return 0
    result = a + b
    return result

class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, x):
        self.value += x
        return self.value

if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(5))
"""

        trainer.train_on_code(demo_code)
        print("✓ Demo model trained")
        print()

        # Create guide - need to create a mock model module
        import types
        
        # Create a mock model module with probabilities
        mock_model = types.ModuleType('mock_model')
        mock_model.probabilities = trainer.get_probabilities()
        mock_model.order = 2
        
        guide = CachedMarkovCodeGuide(mock_model, cache_size=100)

        # Demo queries
        demo_contexts = [
            ("FunctionDef", "If", "Simple function with if statement"),
            ("FunctionDef", "Return", "Function ending with return"),
            ("ClassDef", "FunctionDef", "Method inside class"),
        ]

        print("🚀 Demo Queries:")
        print("-" * 30)

        for parent, current, description in demo_contexts:
            context = ASTContext(parent, current)
            suggestions = guide.suggest_next_nodes(context, top_k=3)

            print(f"\nContext: {description}")
            print(f"AST State: {parent} → {current}")
            print("Suggestions:")
            for s in suggestions:
                print(f"  • {s.node_type} (prob: {s.probability:.3f}, conf: {s.confidence})")

        print()
        print("Cache performance:", guide.get_cache_stats())
        print()
        print("🎯 Demo complete! Try training your own models with 'python -m src train <code> <output>'")


def main():
    """Main entry point."""
    cli = MarkyCLI()
    cli.run()


if __name__ == '__main__':
    main()