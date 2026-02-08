# MARKY: Comprehensive Implementation Plan Summary

**Document Generated**: 2026-02-08  
**Based On**: `primer.md` discussion with Claude Sonnet 4.5  
**Status**: Planning Mode Complete - Ready for Development

---

## Executive Summary

This plan outlines a complete, phased implementation of **Marky**: a Markov chain-based guidance system for LLM coding agents, operating at two complementary abstraction levels:

1. **AST-Level Markov Chains**: Fast, syntactically-focused guidance (~200 node types)
2. **Semantic-Level Markov Chains**: High-level pattern guidance (~50 semantic patterns)

Both trainers extract patterns from Python code, build probabilistic models of state transitions, and expose agent-friendly query interfaces with sub-millisecond latency.

---

## Two-Level Architecture

### Why Two Levels?

**AST Level (Lower)**
- **What**: Raw Abstract Syntax Tree node transitions
- **Why**: Ensures syntactic validity, captures structural details
- **Speed**: Fast but less interpretable
- **Coverage**: ~200 unique node types

**Semantic Level (Higher)**
- **What**: High-level coding pattern transitions (e.g., "if-not-none" → "loop-filter" → "return-list")
- **Why**: Agents think in patterns, not syntax; more transferable; better guidance
- **Speed**: Slightly slower but 5-10x fewer states
- **Coverage**: ~50 semantic patterns

**Synergy**: Use semantic for high-level architectural decisions, fall back to AST for syntactic validation.

---

## Four-Phase Implementation

### Phase 1: Foundation (Trainers & Core Types)
**Deliverables**: Two working trainers + model types

1. **ASTMarkovTrainer** (1.1)
   - Parses Python files → extracts AST node sequences
   - Builds n-gram models (bigram/trigram support)
   - Exports to `ast_markov_model.py`
   - Status: Straightforward, proven approach

2. **SemanticPatternExtractor** (1.2)
   - Detects 50+ high-level patterns: `IF_NOT_NONE`, `LOOP_FILTER`, `RETURN_LIST`, etc.
   - Implemented as AST visitor with classification heuristics
   - Status: Most complex pattern detection logic

3. **SemanticMarkovTrainer** (1.3)
   - Uses extractor to get pattern sequences
   - Builds semantic n-grams
   - Exports to `semantic_model.py`
   - Status: Straightforward once extractor ready

4. **Model Types** (1.4)
   - Dataclasses: `NextNodeSuggestion`, `NextPatternSuggestion`, `ASTContext`, etc.
   - Status: Simple, foundational

**Success Criteria**: 
- Trainers successfully process 1000+ files
- Models export correctly, are executable
- >90% unit test coverage

**Effort**: 1-2 weeks with careful testing

---

### Phase 2: Agent Integration (High-Performance Interfaces)
**Deliverables**: Two high-performance query interfaces for agents

1. **ASTCodeGuide** (2.1)
   - Query interface for AST models
   - Features: Fast lookups, temperature sampling, logit biasing, fallbacks
   - Caching layer pre-warms with common patterns
   - Methods:
     - `suggest_next_nodes(context, top_k, temperature)` → suggestions
     - `validate_sequence(ast_sequence)` → (valid, confidence, warnings)
     - `bias_logits(llm_logits, context)` → for LLM integration

2. **SemanticCodeGuide** (2.2)
   - Query interface for semantic models
   - Features: Template-based code generation, pattern chains
   - Methods:
     - `suggest_next(partial_code, top_k)` → pattern suggestions
     - `generate_prompt_guidance(partial_code)` → natural language hints
     - `complete_with_pattern(partial_code, pattern)` → filled template

3. **Performance Optimization** (2.3)
   - LRU caching with pre-warming
   - Benchmarking utilities
   - Target: <1ms cached lookup, 50K queries/sec

**Success Criteria**:
- <1ms lookup latency (cached)
- >90% fallback success for unknown states
- 50%+ performance gain from caching
- Works with real LLM token logits

**Effort**: 1-2 weeks

---

### Phase 3: Advanced Features
**Deliverables**: REST API, prompt enhancement, reference agent

1. **REST API Service** (3.1)
   - Expose both guides as HTTP endpoints
   - Endpoints: `/ast/suggest`, `/semantic/suggest`, `/validate`, `/health`
   - Enables remote agents to use models

