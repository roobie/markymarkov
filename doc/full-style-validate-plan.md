# Implementation Plan (aligned to existing repo): get_style_guidance and validate_code

Date: 2026-03-01T23:40:00+01:00 (revised)
Prepared by: assistant (agent)

Purpose

This document updates the earlier plan to align with the current implementation in src/markymarkov/ (Python). I reviewed the repository code (key files: __main__.py, trainers/, guides/, interfaces/) and added sg bookmarks to points of interest. The plan now prescribes concrete integration points that reuse existing Markov trainers/guides and provides a migration path to expose two new capabilities:

- get_style_guidance: take a file path (and optional description) and return a style briefing and structured guidance.
- validate_code: take code content and return LSP-style diagnostics (as a programmatic function and CLI/MCP UIs).

Where I looked

- src/markymarkov/__main__.py — current CLI, contains validation flows for AST and semantic models and the MarkyCLI class.
- src/markymarkov/trainers/ast_trainer.py — AST model training and sequence extraction utilities.
- src/markymarkov/trainers/semantic_trainer.py — semantic pattern trainer and related utilities.
- src/markymarkov/guides/ast_code_guide.py — MarkovCodeGuide and CachedMarkovCodeGuide helpers used for suggestions.
- src/markymarkov/interfaces/model_types.py — ASTContext and model-related types.

Bookmarks added (sg)

I added sg bookmarks to these file locations:
- src/markymarkov/__main__.py:1
- src/markymarkov/trainers/ast_trainer.py:1
- src/markymarkov/guides/ast_code_guide.py:1
- src/markymarkov/trainers/semantic_trainer.py:1
- src/markymarkov/interfaces/model_types.py:1

These bookmarks make it easier to reference key code while implementing the new APIs.

Design decisions (aligned to existing code)

1) Reuse existing trainers/guides
- The project already contains AST and semantic trainers and a MarkovCodeGuide implementation. For both style guidance and validation, reuse these components rather than re-implementing domain logic.
- For validation (validate_code), use the same sequence extraction logic in ASTMarkovTrainer and semantic pattern extractor to compute model-based diagnostics programmatically.

2) Provide programmatic API wrappers
- Create small wrapper modules in src/markymarkov/api/ (or src/markymarkov/cli_api/) that expose clean functions:
  - src/markymarkov/api/style.py → def get_style_guidance_from_file(file_path: str, description: Optional[str] = None, engine: str = "markov") -> Dict
  - src/markymarkov/api/validate.py → def validate_code(code: str, language: Optional[str] = 'python', filename: Optional[str] = None, model_path: Optional[str] = None, validators: Optional[List[str]] = None) -> Dict
- These wrappers will call existing MarkovCodeGuide, ASTMarkovTrainer.extract_ast_sequence, and semantic pattern extractors and return JSON-serializable structures.

3) CLI changes
- Extend MarkyCLI in src/markymarkov/__main__.py with two new subcommands (or add a thin wrapper CLI in bin/marky that imports these functions):
  - get_style_guidance <file_path> [--desc "..."] [--engine <engine>] [--json]
  - validate_code [--file <path> | --code <literal> | --stdin] [--model <model_path>] [--language <lang>] [--json]
- The CLI should call the API wrapper functions and print either human-friendly output or JSON when --json is provided.
- For validate_code, if a model_path is not provided, fall back to syntax-only validation using ast.parse and return diagnostics for syntax errors.

4) MCP manifests and Python handlers
- Add tools/mcp/get_style_guidance.json and tools/mcp/validate_code.json with handler fields pointing to Python modules:
  - handler: "markymarkov.api.get_style.get_style_guidance_handler.run"
  - handler: "markymarkov.api.validate.validate_code_handler.run"
- Implement the handler adapters in src/markymarkov/api/ that expose run(inputs: Dict[str,Any]) -> Dict[str,Any] for compatibility with the MCP runtime.

Data schemas (programmatic outputs)

- Style guidance (return)
  {
    "briefing": str,  # human-friendly summary
    "sections": Optional[Dict[str,str]],  # e.g., tone, naming, imports, suggestions
    "examples": Optional[List[str]]  # optional minimal examples / suggestions
  }

- Diagnostics (validate_code return)
  {
    "diagnostics": [
      {
        "range": {"start": {"line": int, "character": int}, "end": {...}},
        "severity": int,  # 1=Error,2=Warning,3=Info,4=Hint
        "source": str,
        "code": Optional[str|int],
        "message": str
      },
      ...
    ],
    "summary": str,  # human summary
    "confidence": Optional[float]  # model confidence (0..1) when model used
  }

How validate_code will be implemented (practical mapping)

