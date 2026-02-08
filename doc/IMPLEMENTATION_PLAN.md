# Marky: Implementation Plan for Trainers & Helpers

Based on `primer.md`, this document outlines the complete implementation roadmap for the Markov chain training system, including both AST-level and semantic-level trainers, along with their supporting infrastructure.

## Phase Overview

**Phase 1: Foundation (Core Trainers)**
- AST Markov Trainer
- Semantic Pattern Extractor & Trainer
- Base model interfaces

**Phase 2: Agent Integration (High-Performance Interfaces)**
- AST-level code guide
- Semantic-level code guide
- Caching & performance optimization

**Phase 3: Advanced Features**
- Pattern chain generation
- Real-time streaming validation
- REST API service
- Prompt enhancement system

**Phase 4: Polish & Utilities**
- Benchmarking tools
- CLI enhancements
- Documentation & examples

---

## Phase 1: Foundation Layer

### 1.1 Core Module: AST Markov Trainer

**File**: `src/trainers/ast_trainer.py`

**Responsibilities**:
- Parse Python files into AST
- Extract node type transition sequences
- Build n-gram models (order 1, 2, 3)
- Compute transition probabilities
- Export models to Python code

**Key Classes**:
```python
class ASTMarkovTrainer:
    - __init__(order: int)
    - extract_ast_sequence(node, parent_type) -> List[Tuple]
    - train_on_code(code: str) -> bool
    - train_on_file(filepath: Path) -> bool
    - train_on_directory(dir: Path, recursive: bool)
    - get_probabilities(min_count: int) -> Dict
    - export_to_python(output_path, min_count)
    - export_to_json(output_path, min_count)
```

**Expected Outputs**:
- `ast_markov_model.py` - Executable model with transitions, probabilities, helper functions
- Optional JSON variant for interoperability

**Testing**:
- Unit tests for AST extraction (simple code snippets)
- Integration test: train on stdlib subset, verify output structure

---

### 1.2 Core Module: Semantic Pattern Extractor

**File**: `src/trainers/semantic_pattern_extractor.py`

**Responsibilities**:
- Define semantic pattern taxonomy
- Detect high-level patterns in AST (if-not-none, loop-filter, etc.)
- Classify functions by type
- Extract pattern sequences from code

**Key Components**:

```python
class CodePattern(Enum):
    # ~50 semantic patterns organized by category:
    # - Control flow (IF_NOT_NONE, GUARD_CLAUSE, etc.)
    # - Loop patterns (LOOP_FILTER, LOOP_TRANSFORM, etc.)
    # - Return patterns (RETURN_LIST, RETURN_COMPUTED, etc.)
    # - Data structure patterns (INIT_EMPTY_LIST, APPEND_TO_LIST, etc.)
    # - Error handling (TRY_EXCEPT_PASS, CONTEXT_MANAGER, etc.)
    # - Class patterns (INIT_METHOD, PROPERTY_GETTER, etc.)
    # - API patterns (API_VALIDATION, API_ERROR_RESPONSE, etc.)

class SemanticPatternAnalyzer(ast.NodeVisitor):
    - visit_FunctionDef(node)
    - visit_If(node)
    - visit_For(node)
    - visit_Return(node)
    - visit_Assign(node)
    - visit_Try(node)
    - visit_With(node)
    - _classify_function(node) -> CodePattern
    - _classify_if_statement(node) -> CodePattern
    - _classify_loop(node) -> CodePattern
    - _classify_return(node) -> CodePattern
    - _classify_assignment(node) -> CodePattern
    - _classify_try_except(node) -> CodePattern
```

**Expected Outputs**:
- `SemanticPatternAnalyzer` ready for use by semantic trainer
- Comprehensive pattern detection covering ~50 semantic patterns

**Testing**:
- Pattern detection tests for each code pattern type
- Edge cases: incomplete code, nested structures

---

### 1.3 Core Module: Semantic Markov Trainer

**File**: `src/trainers/semantic_trainer.py`

**Responsibilities**:
- Use `SemanticPatternAnalyzer` to extract patterns
- Build Markov chains over semantic patterns
- Handle n-gram transitions at semantic level
- Export semantic models

**Key Classes**:
```python
class SemanticMarkovTrainer:
    - __init__(order: int)
    - train_on_code(code: str) -> bool
    - train_on_file(filepath: Path) -> bool
    - train_on_directory(dir: Path, recursive: bool)
    - get_probabilities(min_count: int) -> Dict
    - export_to_python(output_path, min_count)
    - print_statistics()
```

