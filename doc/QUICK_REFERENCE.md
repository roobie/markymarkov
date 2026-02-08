# Quick Reference: Marky Implementation Plan

## TL;DR

Build a **dual-level Markov chain system** for LLM coding agents:
- **AST Level**: Syntactic guidance (~200 node types)
- **Semantic Level**: Pattern guidance (~50 high-level patterns)

Both trainers extract from Python code, export to executable models, expose fast query interfaces.

---

## The Two Levels

| Aspect            | AST Level                          | Semantic Level                                           |
|-------------------|------------------------------------|----------------------------------------------------------|
| **What**          | Raw syntax trees                   | High-level patterns                                      |
| **Examples**      | `FunctionDef → arguments → Return` | `GUARD_CLAUSE → IF_NOT_NONE → LOOP_FILTER → RETURN_LIST` |
| **Vocab Size**    | ~200 node types                    | ~50 patterns                                             |
| **Model Size**    | 10-50MB                            | 1-10MB                                                   |
| **Query Latency** | <1ms (cached)                      | <1ms (cached)                                            |
| **Use Case**      | Ensure syntax correctness          | High-level architectural guidance                        |

---

## 4-Phase Plan

### Phase 1: Trainers (1-2 weeks)
1. **ASTMarkovTrainer** - Parse → extract sequences → export model
2. **SemanticPatternExtractor** - AST → detect 50 patterns
3. **SemanticMarkovTrainer** - Pattern sequences → export model
4. **Model Types** - Data classes for interfaces

### Phase 2: Agent Integration (1-2 weeks)
1. **ASTCodeGuide** - Query interface for AST models
2. **SemanticCodeGuide** - Query interface for semantic models
3. **Caching** - Pre-warming, LRU cache, benchmarking

### Phase 3: Advanced (1-2 weeks)
1. **REST API** - HTTP endpoints for both guides
2. **Prompt Enhancement** - Auto-generate guidance text
3. **Reference Agent** - End-to-end example

### Phase 4: Polish (1-2 weeks)
1. **CLI Tools** - Training and analysis commands
2. **Test Suite** - >95% coverage
3. **Documentation** - Guides, examples, reference

---

## Key Files

| File                            | Phase | Purpose                              |
|---------------------------------|-------|--------------------------------------|
| `ast_trainer.py`                | 1.1   | Parse Python → extract AST sequences |
| `semantic_pattern_extractor.py` | 1.2   | Detect 50+ semantic patterns         |
| `semantic_trainer.py`           | 1.3   | Pattern sequences → export model     |
| `model_types.py`                | 1.4   | Dataclasses for all interfaces       |
| `ast_code_guide.py`             | 2.1   | Query interface for AST models       |
| `semantic_code_guide.py`        | 2.2   | Query interface for semantic models  |
| `performance.py`                | 2.3   | Caching & benchmarking               |
| `markov_service.py`             | 3.1   | REST API endpoints                   |
| `enhancer.py`                   | 3.2   | Prompt enhancement                   |
| `semantic_coding_agent.py`      | 3.3   | Reference agent implementation       |

---

## 50 Semantic Patterns

| Category                  | Patterns                                                                                                                                                           |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Control Flow** (5)      | `IF_NONE_CHECK`, `IF_NOT_NONE`, `IF_EMPTY_CHECK`, `IF_TYPE_CHECK`, `GUARD_CLAUSE`                                                                                  |
| **Loops** (6)             | `LOOP_ACCUMULATE`, `LOOP_TRANSFORM`, `LOOP_FILTER`, `LOOP_ENUMERATE`, `LOOP_ZIP`, `LOOP_DICT_ITEMS`                                                                |
| **Returns** (5)           | `RETURN_NONE`, `RETURN_BOOL`, `RETURN_LIST`, `RETURN_DICT`, `RETURN_COMPUTED`                                                                                      |
| **Data Structures** (8)   | `INIT_EMPTY_LIST`, `INIT_EMPTY_DICT`, `INIT_COUNTER`, `APPEND_TO_LIST`, `DICT_UPDATE`, `DICT_GET_DEFAULT`, `DEFAULT_DICT_PATTERN`, `UNPACKING`                     |
| **Error Handling** (5)    | `TRY_EXCEPT_PASS`, `TRY_EXCEPT_LOG`, `TRY_EXCEPT_RERAISE`, `TRY_FINALLY`, `CONTEXT_MANAGER`                                                                        |
| **Functions/Classes** (6) | `FUNCTION_VALIDATOR`, `FUNCTION_TRANSFORMER`, `INIT_METHOD`, `PROPERTY_GETTER`, `CLASS_METHOD`, `STATIC_METHOD`                                                    |
| **Comprehensions** (3)    | `LIST_COMPREHENSION`, `DICT_COMPREHENSION`, `GENERATOR_EXPRESSION`                                                                                                 |
| **API Patterns** (3)      | `API_VALIDATION`, `API_ERROR_RESPONSE`, `API_SUCCESS_RESPONSE`                                                                                                     |
| **Other Idioms** (8)      | `TERNARY_EXPRESSION`, `STRING_FORMAT`, `LOGGING_CALL`, `EARLY_RETURN_SUCCESS`, `EARLY_RETURN_FAILURE`, `PROPERTY_SETTER`, `FUNCTION_DECORATOR`, `FUNCTION_FACTORY` |

---

## Common Usage Patterns

### Training (One-time)

