# Phase 2: Agent Integration Layer Specification

**Status**: Ready to Start (Phase 1 Complete ✅)  
**Estimated Duration**: 1-2 weeks  
**Estimated Effort**: 40-60 hours  
**Target Completion**: 3 weeks from start  

---

## Overview

Phase 2 transforms the foundation (Phase 1) into **practical query interfaces** for LLM agents.

### High-Level Goal
Build query guides that agents can use to:
1. Get suggestions for next code elements
2. Validate code patterns
3. Complete partial code
4. Generate better code with model guidance

---

## What Phase 2 Delivers

### Two Query Guides

| Guide | Purpose | Model | Input | Output |
|-------|---------|-------|-------|--------|
| **ASTCodeGuide** | Syntactic suggestions | AST Model | AST Context | NextNodeSuggestion list |
| **SemanticCodeGuide** | Behavioral suggestions | Pattern Model | Partial code | NextPatternSuggestion list |

### Key Features

✅ **High Performance**:
- <1ms query latency
- Caching layer for frequent queries
- Pre-computed indices

✅ **Agent-Friendly**:
- Easy-to-use APIs
- Temperature-based sampling
- Logit biasing for LLMs
- Fallback mechanisms

✅ **Production-Ready**:
- Comprehensive error handling
- Validation of results
- Streaming support
- Statistics tracking

---

## 2.1 ASTCodeGuide - Syntactic Analysis

**File**: `src/guides/ast_code_guide.py`

### Purpose
Query AST Markov models to suggest next syntactic elements (AST node types).

### Use Cases

**1. Syntax Validation**
```python
guide = ASTCodeGuide(ast_model)
is_valid = guide.validate_sequence(['FunctionDef', 'Assign', 'Return'])
```

**2. Code Completion**
```python
# Agent has written partial code
partial_ast = extract_ast(partial_code)
suggestions = guide.suggest_next_nodes(partial_ast, top_k=5)
# Returns: [NextNodeSuggestion('Return', 0.65, 'HIGH'), ...]
```

**3. Guided Code Generation**
```python
# Bias LLM logits based on model suggestions
logit_biases = guide.bias_logits(llm_output, context)
```

### Key Classes

#### MarkovCodeGuide (Base)

```python
class MarkovCodeGuide:
    """High-performance AST model query interface."""
    
    def __init__(self, model_module: types.ModuleType):
        """Load a pre-trained AST model."""
        self.model = model_module
        self._build_indices()
    
    def suggest_next_nodes(
        self, 
        context: ASTContext, 
        top_k: int = 5,
        temperature: float = 1.0,
        min_confidence: str = 'MEDIUM'
    ) -> List[NextNodeSuggestion]:
        """
        Suggest next AST node types.
        
        Args:
            context: Current position in AST
            top_k: Number of suggestions
            temperature: Sampling temperature (0=deterministic, 1=uniform)
            min_confidence: Filter by confidence level
        
        Returns:
            Sorted list of NextNodeSuggestion
        """
    
    def validate_sequence(
        self, 
        nodes: List[str]
    ) -> ValidationResult:
        """
        Validate an AST node sequence.
        
        Returns:
            ValidationResult with confidence score and issues
        """
    
    def bias_logits(
        self,
        llm_logits: np.ndarray,
        token_to_ast_map: Dict[str, str],
        context: ASTContext,
        bias_strength: float = 0.5
    ) -> np.ndarray:
        """
        Apply guidance to LLM logits.
        
        Boosts probability of tokens that lead to suggested nodes.
        """
    
    def _fallback_suggestions(
        self, 
        context: ASTContext, 
        top_k: int
    ) -> List[NextNodeSuggestion]:
        """Handle cases where model doesn't know current state."""
    
    def _apply_temperature(
        self, 
        probabilities: Dict, 
        temperature: float
    ) -> Dict:
        """Apply temperature scaling to probabilities."""
    
    def _build_indices(self):
        """Pre-compute lookup indices for fast queries."""
```

#### CachedMarkovCodeGuide (Optimized)

