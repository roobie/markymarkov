# MINDMAP.md - CLI

[0] **META: 🎯 PRIME DIRECTIVE FOR AI AGENTS:** - This MINDMAP documents the Aisha codebase. Read nodes [1-9] for format rules, then [10-14] for project overview. Follow `[N]` references to navigate. **Always update this file as you work.**

[1] **META: Mind Map Format** - This is a graph-based documentation format where each node is exactly one line: `[N] **Title** - content with any number of [N] references`. The format is markdown-compatible, grep-able, and git-friendly [2][3][4]. Nodes enable atomic updates, instant search, and LLM-native citation syntax [5][6].

[2] **META: Node Syntax** - Format is `[N] **Title** - body with [N] references`. Each node is exactly one line. Titles use markdown bold `**...**`. References use citation syntax `[N]` which LLMs recognize from academic papers [1][3].

[3] **META: Node Types** - Nodes are prefixed by type: `**AE: X**` (Architecture Element), `**WF: X**` (Workflow), `**DR: X**` (Decision Record), `**BUG: X**` (Bug Record), `**TODO: X**` (Planned Work), `**DOING: X**` (Work under way), `**DONE: X**` (Work completed), `**META: X**` (Documentation about this mindmap) [1][2][4].

[4] **META: Quick Start for Agents** - First time? (1) Read [1-9] for format, (2) Read [10-14] for project overview, (3) Grep for your task: `grep -i "llm"` then read matching nodes, (4) Follow `[N]` links, (5) Update nodes as you work per protocol [6][7][8].

[5] **META: Why This Format Works** - Line-oriented = atomic updates (replace line N to update node N), instant grep (`grep "^\[42\]"`), diff-friendly (only edited lines change), zero parsing overhead [1][2]. The `[N]` citation syntax leverages LLM training on academic papers [3].

[6] **META: Update Protocol** - **MANDATORY:** (1) Before work, grep for related nodes and read them [4], (2) After changes, update affected nodes immediately, (3) Add new nodes if concept is referenced 3+ times OR non-obvious from code, (4) For bugs create `**BUG:**` node with root cause + solution [3][7].

[7] **META: Node Lifecycle Example** - use `mindmap-cli add/put/patch/delete` to interact with the MINDMAP [6][3].

[8] **META: Reality vs Mindmap** - **Critical:** If MINDMAP contradicts code, code is truth—update MINDMAP immediately [6]. This MINDMAP is an index, not a spec. Stale nodes are worse than missing nodes.

[9] **META: Scaling Strategy** - Current project: <100 nodes. If exceeds 100, split into domain files like `MINDMAP.llm.md`, `MINDMAP.execution.md` [10]. Link from main: `[15] **AE: LLM System** - See MINDMAP.llm.md for details` [1][3].

---

[10] **WF: MINDMAP interactions** - VERY IMPORTANT💯: it is **mandatory** to use the program `mindmap-cli` to interact with MINDMAP files. I.e. querying, reading and updating shall be done by invoking `mindmap-cli`. It is forbidden to update METADATA.md directly. Learn how to use this tool by invoking `mindmap-cli help`. Required reading: [PROTOCOL_MINDMAP.md](./PROTOCOL_MINDMAP.md)

[11] **Core priorities** - Security > Correctness > Robustness > Maintainability > Speed > Visuals.

---

[12] **Project purpose** - Provide a robust and useful tool for agents that can aid in generation of content by leveraging markov chains - See design document at [DESIGN](./DESIGN.md). Make sure to keep both this MINDMAP and the DESIGN document updated as implementation goes along.

[13] **Stack** - this project is managed by `uv` and all python interactions shall go via `uv`, e.g. `uv run python <REST>` and `uv add <DEP>` etc. Testing is by `pytest`

[14] **WF: Marky: Phase 1.1 Complete** - ASTMarkovTrainer implemented and tested. 400+ lines, 45+ test cases. See [PHASE_1_1_COMPLETE.md](./PHASE_1_1_COMPLETE.md)