```python
from trainers import ASTMarkovTrainer, SemanticMarkovTrainer

# AST Training
ast_trainer = ASTMarkovTrainer(order=2)
ast_trainer.train_on_directory('/path/to/code')
ast_trainer.export_to_python('ast_model.py')

# Semantic Training
sem_trainer = SemanticMarkovTrainer(order=2)
sem_trainer.train_on_directory('/path/to/code')
sem_trainer.export_to_python('semantic_model.py')
```

### Query (Runtime)

```python
import ast_model, semantic_model
from guides import MarkovCodeGuide, SemanticCodeGuide

# Load guides
ast_guide = MarkovCodeGuide(ast_model)
sem_guide = SemanticCodeGuide(semantic_model)

# AST suggestions
ast_suggestions = ast_guide.suggest_next_nodes(context, top_k=5)

# Semantic suggestions
patterns = sem_guide.suggest_next(partial_code, top_k=3)

# Validation
valid, confidence, warnings = ast_guide.validate_sequence(ast_seq)

# Prompt enhancement
guidance = sem_guide.generate_prompt_guidance(partial_code)
```

---

## Performance Targets

| Metric                    | Target                                         | Status            |
|---------------------------|------------------------------------------------|-------------------|
| **Query Latency**         | <1ms (cached)                                  | ✓ Design goal     |
| **Throughput**            | >50K queries/sec                               | ✓ Design goal     |
| **Cache Hit Rate**        | >90%                                           | ✓ Design goal     |
| **Model Size (AST)**      | 10-50MB                                        | ✓ Typical         |
| **Model Size (Semantic)** | 1-10MB                                         | ✓ Typical         |
| **Training Speed**        | 1000 files/min (AST), 500 files/min (Semantic) | ✓ Design goal     |
| **Valid Code Generation** | 90-99%                                         | ✓ Post-validation |
| **Pattern Detection**     | 85-95%                                         | ✓ Design goal     |

---

## Success Criteria Summary

| Phase       | Criteria                                                   |
|-------------|------------------------------------------------------------|
| **Phase 1** | Train 1000+ files; Export valid models; >90% unit coverage |
| **Phase 2** | <1ms latency; >90% fallback success; 50%+ cache gain       |
| **Phase 3** | 1000 req/sec API; 95%+ valid code; <5 sec per function     |
| **Phase 4** | >95% test coverage; Complete docs; Examples work           |

---

## Implementation Order

```
Phase 1.1: ASTMarkovTrainer
    ↓
Phase 1.2: SemanticPatternExtractor
    ↓
Phase 1.3: SemanticMarkovTrainer + Phase 1.4: ModelTypes
    ↓
Phase 1 Testing & Validation ✓
    ↓
Phase 2.1: ASTCodeGuide
    ↓
Phase 2.2: SemanticCodeGuide
    ↓
Phase 2.3: Performance + Phase 2 Testing ✓
    ↓
Phase 3 (Advanced): API, Prompt Enhancement, Reference Agent
    ↓
Phase 4 (Polish): CLI, Tests, Docs
    ↓
Production Ready ✓
```

---

## Quick Wins / MVP Path

If you want something working quickly:

1. Implement Phase 1.1 (ASTMarkovTrainer) only
2. Implement Phase 2.1 (ASTCodeGuide) only
3. You have working syntax guidance system in ~1 week
4. Then add semantic layer (Phases 1.2-2.2) for full power

---

## Known Trade-offs

| Decision            | Pro                     | Con             | Mitigation                   |
|---------------------|-------------------------|-----------------|------------------------------|
| Two trainers        | Complementary, flexible | More code       | Clear separation of concerns |
| n-gram based        | Fast, interpretable     | Sparse states   | Fallback mechanisms          |
| Pre-exported models | Fast loading, no deps   | Hard to update  | Version management           |
| REST API            | Flexible, scalable      | Network latency | Optional, can skip Phase 3   |

---

## FAQ

**Q: Do I need both AST and semantic levels?**
A: No, start with semantic (higher-level) for better UX. Use AST as validation layer.

**Q: What's the minimum training data size?**
A: ~100-200 files gives reasonable model. Python stdlib (~1000 files) gives excellent results.

**Q: Can I add custom patterns?**
A: Yes, extend `CodePattern` enum in Phase 1.2 and add detection logic.

**Q: How do I integrate with my LLM?**
A: Three options: (1) Prompt enhancement (simplest), (2) Logit biasing (sophisticated), (3) REST API (most flexible).

**Q: What if code doesn't parse?**
A: Semantic guide has heuristic detection for incomplete code. AST guide validates only complete code.

**Q: How much does caching help?**
A: 50-100x speedup for repeated queries on common patterns (typical agent behavior).

---

## Critical Path

**Must Have**:
- Phase 1: Foundation (trainers + types)
- Phase 2.1-2.2: Query interfaces
- Basic tests

**Should Have**:
- Phase 2.3: Caching & optimization
- Comprehensive tests
- Documentation

**Nice to Have**:
- Phase 3: REST API, advanced features
- CLI tools
- Full examples

---

## Next Action Items

- [ ] Review this plan with team
- [ ] Confirm Phase 1.1 approach
- [ ] Set up git repo structure
- [ ] Create Phase 1 task breakdown
- [ ] Start implementation of ASTMarkovTrainer

---

**Document Version**: 1.0
**Last Updated**: 2026-02-08
**Status**: Ready for Development ✅