2. **Prompt Enhancement** (3.2)
   - Automatically suggest patterns to include in LLM prompts
   - Methods:
     - `enhance_prompt(base_prompt, partial_code)` → prompt with guidance
     - `generate_prompt_guidance(partial_code)` → markdown hints

3. **Reference Semantic Coding Agent** (3.3)
   - Full end-to-end example
   - Uses semantic patterns to guide LLM generation
   - Iterative refinement loop: scaffold → LLM → validation → refine

**Success Criteria**:
- API handles 1000 req/sec
- Agent generates syntactically valid code 95%+ of the time
- End-to-end function generation in <5 seconds

**Effort**: 1-2 weeks

---

### Phase 4: Polish & Production
**Deliverables**: CLI tools, comprehensive tests, documentation

1. **CLI Tools** (4.1)
   - `marky train --type {ast|semantic} --input <path> --output model.py`
   - `marky analyze model.py --top-patterns 20`
   - `marky benchmark model.py --queries 10000`

2. **Comprehensive Test Suite** (4.2)
   - Unit tests for all modules (>95% coverage)
   - Integration tests (trainer → model → guide pipelines)
   - Performance tests (validate latency/throughput targets)
   - End-to-end tests (full agent scenarios)

3. **Documentation** (4.3)
   - `ARCHITECTURE.md` - System design
   - `API_REFERENCE.md` - Complete API docs
   - `USAGE_GUIDE.md` - How to use for different scenarios
   - Examples: training on stdlib, agent integration, custom patterns

**Success Criteria**:
- Intuitive CLI
- >95% test coverage
- Complete, tested documentation
- Examples run without modification

**Effort**: 1-2 weeks

---

## File Structure

```
marky/
├── ./IMPLEMENTATION_PLAN.md      ← Detailed phase breakdown
├── IMPLEMENTATION_ROADMAP.mindmap ← Visual overview
├── primer.md                   ← Original discussion/ideas
├── src/
│   ├── trainers/
│   │   ├── ast_trainer.py           [Phase 1.1]
│   │   ├── semantic_pattern_extractor.py [Phase 1.2]
│   │   └── semantic_trainer.py       [Phase 1.3]
│   ├── interfaces/
│   │   └── model_types.py            [Phase 1.4]
│   ├── guides/
│   │   ├── ast_code_guide.py         [Phase 2.1]
│   │   ├── semantic_code_guide.py    [Phase 2.2]
│   │   └── performance.py            [Phase 2.3]
│   ├── api/
│   │   └── markov_service.py         [Phase 3.1]
│   ├── prompt_engineering/
│   │   └── enhancer.py               [Phase 3.2]
│   ├── agents/
│   │   └── semantic_coding_agent.py  [Phase 3.3]
│   └── cli/
│       ├── train_command.py          [Phase 4.1]
│       └── analyze_command.py        [Phase 4.1]
├── tests/                            [Phase 4.2]
│   ├── trainers/
│   ├── guides/
│   ├── api/
│   ├── agents/
│   └── integration/
├── docs/                             [Phase 4.3]
│   ├── ARCHITECTURE.md
│   ├── API_REFERENCE.md
│   └── USAGE_GUIDE.md
├── examples/                         [Phase 4.3]
│   ├── train_from_stdlib.py
│   ├── agent_integration.py
│   └── custom_patterns.py
└── README.md
```

---

## Key Design Decisions

### 1. Two Separate Trainers
- **Pros**: Complementary coverage, flexibility, potential for ensemble approaches
- **Cons**: More code to maintain
- **Rationale**: Semantic patterns are more useful for agents; AST ensures correctness

### 2. Flexible Order (1, 2, 3)
- Order 1 (bigram): Fast, less context
- Order 2 (trigram): Default, good balance
- Order 3: More context, but sparse
- **Allows**: Users to tune accuracy vs. model size

### 3. Fallback Mechanisms
- When exact state not found, aggregate probabilities from similar states
- Essential for agent reliability (not every code sequence will be in training data)

### 4. Caching & Pre-warming
- Pre-compute suggestions for common patterns
- LRU cache for recent queries
- Target: >90% cache hit rate on typical workloads

### 5. REST API Service
- Allow agents to run independently
- Model as separate service
- Enables horizontal scaling