[15] **WF: Planning Documentation Complete** - 7 comprehensive documents created (80KB+). Architecture designed, 4-phase plan detailed. See [INDEX.md](./INDEX.md)

[16] **TODO: Phase 1.2: SemanticPatternExtractor** - COMPLETE: Implemented with 52 CodePattern types. Pattern classification for if/for/return/try/assign. Full test coverage with 40+ tests [24]

[17] **TODO: Phase 1.3: SemanticMarkovTrainer** - Use extractor from 1.2 to build semantic Markov chains. Export models. ~6-9 hours. Depends on 1.2 [25]

[18] **TODO: Phase 1.4: Model Types/Interfaces** - Define dataclasses: NextNodeSuggestion, NextPatternSuggestion, ASTContext, ValidationResult. ~2-3 hours. [26]

[19] **WF: Phase 2: Agent Integration** - ASTCodeGuide (2.1), SemanticCodeGuide (2.2), Caching/Performance (2.3). ~40-50 hours. Depends on Phase 1 [27]

[20] **WF: Phase 3: Advanced Features** - REST API (3.1), Prompt Enhancement (3.2), Reference Agent (3.3). ~40-50 hours [28]

[21] **WF: Phase 4: Polish & Production** - CLI Tools (4.1), Comprehensive Tests (4.2), Final Docs (4.3). ~40-50 hours [30]

[22] **DR: Two-Level Architecture** - AST level for syntax validation, Semantic level for high-level patterns. Complementary, not redundant. Improves both correctness and UX [12]

[23] **AE: ASTMarkovTrainer** - Core trainer for AST patterns. Supports orders 1-3. Exports to Python/JSON. Helper functions included. Located at src/trainers/ast_trainer.py [15]

[24] **AE: Phase 1 Foundation** - Core trainers and types. AST trainer (1.1) complete. Semantic extractor (1.2-1.3) in progress. Model types (1.4) planned [14]

[25] **AE: SemanticPatternExtractor** - Defines 50 CodePattern enum values. Classifies if/for/return/try statements. Creates pattern sequences. Depends on Phase 1.1 [25]

[26] **AE: Query Interfaces (Phase 2)** - ASTCodeGuide and SemanticCodeGuide provide fast <1ms lookups. Caching layer. Fallback mechanisms. Temperature sampling [19]

[27] **DR: Export Strategy** - Models exported as executable Python with helper functions. Eliminates parsing overhead. Simplifies integration. JSON also supported [23]

[28] **DR: 50 Semantic Patterns** - Control flow (IF_NOT_NONE, GUARD_CLAUSE, etc), Loops (LOOP_FILTER, LOOP_TRANSFORM, etc), Returns, Data structures, Error handling, Functions, Comprehensions, API patterns [25]

[29] **AE: CLI & Testing** - Training commands (marky train --type ast). Analysis tools. Benchmarking. Full test suite (>95% coverage) [30]

[30] **DR: Performance Targets** - Query latency <1ms (cached). Throughput >50K queries/sec. Cache hit rate >90%. Training speed 1000 files/min (AST), 500 files/min (Semantic) [27]

[31] **WF: Project Status: On Track** - Phase 1.1 complete (25% of project). Planning 100% complete. Phase 1.2-1.4 ready to start. Estimated completion 2026-03-08 (4-5 weeks) [14]

[32] **DONE: Phase 1.2: SemanticPatternExtractor** - Implemented with 52 CodePattern types covering all major patterns. AST visitor detects patterns from code. Full test coverage. See [PHASE_1_2_COMPLETE.md](./PHASE_1_2_COMPLETE.md) [32]

[33] **AE: CodePattern Enum (52 patterns)** - Complete semantic pattern vocabulary: control flow (7), loops (6), returns (5), data structures (8), error handling (5), functions (6), classes (3), comprehensions (3), API (3), other (5) [33]
