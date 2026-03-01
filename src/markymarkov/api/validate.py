"""Validation API wrapper for Marky.

Provides:
- validate_code(code, language='python', filename=None, model_path=None, validators=None)
- run(inputs)  # MCP handler compatible

This module maps existing Markov validation logic into structured diagnostics.
"""
from typing import Optional, Dict, Any, List, Union
import ast
import importlib.util
import math

from ..trainers.ast_trainer import ASTMarkovTrainer
from ..trainers.semantic_pattern_extractor import extract_patterns_from_code


def _syntax_diagnostic_from_exception(exc: SyntaxError) -> Dict[str, Any]:
    # SyntaxError has attributes: lineno, offset, msg, text
    start = {"line": exc.lineno or 1, "character": (exc.offset - 1) if exc.offset else 0}
    # End - try to put end at same line after offset
    end = {"line": exc.lineno or 1, "character": (exc.offset) if exc.offset else 0}
    return {
        "range": {"start": start, "end": end},
        "severity": 1,
        "source": "parser",
        "code": "SyntaxError",
        "message": str(exc),
    }


def validate_code(code: str, language: Optional[str] = "python", filename: Optional[str] = None, model_path: Optional[str] = None, validators: Optional[List[str]] = None) -> Dict[str, Any]:
    """Validate code and return diagnostics and summary.

    If model_path is provided and points to a Markov model, perform model-based validation.
    Otherwise, do syntax-only validation for Python using ast.parse.
    """
    diagnostics: List[Dict[str, Any]] = []
    summary = ""
    confidence: Optional[float] = None

    # Syntax-only validation for Python
    if (not model_path) and (language == "python"):
        try:
            ast.parse(code)
            diagnostics = []
            summary = "No syntax errors detected"
            return {"diagnostics": diagnostics, "summary": summary}
        except SyntaxError as e:
            diag = _syntax_diagnostic_from_exception(e)
            diagnostics = [diag]
            summary = "Syntax error detected"
            return {"diagnostics": diagnostics, "summary": summary}

    # If a model is provided, try to load it and use model-based validation
    if model_path:
        spec = importlib.util.spec_from_file_location("model", model_path)
        if spec and spec.loader:
            model_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(model_module)

            # Determine model type heuristic
            is_semantic = hasattr(model_module, "CodePattern") and hasattr(model_module, "probabilities")

            if not is_semantic:
                # AST model path
                try:
                    tree = ast.parse(code)
                    trainer = ASTMarkovTrainer(order=getattr(model_module, "MARKOV_ORDER", 2))
                    sequence = trainer.extract_ast_sequence(tree, "start")

                    issues = []
                    total_log_prob = 0.0
                    transition_count = 0

                    order = getattr(model_module, "MARKOV_ORDER", 2)

                    for i in range(order, min(len(sequence), 100)):
                        context = tuple(sequence[i - order : i])
                        next_node_type = sequence[i][1]

                        if context in model_module.probabilities:
                            probs = model_module.probabilities[context]
                            if next_node_type in probs:
                                prob = probs[next_node_type]
                                if prob > 0:
                                    total_log_prob += math.log(prob)
                                    transition_count += 1
                            else:
                                # Unexpected transition
                                issues.append((i, context, next_node_type))
                        else:
                            issues.append((i, context, next_node_type))

                    if transition_count > 0:
                        avg_log_prob = total_log_prob / transition_count
                        confidence = min(1.0, max(0.0, math.exp(avg_log_prob)))
                    else:
                        confidence = 0.0

                    # Map issues to diagnostics (best-effort)
                    for idx, context, next_node in issues:
                        # We don't have exact lineno for AST node types here; use best-effort message
                        diagnostics.append({
                            "range": {"start": {"line": 1, "character": 0}, "end": {"line": 1, "character": 0}},
                            "severity": 2,
                            "source": "markov_ast_model",
                            "code": "unexpected_transition",
                            "message": f"Unexpected transition at seq index {idx}: {context} -> {next_node}",
                        })

                    summary = f"Model-based validation completed. Issues: {len(issues)}; confidence: {confidence:.3f}"
                    return {"diagnostics": diagnostics, "summary": summary, "confidence": confidence}
                except SyntaxError as e:
                    return {"diagnostics": [_syntax_diagnostic_from_exception(e)], "summary": "Syntax error before model-based validation"}
                except Exception as e:
                    return {"diagnostics": [{"range": {"start": {"line": 1, "character": 0}, "end": {"line": 1, "character": 0}}, "severity": 3, "source": "markov", "code": "error", "message": str(e)}], "summary": "Model validation failed"}
            else:
                # Semantic model
                try:
                    patterns = extract_patterns_from_code(code)
                    pattern_sequence = [node.pattern for node in patterns]
                    pattern_locations = {i: node for i, node in enumerate(patterns)}

                    issues = []
                    matched_sequences = []
                    total_log_prob = 0.0
                    transition_count = 0

                    order = getattr(model_module, "MARKOV_ORDER", 2)

                    for i in range(order, min(len(pattern_sequence), order + 100)):
                        context = tuple(pattern_sequence[i - order : i])
                        next_pattern = pattern_sequence[i]

                        if context in model_module.probabilities:
                            probs = model_module.probabilities[context]
                            if next_pattern in probs:
                                prob = probs[next_pattern]
                                if prob > 0:
                                    total_log_prob += math.log(prob)
                                    transition_count += 1
                                    matched_sequences.append((i, context, next_pattern, prob))
                            else:
                                issues.append((i, context, next_pattern))
                        else:
                            issues.append((i, context, next_pattern))

                    if transition_count > 0:
                        avg_log_prob = total_log_prob / transition_count
                        confidence = min(1.0, max(0.0, math.exp(avg_log_prob)))
                    else:
                        confidence = 0.0

                    for idx, context, next_pattern in issues:
                        node = pattern_locations.get(idx)
                        loc = None
                        if node and getattr(node, "lineno", None):
                            loc = {"line": node.lineno, "character": getattr(node, "col_offset", 0)}
                        else:
                            loc = {"line": 1, "character": 0}

                        diagnostics.append({
                            "range": {"start": loc, "end": loc},
                            "severity": 2,
                            "source": "markov_semantic_model",
                            "code": "unexpected_pattern",
                            "message": f"Unexpected semantic pattern at index {idx}: {context} -> {next_pattern}",
                        })

                    summary = f"Semantic model validation: {len(issues)} issues, confidence: {confidence:.3f}"
                    return {"diagnostics": diagnostics, "summary": summary, "confidence": confidence}
                except Exception as e:
                    return {"diagnostics": [{"range": {"start": {"line": 1, "character": 0}, "end": {"line": 1, "character": 0}}, "severity": 3, "source": "markov_semantic", "code": "error", "message": str(e)}], "summary": "Semantic model validation failed"}

    # Fallback
    return {"diagnostics": diagnostics, "summary": summary}


def run(inputs: Dict[str, Any]) -> Dict[str, Any]:
    """MCP handler-style entrypoint.

    Expected inputs:
      - code (string) OR filename (string)
      - language (optional)
      - model_path (optional)

    Returns:
      { diagnostics: [...], summary: str, confidence?: float }
    """
    code = inputs.get("code")
    filename = inputs.get("filename")
    language = inputs.get("language", "python")
    model_path = inputs.get("model_path")

    if filename and not code:
        with open(filename, "r", encoding="utf-8") as f:
            code = f.read()

    if not code:
        raise ValueError("Either 'code' or 'filename' must be provided")

    return validate_code(code, language=language, filename=filename, model_path=model_path, validators=inputs.get("validators"))
