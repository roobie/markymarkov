# Test Status Report

## Summary
- **Total**: 170 tests
- **Passing**: 164 (96.5%)
- **Failing**: 6 (3.5%)
- **Warnings**: 27 (deprecation warnings in semantic extractor)

## Test Breakdown by Module

### ✅ Phase 2 Guides (All Passing)
- `tests/guides/test_ast_code_guide.py`: **34/34 PASS**
  - MarkovCodeGuide
  - CachedMarkovCodeGuide
  - StreamingCodeValidator
  - Integration tests
  - Edge cases

### ✅ Model Types & Interfaces (All Passing)
- `tests/interfaces/test_model_types.py`: **52/52 PASS**
  - NextNodeSuggestion
  - NextPatternSuggestion
  - ASTContext
  - ValidationResult
  - SemanticNode
  - Integration scenarios

### ✅ Phase 1.1 AST Trainer (All Passing)
- `tests/trainers/test_ast_trainer.py`: **36/36 PASS**
  - Initialization
  - Sequence extraction
  - Markov transition extraction
  - Export functionality
  - Full training pipeline

### ⚠️ Phase 1.2 Semantic Extractor (6 Failures - Pre-existing)
- `tests/trainers/test_semantic_extractor.py`: **66/72 PASS, 6 FAIL**
  - ❌ test_if_not_none - Pattern detector bug
  - ❌ test_return_none - Pattern detector bug
  - ❌ test_return_bool - Pattern detector bug
  - ❌ test_unpacking - Pattern detector bug
  - ❌ test_logging_call - Pattern detector bug
  - ❌ test_error_handling_function - Pattern detector bug

## Pre-existing Failures

These 6 test failures are **NOT caused by recent CLI validation changes**. They are pre-existing bugs in the semantic pattern detector:

1. **test_if_not_none**: Pattern detector doesn't recognize `if x is not None` pattern
2. **test_return_none**: Pattern detector doesn't recognize simple `return None`
3. **test_return_bool**: Pattern detector doesn't recognize `return True/False`
4. **test_unpacking**: Pattern detector doesn't recognize tuple unpacking
5. **test_logging_call**: Pattern detector doesn't recognize logging calls
6. **test_error_handling_function**: Pattern detector doesn't recognize try/except patterns

All failures are in the semantic pattern *detection* logic, not in:
- AST model validation ✅
- Semantic model validation ✅
- CLI commands ✅
- Guide interfaces ✅
- Model types ✅

## CLI Validation Tests

New semantic validation code has been tested manually:
- ✅ AST model validation works correctly
- ✅ Semantic model validation works correctly
- ✅ Auto-detection of model type works
- ✅ Enum conversion for patterns works
- ✅ Confidence scoring works
- ✅ Error reporting works

## Impact Assessment

**My CLI Changes Impact**: ZERO test regressions
- All previously passing tests still pass (164)
- All new validation code works correctly
- No breaking changes to existing APIs

**Semantic Extractor Issues**: Pre-existing, not caused by recent work
- These bugs exist in the pattern detection logic
- Not in the trainer or validator
- Can be fixed separately in Phase 3

## Recommendation

✅ **Safe to proceed** - No test regressions from CLI validation work. The 6 failing tests are pre-existing bugs that should be addressed in a future phase focused on improving the semantic pattern detector.

See [PHASE_2_2_VALIDATION_COMPLETE.md](./PHASE_2_2_VALIDATION_COMPLETE.md) for detailed validation implementation notes.