**Expected Outputs**:
- `semantic_model.py` - Executable model with pattern transitions, probabilities, helper functions
- Statistics printout showing most common patterns & sequences

**Testing**:
- Integration test: train on python standard library
- Verify statistics match expected patterns

---

### 1.4 Data Structures: Model Interfaces

**File**: `src/interfaces/model_types.py`

**Responsibilities**:
- Define common interfaces for both trainer outputs
- Standardize model loading and querying

**Key Types**:
```python
@dataclass
class NextNodeSuggestion:
    node_type: str
    probability: float
    confidence: str  # 'high', 'medium', 'low'
    common_patterns: List[str]

@dataclass
class NextPatternSuggestion:
    pattern: CodePattern
    probability: float
    description: str
    code_template: str
    confidence: str

@dataclass
class ASTContext:
    parent_type: str
    current_node: str
    ancestor_chain: List[str]
    
    def to_state(self, order: int) -> Tuple

@dataclass
class ValidationResult:
    is_valid: bool
    confidence_score: float
    warnings: List[str]
```

**Testing**:
- Dataclass instantiation tests
- State conversion tests (to_state method)

---

## Phase 2: Agent Integration Layer

### 2.1 AST Code Guide (Agent Interface)

**File**: `src/guides/ast_code_guide.py`

**Responsibilities**:
- High-performance query interface for AST model
- Fast lookups with caching
- Fallback mechanisms
- Temperature-based sampling
- Logit biasing for LLMs

**Key Classes**:
```python
class MarkovCodeGuide:
    - __init__(model_module)
    - _build_indices()  # Pre-compute lookups
    - suggest_next_nodes(context, top_k, temperature) -> List[NextNodeSuggestion]
    - _fallback_suggestions(context, top_k) -> List
    - _apply_temperature(probs, temperature) -> Dict
    - validate_sequence(ast_sequence) -> (bool, float, List[str])
    - get_completion_candidates(partial_code, cursor_position) -> List
    - _extract_context_from_ast(tree) -> ASTContext
    - _suggest_from_incomplete_code(partial_code) -> List
    - bias_logits(llm_logits, token_to_ast_map, context, bias_strength) -> ndarray

class CachedMarkovGuide(MarkovCodeGuide):
    - _prewarm_cache()
    - _cached_suggest(state_tuple) -> Tuple
    - suggest_next_nodes(...)  # Cached version

class StreamingCodeValidator:
    - add_token(token) -> (bool, Optional[str])
    - get_next_suggestions(top_k) -> List[str]
```

**Convenience Functions**:
- `quick_suggest(model_module, partial_code, top_k)` → List[str]
- `validate_generated_code(model_module, code)` → (bool, float, List[str])

**Testing**:
- Suggestion accuracy tests
- Cache hit rate verification
- Temperature scaling tests
- Fallback mechanism tests

---

### 2.2 Semantic Code Guide (Agent Interface)

**File**: `src/guides/semantic_code_guide.py`

**Responsibilities**:
- High-level semantic guidance for agents
- Pattern templates for code generation
- Natural language guidance generation
- Pattern-driven code completion

**Key Classes**:
```python
class SemanticCodeGuide:
    - __init__(model_module)
    - _build_templates() -> Dict[CodePattern, str]
    - analyze_partial_code(code: str) -> List[CodePattern]
    - _parse_incomplete(code: str) -> List[CodePattern]
    - suggest_next(partial_code, top_k, context_hint) -> List[PatternSuggestion]
    - _get_default_suggestions() -> List
    - generate_prompt_guidance(partial_code) -> str
    - complete_with_pattern(partial_code, pattern, **template_vars) -> str

class PatternChainGenerator:
    - __init__(model_module)
    - generate_function_scaffold(function_name, purpose, params) -> str
    - _generate_pattern_code(pattern, params) -> str
```

**Convenience Functions**:
- `quick_suggest_patterns(model_module, partial_code)` → List[str]

**Testing**:
- Pattern detection from partial code
- Template instantiation with various parameters
- Prompt guidance generation
- Pattern chain generation

---

### 2.3 Performance Optimization

**File**: `src/guides/performance.py`

**Responsibilities**:
- Caching layer for both guides
- Pre-warming cache with common patterns
- Benchmarking utilities

**Key Classes**:
```python
class CachedMarkovGuide:  # Already defined above
    pass

class MarkovBenchmark:
    - benchmark_lookup_speed(guide, n_queries) -> None
    - benchmark_validation(guide, test_codes) -> None
```