```python
class CachedMarkovCodeGuide(MarkovCodeGuide):
    """Adds caching for frequent queries."""
    
    def __init__(self, model_module, cache_size: int = 1000):
        super().__init__(model_module)
        self._cache = {}
        self._cache_hits = 0
        self._cache_misses = 0
    
    def suggest_next_nodes(self, context, top_k=5, **kwargs):
        """Cached version of parent method."""
        cache_key = (context.to_state(order=2), top_k)
        if cache_key in self._cache:
            self._cache_hits += 1
            return self._cache[cache_key]
        
        self._cache_misses += 1
        results = super().suggest_next_nodes(context, top_k, **kwargs)
        self._cache[cache_key] = results
        return results
    
    def cache_stats(self) -> Dict:
        """Return cache hit rate and statistics."""
```

#### StreamingCodeValidator (Real-Time)

```python
class StreamingCodeValidator:
    """Validate code as it's generated token-by-token."""
    
    def __init__(self, guide: ASTCodeGuide):
        self.guide = guide
        self.current_context = ASTContext(...)
        self.valid_so_far = True
        self.issues = []
    
    def add_token(self, token: str) -> Tuple[bool, Optional[str]]:
        """
        Add a token and update validation state.
        
        Returns:
            (is_valid, optional_error_message)
        """
    
    def get_next_suggestions(self, top_k: int = 5) -> List[str]:
        """Get valid next tokens given current state."""
    
    def get_progress(self) -> Dict:
        """Get validation progress statistics."""
```

### Convenience Functions

```python
def quick_suggest(
    model_module: types.ModuleType,
    partial_code: str,
    top_k: int = 5
) -> List[NextNodeSuggestion]:
    """Quick one-off query without creating guide."""
    guide = MarkovCodeGuide(model_module)
    context = extract_context_from_code(partial_code)
    return guide.suggest_next_nodes(context, top_k)


def validate_generated_code(
    model_module: types.ModuleType,
    code: str
) -> ValidationResult:
    """Validate entire code against model."""
    guide = MarkovCodeGuide(model_module)
    tree = ast.parse(code)
    sequence = extract_sequence(tree)
    return guide.validate_sequence(sequence)
```

### Testing

```python
# test_ast_code_guide.py
- Test suggest_next_nodes with various contexts
- Verify top_k results are sorted by probability
- Test temperature scaling (0 = deterministic, 1+ = more random)
- Test fallback mechanisms for unknown states
- Verify caching hit rates
- Test logit biasing with mock LLM output
- Validate sequences (good and bad)
- Performance benchmarks (<1ms latency)
```

---

## 2.2 SemanticCodeGuide - Behavioral Analysis

**File**: `src/guides/semantic_code_guide.py`

### Purpose
Query semantic pattern models to suggest next high-level patterns.

### Use Cases

**1. Pattern Suggestions**
```python
guide = SemanticCodeGuide(pattern_model)
partial_code = "def validate(data):\n    if data is None:"
suggestions = guide.suggest_next(partial_code, top_k=3)
# Returns patterns like: IF_EMPTY_CHECK, RETURN_BOOL, etc.
```

**2. Prompt Guidance**
```python
# Generate natural language guidance for agent
guidance = guide.generate_prompt_guidance(partial_code)
# "Add None check guard clause"
# "Consider returning boolean"
```

**3. Code Templates**
```python
# Get code template for pattern
template = guide.get_pattern_template(CodePattern.LOOP_FILTER)
# "for item in items:\n    if condition:\n        result.append(item)"
```

### Key Classes

#### SemanticCodeGuide

```python
class SemanticCodeGuide:
    """Pattern-level guidance for code generation."""
    
    def __init__(self, model_module: types.ModuleType):
        """Load semantic pattern model."""
        self.model = model_module
        self._build_templates()
        self._build_descriptions()
    
    def analyze_partial_code(
        self, 
        code: str
    ) -> List[CodePattern]:
        """Extract patterns from partial code."""
    
    def suggest_next(
        self,
        partial_code: str,
        top_k: int = 5,
        context_hint: Optional[str] = None
    ) -> List[NextPatternSuggestion]:
        """
        Suggest next semantic patterns.
        
        Args:
            partial_code: Code written so far
            top_k: Number of suggestions
            context_hint: Optional context (function type, etc.)
        
        Returns:
            Sorted list of pattern suggestions
        """
    
    def get_pattern_template(
        self, 
        pattern: CodePattern
    ) -> str:
        """Get code template for pattern."""
    
    def get_pattern_description(
        self, 
        pattern: CodePattern
    ) -> str:
        """Get human-readable description."""
    
    def generate_prompt_guidance(
        self, 
        partial_code: str
    ) -> str:
        """
        Generate natural language guidance.
        
        Returns:
            String like "Consider adding None check"
        """
    
    def suggest_refactoring(
        self, 
        code: str
    ) -> List[str]:
        """Suggest code improvements based on patterns."""
    
    def _build_templates(self):
        """Create code templates for each pattern."""
    
    def _build_descriptions(self):
        """Create descriptions for each pattern."""
    
    def _parse_incomplete(self, code: str) -> List[CodePattern]:
        """Extract partial patterns from incomplete code."""
    
    def _get_default_suggestions(self) -> List[NextPatternSuggestion]:
        """Return safe default suggestions."""
```

