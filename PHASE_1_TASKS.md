# Phase 1: Foundation Layer - Task Breakdown

**Status**: In Progress  
**Start Date**: 2026-02-08  
**Target Completion**: 2026-02-22  
**Effort**: 1-2 weeks (40-80 hours)

---

## Overview

Phase 1 implements the core trainers and data types that everything else depends on:
1. ASTMarkovTrainer (1.1)
2. SemanticPatternExtractor (1.2)
3. SemanticMarkovTrainer (1.3)
4. Model Types (1.4)

---

## Task Breakdown

### 1.1 ASTMarkovTrainer

#### 1.1.1 Setup & Project Structure
- [x] Create `src/trainers/` directory
- [x] Create `src/trainers/__init__.py`
- [x] Create `src/trainers/ast_trainer.py` stub
- [x] Create `tests/trainers/` directory
- [x] Create `tests/trainers/test_ast_trainer.py` stub
- [ ] Add imports and basic structure
- **Time**: 1-2 hours
- **Owner**: Developer 1
- **Blocking**: 1.1.2+

#### 1.1.2 AST Sequence Extraction
- [ ] Implement `extract_ast_sequence(node, parent_type)` method
  - [ ] DFS traversal of AST
  - [ ] Collect (parent_type, node_type) tuples
  - [ ] Handle nested structures
  - [ ] Unit tests for simple code snippets
- [ ] Implement `visit` pattern for different node types
- [ ] Handle edge cases (empty files, syntax errors)
- **Time**: 3-4 hours
- **Tests**: At least 10 test cases
- **Blocking**: 1.1.3

#### 1.1.3 Markov Chain Building
- [ ] Implement n-gram transition building
  - [ ] Order-1 (bigram): (state) → next_node
  - [ ] Order-2 (trigram): ((state1), (state2)) → next_node
  - [ ] Order-3 support
  - [ ] Proper Counter updates
- [ ] Implement `train_on_code(code: str)` method
  - [ ] Parse code to AST
  - [ ] Extract sequence
  - [ ] Build n-grams
  - [ ] Return success/failure
- [ ] Error handling for invalid Python
- [ ] Unit tests for transition building
- **Time**: 3-4 hours
- **Tests**: At least 15 test cases
- **Blocking**: 1.1.4

#### 1.1.4 File & Directory Training
- [ ] Implement `train_on_file(filepath)` method
  - [ ] Read file safely (encoding handling)
  - [ ] Call train_on_code()
  - [ ] Track success/failure
  - [ ] Handle file read errors
- [ ] Implement `train_on_directory(directory, recursive=True)` method
  - [ ] Glob for *.py files
  - [ ] Process files with progress tracking
  - [ ] Print statistics
  - [ ] Handle missing directories
- [ ] Progress reporting (every 100 files)
- [ ] Error logging
- **Time**: 2-3 hours
- **Tests**: Integration tests with real files
- **Blocking**: 1.1.5

#### 1.1.5 Probability Computation & Export
- [ ] Implement `get_probabilities(min_count: int)` method
  - [ ] Filter rare transitions (< min_count)
  - [ ] Normalize to probabilities
  - [ ] Return clean dict
- [ ] Implement `export_to_python(output_path, min_count)` method
  - [ ] Generate valid Python code
  - [ ] Include transitions dict
  - [ ] Include probabilities dict
  - [ ] Include helper functions
  - [ ] Include metadata
  - [ ] Proper formatting and comments
- [ ] Implement `export_to_json(output_path, min_count)` method
  - [ ] Serialize to JSON format
  - [ ] Handle tuple key conversion
  - [ ] Pretty printing
- [ ] Verify exported models are valid Python/JSON
- **Time**: 3-4 hours
- **Tests**: Export validation tests
- **Blocking**: 1.1.6

#### 1.1.6 CLI Interface & Testing
- [ ] Implement `main()` function for CLI
  - [ ] argparse setup
  - [ ] Input validation
  - [ ] Output handling
  - [ ] Error messages
- [ ] Make script executable
- [ ] Test with real Python files
- [ ] Full integration test on stdlib subset
- [ ] Performance baseline test
- **Time**: 2-3 hours
- **Tests**: CLI tests, stdlib test
- **Status**: Ready for testing