**Target Performance**:
- Lookup latency: <1ms per query (cached)
- Memory footprint: ~10-50MB for typical model
- Throughput: >50K queries/second on single core

**Testing**:
- Benchmark suite that validates performance targets

---

## Phase 3: Advanced Features

### 3.1 REST API Service

**File**: `src/api/markov_service.py`

**Responsibilities**:
- HTTP interface for remote agents
- Support for both AST and semantic models
- Health checks and monitoring

**Endpoints**:
```python
POST /ast/suggest
    Request: {"partial_code": str, "top_k": int}
    Response: {"suggestions": [...]}

POST /ast/validate
    Request: {"code": str}
    Response: {"valid": bool, "confidence": float, "warnings": [...]}

POST /semantic/suggest
    Request: {"partial_code": str, "top_k": int}
    Response: {"suggestions": [...]}

POST /semantic/complete
    Request: {"partial_code": str, "pattern": str, "template_vars": {...}}
    Response: {"completed_code": str}

GET /health
    Response: {"status": str, "ast_model_states": int, "semantic_states": int}
```

**Testing**:
- Integration tests with HTTP client
- Load testing
- Error handling tests

---

### 3.2 Prompt Enhancement System

**File**: `src/prompt_engineering/enhancer.py`

**Responsibilities**:
- Enhance prompts with structural/semantic guidance
- Multi-strategy enhancement

**Key Classes**:
```python
class ASTPromptEnhancer:
    - enhance_prompt(base_prompt, partial_code) -> str

class SemanticPromptEnhancer:
    - enhance_prompt(base_prompt, partial_code) -> str
```

**Testing**:
- Guidance quality tests
- Prompt size impact tests

---

### 3.3 Semantic Coding Agent (Reference Implementation)

**File**: `src/agents/semantic_coding_agent.py`

**Responsibilities**:
- Full end-to-end example of agent using semantic guidance
- Iterative refinement loop
- Intent extraction

**Key Classes**:
```python
class SemanticCodingAgent:
    - __init__(semantic_model, llm_client)
    - generate_function(spec: str) -> str
    - _extract_intent(spec: str) -> dict
```

**Testing**:
- End-to-end generation tests with mock LLM
- Output code validation

---

## Phase 4: Polish & Utilities

### 4.1 Enhanced CLI Tools

**File**: `src/cli/train_command.py`, `src/cli/analyze_command.py`

**Responsibilities**:
- CLI for training both AST and semantic models
- Analysis and statistics tools

**Commands**:
```bash
markymarkov train --type ast --input <path> --output model.py --order 2
markymarkov train --type semantic --input <path> --output model.py --order 2
markymarkov analyze <model.py> --top-patterns 20
markymarkov benchmark <model.py> --queries 10000
```

**Testing**:
- CLI invocation tests
- Output file validation
- Error handling tests

---

### 4.2 Comprehensive Test Suite

**File**: `tests/`

**Coverage Areas**:
```
tests/
├── trainers/
│   ├── test_ast_trainer.py
│   ├── test_semantic_extractor.py
│   └── test_semantic_trainer.py
├── guides/
│   ├── test_ast_code_guide.py
│   ├── test_semantic_code_guide.py
│   └── test_performance.py
├── api/
│   └── test_markov_service.py
├── agents/
│   └── test_semantic_coding_agent.py
└── integration/
    └── test_end_to_end.py
```

**Test Types**:
- Unit tests for each module
- Integration tests for trainer → model → guide pipelines
- Performance tests for caching/optimization
- End-to-end tests for agent scenarios

---

### 4.3 Documentation & Examples

**Files**:
- `docs/ARCHITECTURE.md` - System design overview
- `docs/API_REFERENCE.md` - Complete API documentation
- `docs/USAGE_GUIDE.md` - How to use for different scenarios
- `examples/train_from_stdlib.py` - Example: training on Python stdlib
- `examples/agent_integration.py` - Example: integrating with LLM agent
- `examples/custom_patterns.py` - Example: defining custom patterns

---

## Implementation Dependency Graph

