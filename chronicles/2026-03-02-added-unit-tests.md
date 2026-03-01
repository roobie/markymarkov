# Chronicle: Added unit tests for API modules

timestamp: 2026-03-02T00:10:00+01:00
participants: assistant (agent), user

summary:

Added pytest unit tests for the new API modules under src/markymarkov/api/.

files added:

- tests/test_style.py
- tests/test_validate.py

actions taken:

- Created tests covering basic style guidance heuristics and MCP handler run path.
- Created tests covering syntax-only validation, syntax error handling, and model-based validation with a minimal dummy model.
- Added sg bookmarks for both test files.

next steps:

- Run the test suite (pytest) and fix any failing tests.
- Optionally add CI workflow to run tests on push.