- Syntax-only fallback: for Python code, use ast.parse to detect SyntaxError. Convert that into one Diagnostic with range at the syntax error location.
- Model-based diagnostics: when a Markov model path is provided and is an AST or semantic model, load the model (same _load_model code in __main__.py), extract sequences using ASTMarkovTrainer or semantic extractor, then iterate transitions and compare against model.probabilities like the current _validate_ast/_validate_semantic logic.
  - Map unexpected transitions and unknown contexts into Diagnostic objects. Attach approximate line/column info when available (for semantic patterns we already gather lineno/col_offset in semantic extractor patterns).
  - Compute a confidence score analogous to current confidence calculation and return it.

How get_style_guidance will be implemented (practical)

- Use MarkovCodeGuide and CachedMarkovCodeGuide to analyze the code base or a provided model to extract common patterns and top suggestions.
- Heuristics-based guidance: inspect file extension and conventions (snake_case vs camelCase, presence/absence of docstrings, import grouping) using simple analyses (AST + regex).
- Model-augmented guidance (if a model is supplied or available): examine model.probabilities to identify common transitions, high-probability next nodes, and typical idioms; convert these into human-readable recommendations (e.g., "Prefer using 'with' for file I/O", "Group standard-library imports separately").
- Output both a short briefing and structured sections.

Implementation steps (concrete)

1) Add sg bookmarks (done) and record this action in chronicles/ (see entry created)

2) Implement API wrappers (1–2 hours)
  - Create src/markymarkov/api/__init__.py
  - Create src/markymarkov/api/style.py and src/markymarkov/api/validate.py. These expose the pure functions described above and rely on existing trainers/guides.
  - Add handler adapter functions for MCP (run(inputs)) in the same modules or in src/markymarkov/api/handlers.py.

3) Add CLI subcommands (0.5–1 hour)
  - Modify src/markymarkov/__main__.py: add two subparsers (_setup_style_parser, _setup_validate_code_parser) and handler functions that call the API wrappers.
  - Ensure CLI supports reading code from stdin.

4) MCP manifests (0.5 hour)
  - Add tools/mcp/get_style_guidance.json and tools/mcp/validate_code.json pointing to handler run functions.

5) Tests and CI (1–2 hours)
  - Add tests/test_style.py and tests/test_validate.py using pytest. Tests should exercise syntax-only validation and model-based behavior using a small in-memory or exported model created by trainers in tests.
  - Add GitHub Actions workflow to run pytest.

6) Documentation and examples (0.5 hour)
  - Update @doc/full-style-validate-plan.md (this file) and README with usage examples for CLI and MCP.

7) Chronicle (operational requirement)
  - Append a chronicle entry recording code review and sg.add bookmarks (see chronicles/2026-03-01-sg-add-bookmarks.md).

Files to add or modify

- Add: src/markymarkov/api/style.py
- Add: src/markymarkov/api/validate.py
- Modify: src/markymarkov/__main__.py (add CLI subcommands and thin glue)
- Add: tools/mcp/get_style_guidance.json
- Add: tools/mcp/validate_code.json
- Add: tests/test_style.py
- Add: tests/test_validate.py
- Add: chronicles/2026-03-01-code-review-and-bookmarks.md

Acceptance criteria (aligned)

- Programmatic functions exist under src/markymarkov/api/ and are unit-tested.
- CLI subcommands get_style_guidance and validate_code are available in the MarkyCLI and return JSON when requested.
- MCP manifests exist and handler run(inputs) functions are callable.
- Chronicle entry records this review and sg bookmarks.

Risks and mitigations

- Mapping model-based issues to exact source locations can be imprecise. Mitigate by including best-effort lineno/col when available and falling back to context snippets.
- External linters and language support beyond Python will require subprocess wrappers; isolate these behind validator adapters.
- LLM augmentation (optional) requires careful API key handling — keep it opt-in and environment-based.

Estimated effort

- Minimal (API wrappers + CLI + manifests + basic tests): 3–6 hours.
- Full (good diagnostics mapping, pluggable validators, LLM engine): 1–2 days.

Next actions I can take now

- Generate the Python API skeletons and MCP manifests and add corresponding sg bookmarks.
- Modify src/markymarkov/__main__.py to add the two subcommands (I will make a small, well-tested change).
- Create unit tests and a chronicle entry for these changes.

Reply with one of:
- "generate python skeleton" — I will create the API modules, MCP manifests, CLI changes, tests, and chronicle entries.
- "generate api only" — I will only generate src/markymarkov/api/style.py and src/markymarkov/api/validate.py plus handlers.
- "just bookmarks" — I will only add sg bookmarks to additional locations you specify.
- Or request further edits to this plan.