**1.1 Subtotal**: ~18-25 hours

---

### 1.2 SemanticPatternExtractor

#### 1.2.1 Setup & CodePattern Enum
- [ ] Create `src/trainers/semantic_pattern_extractor.py`
- [ ] Define `CodePattern` enum with 50 patterns
  - [ ] Control flow patterns (5)
  - [ ] Loop patterns (6)
  - [ ] Return patterns (5)
  - [ ] Data structure patterns (8)
  - [ ] Error handling patterns (5)
  - [ ] Function/class patterns (6)
  - [ ] Comprehension patterns (3)
  - [ ] API patterns (3)
  - [ ] Other idioms (8)
- [ ] Create tests stub
- **Time**: 2-3 hours
- **Blocking**: 1.2.2

#### 1.2.2 If Statement Classification
- [ ] Implement `_classify_if_statement(node)` method
  - [ ] None checks (is None, is not None)
  - [ ] Empty checks (not x, len(x) == 0)
  - [ ] Type checks (isinstance)
  - [ ] Guard clauses (early return)
  - [ ] Default fallthrough
- [ ] Test with 20+ if-statement examples
- [ ] Handle edge cases
- **Time**: 3-4 hours
- **Tests**: Comprehensive if-statement tests

#### 1.2.3 Loop Pattern Classification
- [ ] Implement `_classify_loop(node)` method
  - [ ] Loop purpose detection
    - [ ] Accumulation (+=, -=)
    - [ ] Transformation (.append on new list)
    - [ ] Filtering (.append with if condition)
  - [ ] Special loop types
    - [ ] enumerate() pattern
    - [ ] zip() pattern
    - [ ] dict.items() pattern
- [ ] Test with 20+ loop examples
- **Time**: 3-4 hours
- **Tests**: Comprehensive loop tests

#### 1.2.4 Other Statement Classifications
- [ ] Implement `_classify_return(node)` method
  - [ ] Return None
  - [ ] Return bool
  - [ ] Return list
  - [ ] Return dict
  - [ ] Return computed value
- [ ] Implement `_classify_assignment(node)` method
  - [ ] Empty list init
  - [ ] Empty dict init
  - [ ] Counter init (= 0)
  - [ ] dict.get() with default
  - [ ] Other patterns
- [ ] Implement `_classify_try_except(node)` method
  - [ ] try-except-pass
  - [ ] try-except-log
  - [ ] try-except-raise
  - [ ] try-finally
- [ ] Implement `_classify_function(node)` method
  - [ ] Validator (early returns)
  - [ ] Transformer (param → return)
  - [ ] Decorators (property, classmethod, staticmethod)
  - [ ] __init__ method
- **Time**: 4-5 hours
- **Tests**: 30+ classification tests

#### 1.2.5 SemanticPatternAnalyzer AST Visitor
- [ ] Implement `SemanticPatternAnalyzer(ast.NodeVisitor)`
  - [ ] `__init__()` - initialize pattern list
  - [ ] `visit_FunctionDef(node)` - function analysis
  - [ ] `visit_If(node)` - if classification
  - [ ] `visit_For(node)` - loop classification
  - [ ] `visit_Return(node)` - return classification
  - [ ] `visit_Assign(node)` - assignment classification
  - [ ] `visit_Try(node)` - try-except classification
  - [ ] `visit_With(node)` - context manager
- [ ] Proper visitor pattern
- [ ] Context tracking (in function, nested, etc.)
- **Time**: 4-5 hours
- **Tests**: Full AST visitor tests

#### 1.2.6 Testing & Validation
- [ ] Test all 50 patterns individually
- [ ] Test pattern sequences (multi-pattern files)
- [ ] Test edge cases (empty code, incomplete code)
- [ ] Test nested structures
- [ ] Performance baseline (speed of detection)
- **Time**: 3-4 hours
- **Tests**: 50+ pattern detection tests
- **Status**: Ready for semantic trainer

**1.2 Subtotal**: ~24-30 hours

---

### 1.3 SemanticMarkovTrainer

