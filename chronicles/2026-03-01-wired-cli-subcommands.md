# Chronicle: Wired CLI subcommands for API

timestamp: 2026-03-01T23:59:30+01:00
participants: assistant (agent), user

summary:

Added CLI subcommands get_style_guidance and validate_code to the MarkyCLI in src/markymarkov/__main__.py. These subcommands call the API wrapper modules under src/markymarkov/api/ and support JSON output.

actions taken:

- Modified src/markymarkov/__main__.py to add:
  - _setup_style_parser and _setup_validate_code_parser
  - _get_style_guidance_cmd and _validate_code_cmd handlers
  - integrated the new commands into the CLI dispatch
- Added sg bookmark for the modified __main__.py file.

commands run (representative):

- edited src/markymarkov/__main__.py
- sg add src/markymarkov/__main__.py:1

files modified:

- src/markymarkov/__main__.py (updated)

suggested next steps:

1. Run basic manual smoke tests:
   - python -m src get_style_guidance path/to/file.py
   - cat file.py | python -m src validate_code --json
2. Add pytest unit tests for the new CLI handlers.
3. Improve error messages and exit codes if desired.

notes:

- The CLI changes reuse existing model loading and validation logic.
- For validate_code, stdin reading is supported (if code not provided via --code/--file).