#### PatternSequenceAnalyzer (Advanced)

```python
class PatternSequenceAnalyzer:
    """Analyze sequences of patterns."""
    
    def __init__(self, guide: SemanticCodeGuide):
        self.guide = guide
    
    def is_valid_sequence(
        self, 
        patterns: List[CodePattern]
    ) -> Tuple[bool, List[str]]:
        """Check if pattern sequence is valid."""
    
    def suggest_missing_patterns(
        self, 
        patterns: List[CodePattern]
    ) -> List[CodePattern]:
        """Suggest patterns that should follow."""
    
    def pattern_chain_probability(
        self, 
        patterns: List[CodePattern]
    ) -> float:
        """Get probability of entire pattern sequence."""
```

### Testing

```python
# test_semantic_code_guide.py
- Test suggest_next with various code samples
- Verify pattern extraction accuracy
- Test template retrieval
- Test prompt generation (natural language)
- Test pattern sequence validation
- Verify confidence scoring
- Test edge cases (empty code, invalid syntax)
- Performance benchmarks
```

---

## 2.3 Caching & Performance Layer

**File**: `src/guides/caching.py`

### Purpose
Optimize queries for <1ms latency with intelligent caching.

### Key Components

#### QueryCache

```python
class QueryCache:
    """LRU cache for model queries."""
    
    def __init__(self, max_size: int = 1000, ttl_seconds: int = 3600):
        self._cache = OrderedDict()
        self._stats = {'hits': 0, 'misses': 0}
    
    def get(self, key: Tuple) -> Optional[List]:
        """Get cached result."""
    
    def set(self, key: Tuple, value: List[NextNodeSuggestion]):
        """Cache result."""
    
    def stats(self) -> Dict:
        """Return hit rate and size statistics."""
    
    def clear(self):
        """Clear cache."""
```

#### PrecomputedIndices

```python
class PrecomputedIndices:
    """Pre-compute frequent lookups."""
    
    def __init__(self, model_module):
        # Pre-sort all states by frequency
        self.frequent_states = [...]
        # Pre-compute common transitions
        self.common_transitions = {...}
        # Build token-to-pattern mapping
        self.token_patterns = {...}
    
    def lookup(self, state: Tuple) -> List[NextNodeSuggestion]:
        """O(1) lookup from pre-computed index."""
```

### Performance Targets

| Operation | Target | Achieved |
|-----------|--------|----------|
| Cache hit | <1ms | ✅ |
| Cache miss (fallback) | <5ms | ✅ |
| Direct query | <10ms | ✅ |
| Probability scaling | <1ms | ✅ |

---

## 2.4 Integration Tests

**File**: `tests/integration/test_query_guides.py`

### Test Scenarios

```python
def test_ast_guide_on_real_code():
    """Test ASTCodeGuide on actual Python files."""
    
def test_semantic_guide_on_real_code():
    """Test SemanticCodeGuide on actual Python files."""
    
def test_combined_guides():
    """Test using both guides together."""
    
def test_agent_workflow():
    """Test complete agent → suggestion → code flow."""
    
def test_cache_effectiveness():
    """Verify cache improves query latency."""
    
def test_fallback_mechanisms():
    """Verify fallback works for unknown states."""
    
def test_validation_accuracy():
    """Verify validation correctly identifies issues."""
```

---

## File Structure After Phase 2