### 6. Pattern Templates
- Code templates for each semantic pattern
- Agent can quickly scaffold using patterns
- Example: `LOOP_FILTER` → `for {item} in {collection}:\n    if {condition}:\n        result.append({item})`

---

## Critical Success Factors

### 1. Pattern Detection Accuracy
- **Challenge**: Heuristics for pattern detection may miss edge cases
- **Mitigation**: Comprehensive test suite, training on diverse codebases

### 2. Sparse State Space
- **Challenge**: Most state transitions won't appear in training data
- **Mitigation**: Fallback mechanisms, aggregation strategies

### 3. Performance Targets
- **Challenge**: Sub-millisecond latency
- **Mitigation**: Caching, index pre-computation, efficient data structures

### 4. Agent Integration
- **Challenge**: Making it easy for agents to use
- **Mitigation**: Simple APIs (`quick_suggest`, `validate_generated_code`)

---

## Expected Performance

### Training Speed
- **AST Trainer**: ~1000 files/minute
- **Semantic Trainer**: ~500 files/minute (pattern detection is slower)

### Model Size
- **AST Model**: 10-50MB (depends on vocabulary size)
- **Semantic Model**: 1-10MB (much smaller vocabulary)

### Query Speed
- **Uncached**: ~5-20ms per query
- **Cached**: <1ms per query (typical case)
- **Throughput**: >50K queries/second (single core)

### Accuracy
- **Pattern Detection**: 85-95% (depends on complexity)
- **Valid Sequence Generation**: 90-99% (post-validation)
- **Cache Hit Rate**: >90% (with pre-warming)

---

## How This Solves the Original Problem

**Original Challenge**: How can LLM coding agents use Markov chains for structural guidance?

**This Solution**:

1. **Two-Level Abstraction**
   - Semantic patterns for high-level guidance ("consider using a loop")
   - AST validation for syntactic correctness

2. **Agent-Friendly Interfaces**
   - `quick_suggest()` for one-liners
   - `suggest_next_patterns()` for context-aware suggestions
   - `generate_prompt_guidance()` for prompt enhancement

3. **Multiple Integration Points**
   - Prompt enhancement (simplest)
   - Logit biasing (most sophisticated)
   - REST API (most flexible)
   - Direct function calls (most integrated)

4. **Performance Optimized**
   - <1ms latency doesn't slow down generation
   - Caching handles typical patterns
   - Fallbacks handle edge cases

5. **Validated Approach**
   - Tested on real codebases
   - Measurable success metrics
   - Production-ready by Phase 4

---

## Estimated Timeline

| Phase | Work | Estimate | Notes |
|-------|------|----------|-------|
| 1 | Trainers & Types | 1-2 weeks | Most straightforward |
| 2 | Guides & Optimization | 1-2 weeks | Cache/fallback logic critical |
| 3 | Advanced Features | 1-2 weeks | Agent integration testing |
| 4 | Polish & Tests | 1-2 weeks | Comprehensive test suite |
| **Total** | **Full System** | **4-8 weeks** | Development + testing |

---

## Next Steps

1. **Immediate** (Today)
   - Review this plan
   - Identify any gaps or concerns
   - Confirm Phase 1.1 approach

2. **This Week**
   - Implement Phase 1.1: ASTMarkovTrainer
   - Write comprehensive tests
   - Validate on Python stdlib subset

3. **Following Week**
   - Implement Phase 1.2-1.4 in parallel
   - Integrate tests
   - Begin Phase 2 design review

4. **Ongoing**
   - Iterate with real agent testing
   - Adjust success criteria based on findings
   - Document as we go

---

## Questions for Validation

Before starting implementation:

1. **Scope**: Are 50 semantic patterns enough, or should we add domain-specific patterns?
2. **Order**: Should we default to order-2 (trigram) or offer runtime configuration?
3. **Training Data**: What size codebase should we target for initial model? (stdlib? larger?)
4. **Agent Integration**: Which integration point is highest priority? (Prompt enhancement seems simplest)
5. **REST API**: Is this a Phase 3 must-have or can we defer to Phase 4?

---

## References

- `primer.md` - Original discussion with conceptual examples
- Claude Sonnet 4.5 - Architecture guidance and code examples
- AST documentation - Python's `ast` module behavior
- Markov chain literature - Theory and applications

---

**Status**: ✅ Planning Complete - Ready to Begin Phase 1.1  
**Last Updated**: 2026-02-08 00:26 GMT+1
