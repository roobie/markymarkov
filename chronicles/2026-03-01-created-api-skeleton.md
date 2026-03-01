# Chronicle: Created API skeleton and MCP manifests

timestamp: 2026-03-01T23:52:00+01:00
participants: assistant (agent), user

summary:

Generated initial API wrapper modules and MCP handler entrypoints to expose get_style_guidance and validate_code programmatically.

actions taken:

- Added API package: src/markymarkov/api/
  - src/markymarkov/api/__init__.py
  - src/markymarkov/api/style.py
  - src/markymarkov/api/validate.py
- Added MCP manifests:
  - tools/mcp/get_style_guidance.json
  - tools/mcp/validate_code.json
- Added sg bookmarks for the new API modules and manifests.

commands run (representative):

- wrote src/markymarkov/api/__init__.py
- wrote src/markymarkov/api/style.py
- wrote src/markymarkov/api/validate.py
- sg add src/markymarkov/api/style.py:1
- sg add src/markymarkov/api/validate.py:1
- wrote tools/mcp/get_style_guidance.json
- wrote tools/mcp/validate_code.json
- sg add tools/mcp/get_style_guidance.json:1
- sg add tools/mcp/validate_code.json:1

files added:

- src/markymarkov/api/__init__.py
- src/markymarkov/api/style.py
- src/markymarkov/api/validate.py
- tools/mcp/get_style_guidance.json
- tools/mcp/validate_code.json

suggested next steps:

1. Run unit tests for the new modules (I can add tests if you want).
2. Wire the MarkyCLI to call the API wrappers (or add a thin CLI wrapper). I can modify src/markymarkov/__main__.py to add subcommands.
3. Expand model-based guidance (e.g., generate natural-language recommendations from model patterns).

notes:

- The API implementations are initial skeletons with heuristics and best-effort model usage; they should be extended and hardened for production use.

