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
import json
import numpy as np

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from .trainers.ast_trainer import ASTMarkovTrainer
from .trainers.semantic_pattern_extractor import (
    SemanticPatternAnalyzer,
    extract_patterns_from_code,
)
from .trainers.semantic_trainer import SemanticMarkovTrainer
from .guides.ast_code_guide import MarkovCodeGuide, CachedMarkovCodeGuide
from .interfaces.model_types import ASTContext

# API wrappers
from .api.style import get_style_guidance_from_file, get_style_guidance_from_text
from .api.validate import validate_code


class MarkyCLI:
    """Command-line interface for the Marky system."""

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="Marky - Markov Chain Guidance System for LLM Code Generation",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=__doc__,
        )
        self.subparsers = self.parser.add_subparsers(
            dest="command", help="Available commands"
        )

        self._setup_train_parser()
        self._setup_query_parser()
        self._setup_validate_parser()
        self._setup_stats_parser()
        self._setup_demo_parser()
        # New commands
        self._setup_style_parser()
        self._setup_validate_code_parser()

    def _setup_train_parser(self):
        """Setup train command parser."""
        parser = self.subparsers.add_parser(
            "train", help="Train Markov models from code"
        )
        parser.add_argument("code_path", help="Path to Python code file or directory")
        parser.add_argument("output_dir", help="Directory to save trained models")
        parser.add_argument(
            "--model-type",
            choices=["ast", "semantic", "both"],
            default="both",
            help="Type of model to train (default: both)",
        )
        parser.add_argument(
            "--order",
            type=int,
            default=2,
            choices=[1, 2, 3],
            help="Markov chain order (default: 2)",
        )

    def _setup_query_parser(self):
        """Setup query command parser."""
        parser = self.subparsers.add_parser("query", help="Query model for suggestions")
        parser.add_argument("model_path", help="Path to trained model file")
        parser.add_argument("code_context", help="Partial code context for suggestions")
        parser.add_argument(
            "--top-k", type=int, default=5, help="Number of suggestions to return"
        )
        parser.add_argument(
            "--temperature", type=float, default=1.0, help="Sampling temperature"
        )
        parser.add_argument(
            "--min-confidence",
            choices=["LOW", "MEDIUM", "HIGH"],
            default="MEDIUM",
            help="Minimum confidence level",
        )

    def _setup_validate_parser(self):
        """Setup validate command parser."""
        parser = self.subparsers.add_parser(
            "validate", help="Validate code against model"
        )
        parser.add_argument("model_path", help="Path to trained model file")
        parser.add_argument("code_file", help="Python code file to validate")

    def _setup_stats_parser(self):
        """Setup stats command parser."""
        parser = self.subparsers.add_parser("stats", help="Show model statistics")
        parser.add_argument("model_path", help="Path to trained model file")

    def _setup_demo_parser(self):
        """Setup demo command parser."""
        parser = self.subparsers.add_parser("demo", help="Run interactive demo")

    def _setup_style_parser(self):
        """Setup get_style_guidance parser."""
        parser = self.subparsers.add_parser(
            "get_style_guidance", help="Return a style briefing for a file or text"
        )
        parser.add_argument("file_path", nargs="?", help="Path to file to analyze")
        parser.add_argument("--desc", "--description", dest="description", help="Short description of what's being written", default=None)
        parser.add_argument("--engine", dest="engine", default="heuristics", help="Engine to use: heuristics or markov")
        parser.add_argument("--model", dest="model_path", default=None, help="Optional model path to augment guidance")
        parser.add_argument("--json", action="store_true", dest="json", help="Output JSON")

    def _setup_validate_code_parser(self):
        """Setup validate_code parser."""
        parser = self.subparsers.add_parser(
            "validate_code", help="Validate code (syntax-only or model-based)"
        )
        group = parser.add_mutually_exclusive_group(required=False)
        group.add_argument("--file", dest="file", help="Path to code file")
        group.add_argument("--code", dest="code", help="Code text literal")
        parser.add_argument("--model", dest="model_path", help="Optional model path for model-based validation")
        parser.add_argument("--language", dest="language", default="python", help="Language hint (default: python)")
        parser.add_argument("--json", action="store_true", dest="json", help="Output JSON")

    def run(self):
        """Run the CLI."""
        args = self.parser.parse_args()

        if not args.command:
            self.parser.print_help()
            return

        try:
            if args.command == "train":
                self._train(args)
            elif args.command == "query":
                self._query(args)
            elif args.command == "validate":
                self._validate(args)
            elif args.command == "stats":
                self._stats(args)
            elif args.command == "demo":
                self._demo()
            elif args.command == "get_style_guidance":
                self._get_style_guidance_cmd(args)
            elif args.command == "validate_code":
                self._validate_code_cmd(args)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    def _find_python_files(self, path: str) -> List[str]:
        """Find all Python files in path."""
        if os.path.isfile(path):
            if path.endswith(".py"):
                return [path]
            else:
                raise ValueError(f"Not a Python file: {path}")

        if os.path.isdir(path):
            pattern = os.path.join(path, "**", "*.py")
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
        if args.model_type in ["ast", "both"]:
            print("Training AST model...")
            ast_trainer = ASTMarkovTrainer(order=args.order)

            for file_path in python_files:
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        code = f.read()
                    ast_trainer.train_on_code(code)
                    print(f"✓ Processed: {file_path}")
                except Exception as e:
                    print(f"✗ Failed: {file_path} - {e}")

            # Export AST model
            ast_model_path = os.path.join(args.output_dir, "ast_model.py")
            ast_trainer.export_to_python(Path(ast_model_path))
            print(f"✓ AST model saved to: {ast_model_path}")
            print()

        # Train semantic model if requested
        if args.model_type in ["semantic", "both"]:
            print("Training semantic model...")
            semantic_trainer = SemanticMarkovTrainer(order=args.order)

            for file_path in python_files:
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        code = f.read()
                    semantic_trainer.train_on_code(code)
                    print(f"✓ Processed: {file_path}")
                except Exception as e:
                    print(f"✗ Failed: {file_path} - {e}")

            # Export semantic model
            semantic_model_path = os.path.join(args.output_dir, "semantic_model.py")
            semantic_trainer.export_to_python(Path(semantic_model_path))
            print(f"✓ Semantic model saved to: {semantic_model_path}")
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
            context = ASTContext("Module", "Expr")  # Fallback

        # Get suggestions
        suggestions = guide.suggest_next_nodes(
            context=context,
            top_k=args.top_k,
            temperature=args.temperature,
            min_confidence=args.min_confidence,
        )

        print("Suggestions:")
        for i, s in enumerate(suggestions, 1):
            print(
                f"{i}. {s.node_type} (prob: {s.probability:.3f}, conf: {s.confidence})"
            )

        print()
        print(f"Cache stats: {guide.get_cache_stats()}")

    def _extract_context_from_code(self, code: str) -> ASTContext:
        """Extract AST context from partial code."""
        try:
            tree = ast.parse(code)
            # Find the last meaningful node
            last_node = None
            for node in ast.walk(tree):
                if isinstance(
                    node, (ast.FunctionDef, ast.ClassDef, ast.If, ast.For, ast.While)
                ):
                    last_node = node
                elif isinstance(node, (ast.Return, ast.Assign, ast.Expr)):
                    last_node = node

            if last_node:
                parent_type = type(tree.body[0]).__name__ if tree.body else "Module"
                current_type = type(last_node).__name__
                return ASTContext(parent_type, current_type)
            else:
                return ASTContext("Module", "Expr")
        except:
            return ASTContext("Module", "Expr")

    def _validate(self, args):
        """Validate code against model."""
        print(f"Loading model: {args.model_path}")
        print(f"Validating code: {args.code_file}")
        print()

        # Load code
        with open(args.code_file, "r", encoding="utf-8") as f:
            code = f.read()

        # Load model
        model_module = self._load_model(args.model_path)

        # Determine if this is a semantic or AST model
        is_semantic = hasattr(model_module, "CodePattern") and hasattr(
            model_module, "probabilities"
        )

        if is_semantic:
            self._validate_semantic(args, model_module, code)
        else:
            self._validate_ast(args, model_module, code)

    def _validate_ast(self, args, model_module, code):
        """Validate code against AST model."""
        try:
            tree = ast.parse(code)
            trainer = ASTMarkovTrainer(order=getattr(model_module, "MARKOV_ORDER", 2))
            sequence = trainer.extract_ast_sequence(tree, "start")

            if sequence:
                print(f"Extracted {len(sequence)} AST transitions")

                issues = []
                total_log_prob = 0.0
                transition_count = 0

                order = getattr(model_module, "MARKOV_ORDER", 2)
                print(f"Model order: {order}")

                for i in range(order, min(len(sequence), 25)):
                    context = tuple(sequence[i - order : i])
                    next_node_type = sequence[i][1]

                    if context in model_module.probabilities:
                        probs = model_module.probabilities[context]
                        if next_node_type in probs:
                            prob = probs[next_node_type]
                            total_log_prob += np.log(prob) if prob > 0 else -np.inf
                            transition_count += 1
                        else:
                            issues.append(
                                f"Unexpected transition: {context} → {next_node_type}"
                            )
                    else:
                        issues.append(f"Unknown context: {context}")

                if transition_count > 0:
                    avg_log_prob = total_log_prob / transition_count
                    confidence = min(1.0, max(0.0, np.exp(avg_log_prob)))
                else:
                    confidence = 0.0

                is_valid = confidence > 0.1 or len(issues) == 0

                print("Validation Result (AST Model):")
                print(f"  Valid: {is_valid}")
                print(f"  Confidence: {confidence:.3f}")
                print(
                    f"  Transitions checked: {max(0, min(len(sequence) - order, 25))}"
                )
                print(f"  Known transitions: {transition_count}")

                if issues:
                    print(f"  Issues: {len(issues)}")
                    for error in issues[:5]:
                        print(f"    - {error}")
                    if len(issues) > 5:
                        print(f"    ... and {len(issues) - 5} more")
            else:
                print("Could not extract AST sequence from code")

        except Exception as e:
            print(f"Validation failed: {e}")
            import traceback

            traceback.print_exc()

    def _validate_semantic(self, args, model_module, code):
        """Validate code against semantic pattern model."""
        try:
            # Import CodePattern from the MODEL, not from the source
            ModelCodePattern = model_module.CodePattern

            # Extract patterns from code using our extractor
            patterns = extract_patterns_from_code(code)

            # Build sequence with location info
            pattern_sequence = [node.pattern for node in patterns]
            pattern_locations = {i: node for i, node in enumerate(patterns)}

            # Convert our CodePattern enums to the model's CodePattern enums
            # by matching on the value string
            model_pattern_sequence = []
            for pattern in pattern_sequence:
                # Find matching pattern in model's enum
                for model_pattern in ModelCodePattern:
                    if model_pattern.value == pattern.value:
                        model_pattern_sequence.append(model_pattern)
                        break

            if model_pattern_sequence:
                print(f"Extracted {len(model_pattern_sequence)} semantic patterns")
                print(
                    f"First 20 patterns: {[p.value for p in model_pattern_sequence[:20]]}"
                )

                issues = []
                matched_sequences = []
                total_log_prob = 0.0
                transition_count = 0

                order = getattr(model_module, "MARKOV_ORDER", 2)
                print(f"Model order: {order}")
                print(f"Model has {len(model_module.probabilities)} pattern sequences")

                # For order N, we need N consecutive patterns to predict the next
                checked = 0
                for i in range(order, min(len(model_pattern_sequence), order + 15)):
                    context = tuple(model_pattern_sequence[i - order : i])
                    next_pattern = model_pattern_sequence[i]
                    checked += 1

                    context_str = " → ".join(p.value for p in context)

                    # Get location info for the next pattern
                    next_node = pattern_locations.get(i)
                    loc_info = ""
                    if next_node and next_node.lineno:
                        loc_info = f" @ line {next_node.lineno}:{next_node.col_offset}"

                    if context in model_module.probabilities:
                        probs = model_module.probabilities[context]
                        if next_pattern in probs:
                            prob = probs[next_pattern]
                            total_log_prob += np.log(prob) if prob > 0 else -np.inf
                            transition_count += 1
                            matched_sequences.append(
                                {
                                    "context": context_str,
                                    "next": next_pattern.value,
                                    "prob": prob,
                                    "location": loc_info,
                                }
                            )
                        else:
                            # This transition doesn't exist in model
                            next_options = ", ".join(
                                p.value for p in list(probs.keys())[:3]
                            )
                            issues.append(
                                {
                                    "type": "unexpected",
                                    "context": context_str,
                                    "next": next_pattern.value,
                                    "options": next_options,
                                    "location": loc_info,
                                }
                            )
                    else:
                        # Context not in model
                        issues.append(
                            {
                                "type": "unknown_context",
                                "context": context_str,
                                "location": loc_info,
                            }
                        )

                if transition_count > 0:
                    avg_log_prob = total_log_prob / transition_count
                    confidence = min(1.0, max(0.0, np.exp(avg_log_prob)))
                else:
                    confidence = 0.0

                # Semantic validation - if ANY patterns match, it's somewhat valid
                is_valid = transition_count > 0

                print("\nValidation Result (Semantic Model):")
                print(f"  Valid: {is_valid}")
                print(f"  Confidence: {confidence:.3f}")
                print(f"  Pattern sequences checked: {checked}")
                print(f"  Known transitions: {transition_count}/{checked}")

                if matched_sequences:
                    print(f"\n  ✓ Matching sequences ({len(matched_sequences)}):")
                    for i, seq in enumerate(matched_sequences[:7], 1):
                        print(
                            f"    {i}. {seq['context']} → {seq['next']} ({seq['prob']:.3f}){seq['location']}"
                        )

                if issues:
                    print(f"\n  ✗ Non-matching sequences ({len(issues)}):")
                    for i, issue in enumerate(issues[:5], 1):
                        if issue["type"] == "unknown_context":
                            print(
                                f"    {i}. Unknown sequence: {issue['context']}{issue['location']}"
                            )
                        else:
                            print(
                                f"    {i}. {issue['context']} → {issue['next']}{issue['location']}"
                            )
                            print(f"       Expected one of: {issue['options']}")

                    if len(issues) > 5:
                        print(f"    ... and {len(issues) - 5} more")

                # Summary statistics
                print(f"\n  Summary:")
                print(
                    f"    Unique patterns found: {len(set(p.value for p in model_pattern_sequence))}"
                )
                print(
                    f"    Coverage: {transition_count}/{checked} transitions ({100 * transition_count / max(1, checked):.1f}%)"
                )
                if issues:
                    print(
                        f"    Issues: {len([i for i in issues if i['type'] == 'unexpected'])} unexpected, {len([i for i in issues if i['type'] == 'unknown_context'])} unknown context"
                    )
            else:
                print(
                    "Could not extract semantic patterns from code (no patterns detected)"
                )

        except Exception as e:
            print(f"Semantic validation failed: {e}")
            import traceback

            traceback.print_exc()

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
        if hasattr(model_module, "probabilities"):
            print(
                f"\nSample states ({min(5, len(model_module.probabilities))} of {len(model_module.probabilities)}):"
            )
            for i, (state, probs) in enumerate(
                list(model_module.probabilities.items())[:5]
            ):
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
        mock_model = types.ModuleType("mock_model")
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
                print(
                    f"  • {s.node_type} (prob: {s.probability:.3f}, conf: {s.confidence})"
                )

        print()
        print("Cache performance:", guide.get_cache_stats())
        print()
        print(
            "🎯 Demo complete! Try training your own models with 'python -m src train <code> <output>'"
        )

    def _get_style_guidance_cmd(self, args):
        """Handler for get_style_guidance CLI command."""
        if not getattr(args, "file_path", None):
            print("Error: file_path is required unless you provide text via the API.")
            return

        try:
            result = get_style_guidance_from_file(args.file_path, description=getattr(args, "description", None), engine=getattr(args, "engine", "heuristics"), model_path=getattr(args, "model_path", None))
            if getattr(args, "json", False):
                print(json.dumps(result, indent=2))
            else:
                print(result.get("briefing", "No briefing available"))
                sections = result.get("sections")
                if sections:
                    print("\nSections:")
                    for k, v in sections.items():
                        print(f"- {k}: {v}")
        except Exception as e:
            print(f"Failed to get style guidance: {e}")

    def _validate_code_cmd(self, args):
        """Handler for validate_code CLI command."""
        code = getattr(args, "code", None)
        if not code and getattr(args, "file", None):
            try:
                with open(args.file, "r", encoding="utf-8") as f:
                    code = f.read()
            except Exception as e:
                print(f"Failed to read file {args.file}: {e}")
                return

        # If still no code, try to read from stdin
        if not code:
            if not sys.stdin.isatty():
                code = sys.stdin.read()

        if not code:
            print("Error: no code provided. Use --code or --file or pipe code to stdin.")
            return

        try:
            result = validate_code(code, language=getattr(args, "language", "python"), filename=getattr(args, "file", None), model_path=getattr(args, "model_path", None))
            if getattr(args, "json", False):
                print(json.dumps(result, indent=2))
            else:
                print(result.get("summary", "No summary"))
                diags = result.get("diagnostics", [])
                if diags:
                    print("\nDiagnostics:")
                    for d in diags:
                        rng = d.get("range", {})
                        start = rng.get("start", {})
                        line = start.get("line", "?")
                        ch = start.get("character", "?")
                        print(f"- [{d.get('severity')}] line {line}:{ch} {d.get('message')}")
                if "confidence" in result:
                    print(f"\nConfidence: {result.get('confidence')}")
        except Exception as e:
            print(f"Validation failed: {e}")
            import traceback

            traceback.print_exc()


def main():
    """Main entry point."""
    cli = MarkyCLI()
    cli.run()


if __name__ == "__main__":
    main()
