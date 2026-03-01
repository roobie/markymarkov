# Chronicle: Commit API wrappers, CLI wiring, MCP manifests, and tests

timestamp: 2026-03-02T00:40:00+01:00
participants: assistant (agent), user

summary:

Committed changes that add API wrappers for style guidance and validation, MCP manifests, CLI subcommands, and pytest unit tests. Tests were run and passed locally after user fixed test environment issues.

commands run (representative):

- git add -A
- git commit -m "Add API wrappers, MCP manifests, CLI subcommands, and unit tests for style guidance and validation"
- (optional) git show --name-only HEAD

files added/modified (representative):

- src/markymarkov/api/__init__.py
- src/markymarkov/api/style.py
- src/markymarkov/api/validate.py
- tools/mcp/get_style_guidance.json
- tools/mcp/validate_code.json
- src/markymarkov/__main__.py (modified to wire CLI subcommands)
- tests/test_style.py
- tests/test_validate.py
- src/guides/ast_code_guide.py (compat proxy)
- src/trainers/ast_trainer.py (compat proxy)
- src/trainers/semantic_trainer.py (compat proxy)
- src/interfaces/model_types.py (compat proxy)
- src/__init__.py

next steps:

1. Push the commit to remote (if desired).
2. Add CI workflow to run tests on push (GitHub Actions) if not already present.
3. Iterate on improving diagnostics mapping and style guidance outputs.

notes:

- All actions have been recorded in chronicles/ per repository operational requirements.
- sg bookmarks were added for key files during development.