```
Phase 1: Foundation
├── 1.1 ASTMarkovTrainer ✓ (independent)
├── 1.2 SemanticPatternExtractor ✓ (depends on ast module only)
├── 1.3 SemanticMarkovTrainer (depends on 1.2)
└── 1.4 Model Types (independent)

Phase 2: Agent Integration
├── 2.1 ASTCodeGuide (depends on 1.1, 1.4)
├── 2.2 SemanticCodeGuide (depends on 1.3, 1.2, 1.4)
├── 2.3 Performance (depends on 2.1, 2.2)
└── Phase 2 ✓ (all tests must pass)

Phase 3: Advanced Features
├── 3.1 REST API (depends on Phase 2)
├── 3.2 Prompt Enhancement (depends on Phase 2)
├── 3.3 Semantic Coding Agent (depends on Phase 3.2)
└── Phase 3 ✓ (all tests must pass)

Phase 4: Polish
├── 4.1 CLI Tools (depends on Phase 1 & 2)
├── 4.2 Full Test Suite (comprehensive coverage)
└── 4.3 Documentation
```

---

## File Structure

```
markymarkov/
├── src/
│   ├── trainers/
│   │   ├── __init__.py
│   │   ├── ast_trainer.py           [Phase 1.1]
│   │   ├── semantic_pattern_extractor.py  [Phase 1.2]
│   │   └── semantic_trainer.py       [Phase 1.3]
│   ├── interfaces/
│   │   ├── __init__.py
│   │   └── model_types.py            [Phase 1.4]
│   ├── guides/
│   │   ├── __init__.py
│   │   ├── ast_code_guide.py         [Phase 2.1]
│   │   ├── semantic_code_guide.py    [Phase 2.2]
│   │   └── performance.py            [Phase 2.3]
│   ├── api/
│   │   ├── __init__.py
│   │   └── markov_service.py         [Phase 3.1]
│   ├── prompt_engineering/
│   │   ├── __init__.py
│   │   └── enhancer.py               [Phase 3.2]
│   ├── agents/
│   │   ├── __init__.py
│   │   └── semantic_coding_agent.py  [Phase 3.3]
│   └── cli/
│       ├── __init__.py
│       ├── train_command.py          [Phase 4.1]
│       └── analyze_command.py        [Phase 4.1]
├── tests/
│   ├── trainers/
│   ├── guides/
│   ├── api/
│   ├── agents/
│   └── integration/
├── docs/
│   ├── ARCHITECTURE.md               [Phase 4.3]
│   ├── API_REFERENCE.md              [Phase 4.3]
│   └── USAGE_GUIDE.md                [Phase 4.3]
├── examples/
│   ├── train_from_stdlib.py          [Phase 4.3]
│   ├── agent_integration.py          [Phase 4.3]
│   └── custom_patterns.py            [Phase 4.3]
└── README.md
```

---

## Success Criteria

### Phase 1
- [ ] AST trainer can parse 1000+ Python files
- [ ] Semantic extractor identifies 40+ pattern types
- [ ] Both trainers export valid, executable Python modules
- [ ] Unit test coverage >90%

### Phase 2
- [ ] Both guides achieve <1ms lookup latency (cached)
- [ ] Fallback mechanisms handle 95%+ of unknown states
- [ ] Caching improves performance by 50%+ vs uncached
- [ ] Temperature sampling produces diverse yet valid outputs

### Phase 3
- [ ] REST API handles 1000 requests/second
- [ ] Prompt enhancement improves agent generation quality (validated manually)
- [ ] Semantic agent generates syntactically valid code 95%+ of the time
- [ ] End-to-end loop completes in <5 seconds per function

### Phase 4
- [ ] CLI tools have intuitive interfaces
- [ ] Full test suite passes (>95% coverage)
- [ ] Documentation is complete and examples run without modification
- [ ] Ready for production use

---

## Notes & Considerations

### Design Decisions
1. **Two separate trainers**: AST and semantic provide complementary benefits
2. **Order flexibility**: Support order 1, 2, 3 for different accuracy/size tradeoffs
3. **Fallback mechanisms**: Essential for agent reliability
4. **Caching**: Pre-warm with common patterns for predictable latency
5. **REST API**: Allow agents to run independently with remote model service

### Potential Extensions
- Custom pattern definitions per domain
- Multi-language support (go, typescript, rust, etc.)
- Real-time model updates as agent learns
- Confidence-weighted LLM biasing
- Pattern weighting by code quality signals (stars, test coverage, etc.)

### Known Challenges
- Pattern detection accuracy (will improve with more training data)
- Memory usage for large models (consider quantization)
- Handling edge cases in incomplete code
- Fallback behavior when model state space is sparse

---

## Next Steps
1. Start with Phase 1.1: Implement ASTMarkovTrainer
2. Validate on stdlib subset
3. Proceed to Phase 1.2-1.4 in parallel
4. Comprehensive Phase 1 testing before Phase 2
5. Iterative development with real-world testing throughout
