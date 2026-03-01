import json
import textwrap
from pathlib import Path

import pytest

from markymarkov.api.style import get_style_guidance_from_file, get_style_guidance_from_text, run


def test_get_style_guidance_from_file(tmp_path: Path):
    code = textwrap.dedent('''
    # TODO: improve this
    def foo_bar(x, y):
        return x + y  # simple add

    # a very long line follows
    a = """{}"""
    '''.format('x' * 130))

    file_path = tmp_path / "sample.py"
    file_path.write_text(code, encoding="utf-8")

    res = get_style_guidance_from_file(str(file_path), description="sample function")
    assert isinstance(res, dict)
    assert "briefing" in res
    assert "sections" in res
    sections = res["sections"]
    # Expect todo count and long_lines to be reported
    assert "todos" in sections
    assert "long_lines" in sections
    assert "naming" in sections
    assert "snake_case" in sections["naming"] or "no top-level functions" not in sections["naming"]


def test_get_style_guidance_from_text_and_run():
    src = 'def my_func():\n    """docstring"""\n    pass\n'
    res = get_style_guidance_from_text(src, description="docstring present")
    assert isinstance(res, dict)
    assert "briefing" in res

    # test MCP-style run with text input
    inp = {"text": src, "description": "docstring present"}
    out = run(inp)
    assert "briefing" in out
    assert "sections" in out