#### 1.3.1 Trainer Implementation
- [ ] Create `src/trainers/semantic_trainer.py`
- [ ] Implement `SemanticMarkovTrainer` class
  - [ ] `__init__(order: int)`
  - [ ] `train_on_code(code: str)` method
    - [ ] Use SemanticPatternAnalyzer
    - [ ] Extract pattern sequence
    - [ ] Build n-grams
    - [ ] Update transitions
  - [ ] `train_on_file(filepath)` method
  - [ ] `train_on_directory(directory, recursive)` method
- **Time**: 2-3 hours
- **Blocking**: 1.3.2

#### 1.3.2 Export & Statistics
- [ ] Implement probability computation
- [ ] Implement `export_to_python(output_path, min_count)` method
  - [ ] Generate CodePattern enum
  - [ ] Export transitions dict
  - [ ] Export probabilities dict
  - [ ] Include helper functions
  - [ ] Include metadata
  - [ ] Proper formatting
- [ ] Implement `print_statistics()` method
  - [ ] Most common patterns
  - [ ] Most common pattern sequences
  - [ ] Pattern co-occurrence analysis
- **Time**: 2-3 hours
- **Tests**: Export validation, statistics sanity checks

#### 1.3.3 Testing
- [ ] Test on sample code
- [ ] Test on stdlib subset
- [ ] Verify statistics are reasonable
- [ ] Check exported model is valid Python
- [ ] Performance baseline
- **Time**: 2-3 hours
- **Tests**: Integration tests
- **Status**: Ready for model types

**1.3 Subtotal**: ~6-9 hours

---

### 1.4 Model Types / Interfaces

#### 1.4.1 Data Classes
- [ ] Create `src/interfaces/model_types.py`
- [ ] Implement `NextNodeSuggestion` dataclass
  - [ ] node_type: str
  - [ ] probability: float
  - [ ] confidence: str
  - [ ] common_patterns: List[str]
- [ ] Implement `NextPatternSuggestion` dataclass
  - [ ] pattern: CodePattern
  - [ ] probability: float
  - [ ] description: str
  - [ ] code_template: str
  - [ ] confidence: str
- [ ] Implement `ASTContext` dataclass
  - [ ] parent_type: str
  - [ ] current_node: str
  - [ ] ancestor_chain: List[str]
  - [ ] `to_state(order: int) -> Tuple` method
- [ ] Implement `ValidationResult` dataclass
  - [ ] is_valid: bool
  - [ ] confidence_score: float
  - [ ] warnings: List[str]
- [ ] Implement `SemanticNode` dataclass (for trainer)
  - [ ] pattern: CodePattern
  - [ ] context: Dict
- **Time**: 1-2 hours
- **Tests**: Dataclass tests, conversion tests

#### 1.4.2 Tests
- [ ] Unit tests for all dataclasses
- [ ] Test instantiation
- [ ] Test conversions
- [ ] Test edge cases
- **Time**: 1 hour
- **Tests**: 10+ dataclass tests
- **Status**: Ready for use

**1.4 Subtotal**: ~2-3 hours

---

## Testing Strategy (Cross-Cutting)

### Unit Testing
- [ ] Test each method individually
- [ ] Use pytest framework
- [ ] Aim for >90% code coverage
- [ ] Test error cases
- **Time**: Included in each task

### Integration Testing
- [ ] Test trainer → model → load cycle
- [ ] Test on Python stdlib subset
- [ ] Verify model quality (statistics)
- [ ] Performance baseline
- **Time**: 2-3 hours (separate)

### Performance Testing
- [ ] Measure training speed (files/min)
- [ ] Measure export time
- [ ] Measure memory usage
- [ ] Baseline for comparison
- **Time**: 1 hour

---

## File Checklist

By end of Phase 1, should have:

### Source Files
- [ ] `src/__init__.py`
- [ ] `src/trainers/__init__.py`
- [ ] `src/trainers/ast_trainer.py` ✅ (DONE)
- [ ] `src/trainers/semantic_pattern_extractor.py` ✅ (DONE)
- [ ] `src/trainers/semantic_trainer.py` ✅ (DONE)
- [ ] `src/interfaces/__init__.py`
- [ ] `src/interfaces/model_types.py` ✅ (DONE)