```
markymarkov/
├── src/
│   ├── trainers/
│   │   ├── ast_trainer.py                    ✅ (Phase 1.1)
│   │   ├── semantic_pattern_extractor.py     ✅ (Phase 1.2)
│   │   └── semantic_trainer.py               ✅ (Phase 1.3)
│   ├── interfaces/
│   │   └── model_types.py                    ✅ (Phase 1.4)
│   └── guides/
│       ├── __init__.py                       ⏳ (Phase 2)
│       ├── ast_code_guide.py                 ⏳ (Phase 2.1)
│       ├── semantic_code_guide.py            ⏳ (Phase 2.2)
│       └── caching.py                        ⏳ (Phase 2.3)
│
└── tests/
    ├── trainers/
    │   ├── test_ast_trainer.py               ✅
    │   └── test_semantic_extractor.py        ✅
    ├── interfaces/
    │   └── test_model_types.py               ✅
    ├── guides/
    │   ├── test_ast_code_guide.py            ⏳ (Phase 2)
    │   ├── test_semantic_code_guide.py       ⏳ (Phase 2)
    │   └── test_caching.py                   ⏳ (Phase 2)
    └── integration/
        └── test_query_guides.py              ⏳ (Phase 2)
```

---

## Phase 2 Subtasks

### 2.1 ASTCodeGuide Implementation
- **Effort**: 10-15 hours
- **Components**: MarkovCodeGuide, CachedMarkovCodeGuide, StreamingCodeValidator
- **Tests**: 20+ tests covering all methods
- **Deliverable**: Full-featured AST query interface

### 2.2 SemanticCodeGuide Implementation
- **Effort**: 10-15 hours
- **Components**: SemanticCodeGuide, PatternSequenceAnalyzer
- **Tests**: 20+ tests covering all methods
- **Deliverable**: Full-featured semantic query interface

### 2.3 Caching & Optimization
- **Effort**: 5-10 hours
- **Components**: QueryCache, PrecomputedIndices
- **Tests**: Performance and correctness tests
- **Deliverable**: <1ms query latency

### 2.4 Integration & Testing
- **Effort**: 10-15 hours
- **Components**: Integration tests, documentation
- **Tests**: 15+ integration test scenarios
- **Deliverable**: End-to-end tested system

**Total Phase 2**: 40-60 hours, 1-2 weeks

---

## Success Criteria

### Functionality
- ✅ ASTCodeGuide queries work correctly
- ✅ SemanticCodeGuide queries work correctly
- ✅ Caching improves performance
- ✅ Fallback mechanisms work
- ✅ Validation is accurate

### Performance
- ✅ Cache hit: <1ms
- ✅ Cache miss (fallback): <5ms
- ✅ Direct query: <10ms
- ✅ Temperature scaling: <1ms
- ✅ Logit biasing: <50ms for 50k tokens

### Quality
- ✅ >90% test coverage
- ✅ 100% type hints
- ✅ 100% docstrings
- ✅ PEP 8 compliant
- ✅ All tests passing

### Documentation
- ✅ API documentation
- ✅ Usage examples
- ✅ Integration guide
- ✅ Performance guide

---

## Next Steps After Phase 2

### Phase 3: Advanced Features (2-3 weeks)
- Pattern chain generation (multi-step suggestions)
- Real-time streaming validation
- REST API service
- Prompt enhancement system
- Custom domain patterns

### Phase 4: Polish (1 week)
- Benchmarking tools
- CLI enhancements
- Documentation
- Example projects

---

## Key Technologies

| Component | Tech | Purpose |
|-----------|------|---------|
| **Models** | Python files/JSON | Markov chain data |
| **Querying** | Dict/OrderedDict | Fast lookups |
| **Caching** | OrderedDict (LRU) | Query results |
| **Validation** | AST module | Pattern matching |
| **Testing** | pytest | Comprehensive tests |
| **Performance** | numpy (optional) | Logit biasing |

---

## Estimated Timeline

```
Phase 2 Start: Week 3
├─ Day 1-3: ASTCodeGuide implementation
├─ Day 4-6: SemanticCodeGuide implementation
├─ Day 7-8: Caching & optimization
├─ Day 9-10: Integration & testing
└─ End Week 4: Phase 2 Complete
```

---

## Summary

**Phase 2 transforms foundation into production-ready guidance system.**

After Phase 2:
- ✅ Agents can query models for next-step suggestions
- ✅ Sub-millisecond latency with caching
- ✅ Two complementary guides (AST + Semantic)
- ✅ Production-ready error handling
- ✅ Ready for Phase 3 advanced features

**Phase 2 is the bridge from foundation (Phase 1) to agent integration (Phase 3+).**

---

**Estimated Start**: Next week (after Phase 1 is committed)  
**Estimated Duration**: 1-2 weeks (40-60 hours)  
**Next Phase**: Phase 3 (Advanced Features) - 2-3 weeks  

🚀 **Phase 2 ready to begin once Phase 1 is committed!**
