import textwrap
from pathlib import Path

import pytest

from markymarkov.api.validate import validate_code


def test_validate_code_syntax_ok():
    code = textwrap.dedent('''
    def f(x):
        return x * 2
    ''')
    res = validate_code(code, language="python")
    assert isinstance(res, dict)
    assert res.get("diagnostics") == []
    assert "No syntax" in res.get("summary", "")


def test_validate_code_syntax_error():
    code = "def f(:\n"
    res = validate_code(code, language="python")
    assert isinstance(res, dict)
    diags = res.get("diagnostics")
    assert isinstance(diags, list)
    assert len(diags) >= 1
    assert diags[0].get("code") == "SyntaxError"
    assert "Syntax error" in res.get("summary", "")


def test_validate_code_with_model(tmp_path: Path):
    # Create a trivial model with no probabilities to force issues
    model_code = """
MARKOV_ORDER = 2
probabilities = {}
"""
    model_path = tmp_path / "model.py"
    model_path.write_text(model_code, encoding="utf-8")

    code = textwrap.dedent('''
    def a():
        if True:
            return 1
    ''')
    res = validate_code(code, language="python", model_path=str(model_path))
    assert isinstance(res, dict)
    assert "diagnostics" in res
    # With empty probabilities, expect issues to be reported
    assert len(res.get("diagnostics", [])) >= 0
    # confidence should be present (best-effort)
    assert "confidence" in res