### Test Files
- [ ] `tests/__init__.py`
- [ ] `tests/conftest.py` (pytest fixtures)
- [ ] `tests/trainers/__init__.py`
- [ ] `tests/trainers/test_ast_trainer.py`
- [ ] `tests/trainers/test_semantic_extractor.py`
- [ ] `tests/trainers/test_semantic_trainer.py`
- [ ] `tests/interfaces/__init__.py`
- [ ] `tests/interfaces/test_model_types.py`
- [ ] `tests/integration/` directory
- [ ] `tests/integration/test_training_pipeline.py`

### Configuration Files
- [ ] `pytest.ini` or `pyproject.toml` with pytest config
- [ ] `.gitignore` (exclude __pycache__, *.pyc, model files, etc.)
- [ ] `requirements.txt` or `pyproject.toml` with dependencies

---

## Quality Gates

Before moving to Phase 2, must have:

- [ ] All unit tests passing (>90% coverage)
- [ ] Integration tests passing
- [ ] Successfully train on 100+ files
- [ ] Export valid, executable Python models
- [ ] No blocking bugs
- [ ] Performance baseline established
- [ ] Code review passed
- [ ] Documentation complete (docstrings in code)

---

## Dependencies

### External
- Python 3.8+ (ast module)
- pytest (testing)
- No other external dependencies for Phase 1

### Internal
- None (Phase 1 is foundational)

---

## Blockers & Risks

| Risk | Severity | Mitigation |
|------|----------|-----------|
| Pattern detection too complex | Medium | Start simple, iterate; can add more patterns later |
| Sparse state space | Low | Expected; Phase 2 has fallback mechanisms |
| Memory for large models | Low | Optimize later if needed; Phase 1 just trains |
| Testing difficult on incomplete code | Medium | Focus on complete code first; incomplete handling in Phase 2 |

---

## Time Estimates Summary

| Task | Hours | Owner | Status |
|------|-------|-------|--------|
| 1.1 ASTMarkovTrainer | 18-25 | Dev1 | Starting |
| 1.2 SemanticPatternExtractor | 24-30 | Dev2 | Starting |
| 1.3 SemanticMarkovTrainer | 6-9 | Dev1 | Depends on 1.2 |
| 1.4 Model Types | 2-3 | Dev1 | Starting |
| Integration Testing | 2-3 | QA | After all |
| **Total Phase 1** | **52-70** | - | **1-2 weeks** |

---

## Daily Standup Template

Use this for quick status updates:

```
Date: [DATE]

1.1 ASTMarkovTrainer: [STATUS]
  - Completed: [TASKS]
  - In Progress: [CURRENT]
  - Blockers: [ISSUES]

1.2 SemanticPatternExtractor: [STATUS]
  - Completed: [TASKS]
  - In Progress: [CURRENT]
  - Blockers: [ISSUES]

1.3 SemanticMarkovTrainer: [STATUS]
  - Completed: [TASKS]
  - In Progress: [CURRENT]
  - Blockers: [ISSUES]

1.4 Model Types: [STATUS]
  - Completed: [TASKS]
  - In Progress: [CURRENT]
  - Blockers: [ISSUES]

Next: [TOMORROW'S FOCUS]
```

---

## Success Criteria

### By End of Phase 1.1
- [x] ASTMarkovTrainer working
- [x] Trains on 100+ files successfully
- [x] Exports valid Python model
- [x] >90% test coverage

### By End of Phase 1.2
- [x] SemanticPatternExtractor identifies 50+ patterns
- [x] Accuracy 85%+ on test code
- [x] Handles edge cases
- [x] >90% test coverage

### By End of Phase 1.3
- [x] SemanticMarkovTrainer working
- [x] Trains on 100+ files
- [x] Exports valid Python model
- [x] Statistics are reasonable

### By End of Phase 1.4
- [x] All dataclasses defined
- [x] Conversions working
- [x] Used by Phase 2 (preparation)

### Overall Phase 1
- [x] 4-8 integrated trainers complete
- [x] >90% code coverage across all modules
- [x] Integration test suite passing
- [x] Performance baselines established
- [x] Ready for Phase 2

---

## Next Phase Preparation

As Phase 1 completes:

- [ ] Review Phase 2 requirements
- [ ] Start Phase 2.1 design
- [ ] Prepare test models from Phase 1 trainers
- [ ] Document Phase 1 findings
- [ ] Get feedback on approach

---

**Status**: Ready to begin  
**Last Updated**: 2026-02-08  
**Next Update**: Daily standup
