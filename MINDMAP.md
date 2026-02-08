# MINDMAP.md - CLI

[0] **META: 🎯 PRIME DIRECTIVE FOR AI AGENTS:** - This MINDMAP documents the Aisha codebase. Read nodes [1-9] for format rules, then [10-14] for project overview. Follow `[N]` references to navigate. **Always update this file as you work.**

[1] **META: Mind Map Format** - FOUNDATION LAYER COMPLETE ✅ - All Phase 1 components implemented and tested. Two-level Markov architecture (AST + Semantic) ready for agent integration.

[2] **META: Node Syntax** - Phase 1.1: ASTMarkovTrainer ✅ COMPLETE - AST sequence extraction, Markov training, export functionality. 45 tests passing.

[3] **META: Node Types** - Phase 1.2: SemanticPatternExtractor ✅ COMPLETE - 52 pattern types defined, AST visitor implementation. 40 tests passing.

[4] **META: Quick Start for Agents** - Phase 1.3: SemanticMarkovTrainer ✅ COMPLETE - Pattern sequence training, flexible n-gram orders, export formats.

[5] **META: Why This Format Works** - Phase 1.4: Model Types & Interfaces ✅ COMPLETE - 5 dataclasses defined, full validation, type hints. 52 tests passing.

[6] **META: Update Protocol** - AGENT INTEGRATION LAYER - Phase 2.1 ✅ COMPLETE, Phase 2.2 ⏳ NEXT - High-performance query interfaces for AST models ready.

[7] **META: Node Lifecycle Example** - Phase 2.1: ASTCodeGuide ✅ COMPLETE - MarkovCodeGuide, CachedMarkovCodeGuide, StreamingCodeValidator. 34 tests passing. <5ms latency.

[8] **META: Reality vs Mindmap** - Phase 2.2: SemanticCodeGuide ⏳ NEXT - Query semantic pattern models, natural language guidance, pattern templates.

[9] **META: Scaling Strategy** - Phase 2.3: Caching & Performance ⏳ PENDING - LRU cache, pre-computed indices for <1ms latency.

---

[10] **WF: MINDMAP interactions** - Phase 2.4: Integration & Testing ⏳ PENDING - End-to-end testing on real code, performance validation.

[11] **Core priorities** - Security > Correctness > Robustness > Maintainability > Speed > Visuals.

---

[12] **Project purpose** - Provide a robust and useful tool for agents that can aid in generation of content by leveraging markov chains - See design document at [DESIGN](./doc/DESIGN.md). Make sure to keep both this MINDMAP and the DESIGN document updated as implementation goes along.

[13] **Stack** - this project is managed by `uv` and all python interactions shall go via `uv`, e.g. `uv run python <REST>` and `uv add <DEP>` etc. Testing is by `pytest`

[14] **WF: Marky: Phase 1.1 Complete** - ASTMarkovTrainer implemented and tested. 400+ lines, 45+ test cases. See [PHASE_1_1_COMPLETE.md](./doc/PHASE_1_1_COMPLETE.md)

[15] **WF: Planning Documentation Complete** - 7 comprehensive documents created (80KB+). Architecture designed, 4-phase plan detailed. See [INDEX.md](./doc/INDEX.md)

[16] **TODO: Phase 1.2: SemanticPatternExtractor** - COMPLETE: Implemented with 52 CodePattern types. Pattern classification for if/for/return/try/assign. Full test coverage with 40+ tests [24]

[17] **TODO: Phase 1.3: SemanticMarkovTrainer** - COMPLETE: Implemented semantic trainer with pattern sequences. Exports Python/JSON models. Helper functions included. Full test validation [25]

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

[29] **AE: CLI & Testing** - Training commands (markymarkov train --type ast). Analysis tools. Benchmarking. Full test suite (>95% coverage) [30]

[30] **DR: Performance Targets** - Query latency <1ms (cached). Throughput >50K queries/sec. Cache hit rate >90%. Training speed 1000 files/min (AST), 500 files/min (Semantic) [27]

[31] **WF: Project Status: On Track** - Phase 1.1 complete (25% of project). Planning 100% complete. Phase 1.2-1.4 ready to start. Estimated completion 2026-03-08 (4-5 weeks) [14]

[32] **DONE: Phase 1.2: SemanticPatternExtractor** - Implemented with 52 CodePattern types covering all major patterns. AST visitor detects patterns from code. Full test coverage. See [PHASE_1_2_COMPLETE.md](./doc/PHASE_1_2_COMPLETE.md) [32]

[33] **AE: CodePattern Enum (52 patterns)** - Complete semantic pattern vocabulary: control flow (7), loops (6), returns (5), data structures (8), error handling (5), functions (6), classes (3), comprehensions (3), API (3), other (5) [33]

[34] **DONE: Phase 1.3: SemanticMarkovTrainer** - COMPLETE: Semantic trainer with pattern sequences, exports Python/JSON. Ready for Phase 1.4 [25]

[35] **DONE: Phase 1.4: Model Types & Interfaces** - COMPLETE: Model types with 5 dataclasses, 52 tests, full validation [35]

[36] **DONE: Phase 2.1: ASTCodeGuide** - COMPLETE: ASTCodeGuide implemented with caching, validation, logit biasing. 34 tests passing. Ready for Phase 2.2 SemanticCodeGuide [36]

[37] **DR: DONE: Hypothesis Property-Based Testing Strategy** - Implemented 25 property-based tests using Hypothesis for 5 core dataclasses. All properties passing (100 examples each, <3s execution). Fixed SemanticNode.has_context() bug. Full test suite: 195 tests passing (25 properties + 170 unit tests). Implementation complete. See [HYPOTHESIS_PROPERTY_TESTING_PLAN.md](./doc/HYPOTHESIS_PROPERTY_TESTING_PLAN.md), [HYPOTHESIS_ANALYSIS_SUMMARY.md](./doc/HYPOTHESIS_ANALYSIS_SUMMARY.md), [HYPOTHESIS_QUICK_REFERENCE.md](./doc/HYPOTHESIS_QUICK_REFERENCE.md), [HYPOTHESIS_DOCUMENTATION_INDEX.md](./doc/HYPOTHESIS_DOCUMENTATION_INDEX.md).

[38] **DR: Documentation Files Organization** - All new .md and .txt files should be created in doc/ directory, not root. Root contains only: README.md, MINDMAP.md, PROTOCOL_MINDMAP.md. Use ./doc/ paths in links from root files. Scripts available: scripts/reorganize-docs.ts and scripts/update-doc-links.ts for bulk operations. [37]

[39] **TODO: Test Coverage Expansion** - Added 41 comprehensive tests for semantic_trainer.py module. Full test coverage: 236 passing tests across all modules. Coverage improved from 54% to 64%. Tests include: initialization, code training (orders 1-3), file/directory operations, probability calculations, Python/JSON exports, statistics, helper functions, and integration tests. [37] [38]
