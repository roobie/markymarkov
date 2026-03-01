"""Style guidance API wrapper for Marky.

Provides:
- get_style_guidance_from_file
- get_style_guidance_from_text
- run(inputs)  # MCP handler compatible

This module uses simple heuristics and can optionally use a Markov model if model_path is provided.
"""
from typing import Optional, Dict, Any, List
import os
import ast
import re
import importlib.util

from ..guides.ast_code_guide import MarkovCodeGuide, CachedMarkovCodeGuide
from ..trainers.ast_trainer import ASTMarkovTrainer


def _detect_language_from_path(path: str) -> str:
    if path.endswith(".py"):
        return "python"
    if path.endswith(".js") or path.endswith(".ts"):
        return "javascript"
    return "unknown"


def _basic_python_style_checks(source: str) -> Dict[str, str]:
    sections: Dict[str, str] = {}

    # Docstring check (module-level)
    try:
        tree = ast.parse(source)
        doc = ast.get_docstring(tree)
        sections["docstring"] = (
            "present" if doc and doc.strip() else "missing"
        )
    except Exception:
        sections["docstring"] = "unknown"

    # Naming heuristics: look for function and variable names
    func_names = [f.name for f in ast.walk(ast.parse(source)) if isinstance(f, ast.FunctionDef)] if source.strip() else []
    if func_names:
        snake = sum(1 for n in func_names if re.match(r"^[a-z_][a-z0-9_]*$", n))
        camel = len(func_names) - snake
        if snake >= camel:
            sections["naming"] = "predominantly snake_case"
        else:
            sections["naming"] = "some camelCase detected"
    else:
        sections["naming"] = "no top-level functions found"

    # TODOs and FIXMEs
    todos = re.findall(r"#\s*(TODO|FIXME)[:\s]?(.*)", source, flags=re.IGNORECASE)
    sections["todos"] = f"{len(todos)} TODO/FIXME comments"

    # Long lines
    long_lines = [i + 1 for i, l in enumerate(source.splitlines()) if len(l) > 120]
    sections["long_lines"] = f"{len(long_lines)} lines > 120 chars"

    # Imports grouping heuristic
    imports = [l for l in source.splitlines() if l.strip().startswith("import") or l.strip().startswith("from")]
    sections["imports"] = f"{len(imports)} import lines"

    return sections


def get_style_guidance_from_text(text: str, description: Optional[str] = None, engine: str = "heuristics", model_path: Optional[str] = None) -> Dict[str, Any]:
    """Analyze text and return a style briefing and structured sections.

    engine: 'heuristics' or 'markov'. If 'markov' and model_path provided, try to use model to augment guidance.
    """
    lang = "python"  # for now, heuristics target python
    sections: Dict[str, str] = {}

    # Basic heuristics
    if lang == "python":
        sections = _basic_python_style_checks(text)

    briefing_lines: List[str] = []
    if description:
        briefing_lines.append(f"Context: {description}")

    briefing_lines.append("Style briefing (summary):")
    briefing_lines.append(f"- Detected language: {lang}")
    briefing_lines.append(f"- Docstring: {sections.get('docstring')}")
    briefing_lines.append(f"- Naming: {sections.get('naming')}")
    briefing_lines.append(f"- Imports: {sections.get('imports')}")
    briefing_lines.append(f"- TODOs: {sections.get('todos')}")
    briefing_lines.append(f"- Long lines: {sections.get('long_lines')}")

    # Model-augmented guidance (optional)
    if engine == "markov" and model_path:
        try:
            spec = importlib.util.spec_from_file_location("model", model_path)
            if spec and spec.loader:
                model = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(model)
                # Use MarkovCodeGuide to sample common transitions if available
                guide = CachedMarkovCodeGuide(model, cache_size=500)
                # Try to inspect top suggestions for a generic "pattern" summary
                suggestions = guide.suggest_top_k_examples(top_k=5) if hasattr(guide, "suggest_top_k_examples") else None
                if suggestions:
                    briefing_lines.append("- Model observations:")
                    for s in suggestions:
                        briefing_lines.append(f"  • {s}")
        except Exception:
            briefing_lines.append("- (Could not load model for augmented guidance)")

    briefing = "\n".join(briefing_lines)

    return {"briefing": briefing, "sections": sections}


def get_style_guidance_from_file(file_path: str, description: Optional[str] = None, engine: str = "heuristics", model_path: Optional[str] = None) -> Dict[str, Any]:
    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    return get_style_guidance_from_text(text, description=description, engine=engine, model_path=model_path)


def run(inputs: Dict[str, Any]) -> Dict[str, Any]:
    """MCP handler-style entrypoint.

    Expected inputs:
      - file_path (required) OR text (optional)
      - description (optional)
      - engine (optional)
      - model_path (optional)

    Returns a JSON-serializable dict with briefing and sections.
    """
    file_path = inputs.get("file_path")
    text = inputs.get("text")
    description = inputs.get("description")
    engine = inputs.get("engine", "heuristics")
    model_path = inputs.get("model_path")

    if file_path:
        return get_style_guidance_from_file(file_path, description=description, engine=engine, model_path=model_path)
    elif text:
        return get_style_guidance_from_text(text, description=description, engine=engine, model_path=model_path)
    else:
        raise ValueError("Either 'file_path' or 'text' must be provided")
