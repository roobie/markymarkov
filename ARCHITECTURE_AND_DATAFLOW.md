# Architecture & Data Flow Reference

This document provides a visual and structural reference for the implementation.

---

## High-Level System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         LLM CODING AGENT                         │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Generation Loop                                        │   │
│  │  - Query guides for next patterns/nodes               │   │
│  │  - Generate with guidance (prompt/logit bias)         │   │
│  │  - Validate generated code                            │   │
│  │  - Iterate until complete                             │   │
│  └─────────────────────────────────────────────────────────┘   │
└──────────────┬──────────────────────────────────────────────────┘
               │
               │ Queries: "what's next?", "validate this code"
               ▼
┌─────────────────────────────────────────────────────────────────┐
│              MARKY: MARKOV GUIDANCE SYSTEM                       │
│                                                                   │
│  ┌────────────────────┐          ┌────────────────────┐         │
│  │  ASTCodeGuide      │          │ SemanticCodeGuide  │         │
│  │  ─────────────────  │          │ ──────────────────  │         │
│  │ .suggest_next()    │          │ .suggest_next()   │         │
│  │ .validate()        │          │ .generate_prompt()│         │
│  │ .bias_logits()     │          │ .complete_pattern()         │
│  │ .get_cached()      │          │ .analyze_code()   │         │
│  └────────────────────┘          └────────────────────┘         │
│           ▲                               ▲                      │
│           │                               │                      │
│  ┌────────┴───────────┐        ┌─────────┴───────────┐         │
│  │ AST Model          │        │ Semantic Model      │         │
│  │ (transitions)      │        │ (pattern sequences) │         │
│  │ (probabilities)    │        │ (probabilities)     │         │
│  │ (helpers)          │        │ (templates)         │         │
│  └────────────────────┘        └─────────────────────┘         │
└──────────────┬───────────────────────────┬──────────────────────┘
               │                           │
               │                           │
        ┌──────▼──────┐         ┌──────────▼────────┐
        │ Load at     │         │ Load at          │
        │ Runtime     │         │ Runtime          │
        └──────┬──────┘         └──────┬───────────┘
               │                       │
               ▼                       ▼
        ┌──────────────┐      ┌──────────────────┐
        │ Training     │      │ Training         │
        │ (one-time)   │      │ (one-time)       │
        │              │      │                  │
        │ ASTTrainer   │      │ SemanticTrainer  │
        └──────────────┘      └──────────────────┘
               ▲                       ▲
               │                       │
        ┌──────┴───────────────────────┴─────────┐
        │       Your Python Codebase             │
        │       (stdlib, project, examples)      │
        └────────────────────────────────────────┘
```

---

## Training Pipeline Data Flow

### AST Training Pipeline

```
Source Code
    │
    ▼
┌─────────────────────────┐
│ ASTMarkovTrainer        │
├─────────────────────────┤
│ train_on_code()         │
│ ├─ ast.parse(code)      │
│ ├─ extract_ast_sequence │
│ │  ├─ DFS traversal     │
│ │  └─ Collect (parent, node_type) pairs
│ ├─ Build n-grams        │
│ │  ├─ Order-1: (parent, node) → next
│ │  ├─ Order-2: ((p1,n1), (p2,n2)) → next
│ │  └─ ...                │
│ └─ Update transitions dict
└─────────────────────────┘
    │
    ▼
transitions = {
    ('FunctionDef', 'arguments'): Counter({'Return': 450, 'Expr': 230, ...}),
    ...
}
    │
    ▼
probabilities = {
    ('FunctionDef', 'arguments'): {'Return': 0.65, 'Expr': 0.33, ...},
    ...
}
    │
    ▼
export_to_python()
    │
    ▼
ast_markov_model.py (executable Python module)
```

### Semantic Training Pipeline

```
Source Code
    │
    ▼
┌──────────────────────────────┐
│ SemanticMarkovTrainer        │
├──────────────────────────────┤
│ train_on_code()              │
│ ├─ ast.parse(code)           │
│ ├─ SemanticPatternAnalyzer   │
│ │  ├─ ast.walk() + classify  │
│ │  ├─ visit_If()             │
│ │  ├─ visit_For()            │
│ │  ├─ visit_Return()         │
│ │  └─ Detect CodePattern     │
│ ├─ Collect pattern sequence  │
│ ├─ Build n-grams             │
│ │  └─ (Pattern, Pattern, ...) → next Pattern
│ └─ Update transitions dict   │
└──────────────────────────────┘
    │
    ▼
transitions = {
    (CodePattern.GUARD_CLAUSE, CodePattern.IF_NOT_NONE): Counter({
        CodePattern.LOOP_FILTER: 45,
        CodePattern.LOOP_TRANSFORM: 32,
        ...
    }),
    ...
}
    │
    ▼
probabilities = {
    (CodePattern.GUARD_CLAUSE, CodePattern.IF_NOT_NONE): {
        CodePattern.LOOP_FILTER: 0.58,
        CodePattern.LOOP_TRANSFORM: 0.41,
        ...
    },
    ...
}
    │
    ▼
export_to_python()
    │
    ▼
semantic_model.py (executable Python module)
```

---

## Query Time Data Flow

### AST Guide Query

```
Agent: "Given this AST state, what should come next?"
    │
    ▼
ASTCodeGuide.suggest_next_nodes(context, top_k=5, temperature=1.0)
    │
    ├─ Convert context to state tuple
    │  └─ ASTContext.to_state(order=2)
    │
    ├─ Lookup in cache
    │  ├─ HIT: Return immediately
    │  └─ MISS: Continue
    │
    ├─ Get probabilities from model
    │  └─ self.probabilities.get(state)
    │
    ├─ Handle unknown state (fallback)
    │  └─ Aggregate similar states
    │
    ├─ Apply temperature if needed
    │  └─ Scale probabilities
    │
    ├─ Select top-k
    │  └─ Sort by probability
    │
    └─ Build suggestions list
       └─ [NextNodeSuggestion(...), ...]
    │
    ▼
Return: List[NextNodeSuggestion]
    {
        node_type: str
        probability: float
        confidence: str ('high'/'medium'/'low')
        common_patterns: List[str]
    }
```

### Semantic Guide Query

```
Agent: "Given this partial code, what patterns should I use next?"
    │
    ▼
SemanticCodeGuide.suggest_next(partial_code, top_k=5, context_hint=None)
    │
    ├─ Analyze partial code
    │  ├─ ast.parse(code)
    │  ├─ SemanticPatternAnalyzer.visit()
    │  └─ Extract current patterns
    │
    ├─ If parsing fails (incomplete code)
    │  └─ Heuristic pattern detection from text
    │
    ├─ Query semantic model
    │  └─ model.suggest_next_patterns(current_patterns, k=top_k)
    │
    ├─ Enrich with metadata
    │  ├─ Add confidence levels
    │  ├─ Add code templates
    │  └─ Add descriptions
    │
    └─ Build suggestions list
       └─ [PatternSuggestion(...), ...]
    │
    ▼
Return: List[PatternSuggestion]
    {
        pattern: CodePattern
        probability: float
        description: str
        code_template: str
        confidence: str
    }
```

---

## Integration Point Examples

### Example 1: Prompt Enhancement

```
Agent has generated:
    def process_users(users):
        if users is None:
            return []
        result = []

Query semantic guide:
    guide.suggest_next(partial_code)
    → [
        PatternSuggestion(LOOP_FILTER, 0.67, "Loop with filtering", "for... if..."),
        PatternSuggestion(LOOP_TRANSFORM, 0.23, "Transform items", "for..."),
        ...
    ]

Generate guidance:
    guidance = guide.generate_prompt_guidance(partial_code)
    → "Based on common patterns, consider:
        🔥 Loop with filtering (67% common)
        ✓ Transform items (23% common)
        · Check if empty (10% common)"

Enhance prompt:
    prompt = f"""
    Complete this function to filter users:
    
    {partial_code}
    
    {guidance}
    
    Continue the implementation:
    """

Send to LLM → Gets better suggestions
```

### Example 2: Code Completion with Pattern

```
Agent decides to use LOOP_FILTER pattern:

SemanticCodeGuide.complete_with_pattern(
    partial_code="""
    def filter_active_users(users):
        result = []
    """,
    pattern=CodePattern.LOOP_FILTER,
    item='user',
    collection='users',
    condition='user.is_active',
    result='result'
)

Template: "for {item} in {collection}:\n    if {condition}:\n        {result}.append({item})"

Fill template with variables:
    for user in users:
        if user.is_active:
            result.append(user)

Return: Complete code snippet ready to use
```

### Example 3: Real-time Validation

```
Agent generating token by token:

def validate_email(email):
    if email is None:
        return False
    ↓ (generate next token)

Validator:
    validator.add_token(token)
    ├─ current_code += token
    ├─ Try parse → works
    ├─ Extract AST sequence
    ├─ Validate against model
    │  └─ Check: Return → Return (unusual!)
    ├─ is_valid=False, warnings=["Unusual transition: Return → Return"]
    └─ Return: (should_continue=False, warning=...)

Agent: STOP - Unusual structure detected
```

### Example 4: Logit Biasing

```
LLM generates token logits: [0.1, 0.2, -0.5, 1.2, -0.8, ...]
    Index 0: token 'if'
    Index 1: token 'for'
    Index 2: token 'def'
    Index 3: token 'return'
    ...

Query AST guide:
    suggestions = guide.suggest_next_nodes(context, top_k=10)
    → [(If, 0.45), (For, 0.32), (Return, 0.18), ...]

Bias logits:
    bias_strength = 0.3
    biased_logits = (1 - 0.3) * original + 0.3 * bias_vector
    
    Where bias_vector upweights tokens for high-probability nodes:
        bias[0] (if) += log(0.45)
        bias[1] (for) += log(0.32)
        bias[3] (return) += log(0.18)

Sample from biased distribution:
    → More likely to generate If, For, Return
    → Less likely to generate semantically unusual constructs
```

---

## State Transitions Examples

### AST Level

```
Transition sequence in a typical function:

start → Module
Module → FunctionDef
FunctionDef → arguments
arguments → arg
arg → Expr (docstring)
Expr → Assign
Assign → Name, Assign
Assign → Call
Call → Name, keyword
keyword → Constant
Constant → Return
Return → Name

Probability model captures:
P(arg | arguments, FunctionDef) = 0.8
P(Expr | FunctionDef, arguments) = 0.15
...
```

### Semantic Level

```
Typical pattern sequences in data processing:

GUARD_CLAUSE → IF_NOT_NONE
IF_NOT_NONE → INIT_EMPTY_LIST
INIT_EMPTY_LIST → LOOP_TRANSFORM
LOOP_TRANSFORM → APPEND_TO_LIST
APPEND_TO_LIST → RETURN_LIST

Probability model captures:
P(IF_NOT_NONE | GUARD_CLAUSE) = 0.65
P(INIT_EMPTY_LIST | IF_NOT_NONE) = 0.45
P(LOOP_TRANSFORM | INIT_EMPTY_LIST) = 0.52
...
```

---

## Model Export Format

### AST Model (ast_markov_model.py)

```python
"""Auto-generated Markov chain model for Python AST patterns"""
from collections import Counter

# Raw transition counts
transitions = {
    (('start', 'Module'), ('Module', 'FunctionDef')): Counter({
        'arguments': 890,
        'Expr': 120,
        ...
    }),
    ...
}

# Transition probabilities
probabilities = {
    (('start', 'Module'), ('Module', 'FunctionDef')): {
        'arguments': 0.8636,
        'Expr': 0.1364,
        ...
    },
    ...
}

# Helper functions
def get_next_node_probabilities(state):
    return probabilities.get(state)

def get_top_k_next_nodes(state, k=5):
    probs = get_next_node_probabilities(state)
    return sorted(probs.items(), key=lambda x: x[1], reverse=True)[:k]

# Metadata
MARKOV_ORDER = 2
FILES_PROCESSED = 156
UNIQUE_STATES = 287
MIN_COUNT_THRESHOLD = 5
```

### Semantic Model (semantic_model.py)

```python
"""Auto-generated Semantic Markov Model for Code Patterns"""
from collections import Counter
from enum import Enum

class CodePattern(Enum):
    GUARD_CLAUSE = "guard-clause"
    IF_NOT_NONE = "if-not-none"
    LOOP_FILTER = "loop-filter"
    RETURN_LIST = "return-list"
    ...

# Pattern transition counts
transitions = {
    (CodePattern.GUARD_CLAUSE, CodePattern.IF_NOT_NONE): Counter({
        CodePattern.LOOP_FILTER: 234,
        CodePattern.LOOP_TRANSFORM: 156,
        ...
    }),
    ...
}

# Pattern transition probabilities
probabilities = {
    (CodePattern.GUARD_CLAUSE, CodePattern.IF_NOT_NONE): {
        CodePattern.LOOP_FILTER: 0.5821,
        CodePattern.LOOP_TRANSFORM: 0.3871,
        ...
    },
    ...
}

# Helper functions
def get_next_pattern_probabilities(pattern_sequence):
    return probabilities.get(pattern_sequence)

def suggest_next_patterns(current_patterns, k=5):
    # Implementation with descriptions
    ...

# Metadata
MARKOV_ORDER = 2
FILES_PROCESSED = 445
UNIQUE_SEQUENCES = 287
MIN_COUNT_THRESHOLD = 3
```

---

## Cache Strategy

### Pre-warming with Common Patterns

```
Common contexts that should be pre-cached:

AST Level:
  - Start of function: ('Module', 'FunctionDef')
  - Function body: ('FunctionDef', 'arguments')
  - If statement: ('FunctionDef', 'If')
  - Loop: ('FunctionDef', 'For')
  - Return: ('body', 'Return')
  ...

Semantic Level:
  - Guard + validation: (GUARD_CLAUSE, IF_NOT_NONE)
  - Validation + loop: (IF_NOT_NONE, LOOP_FILTER)
  - Init + loop: (INIT_EMPTY_LIST, LOOP_TRANSFORM)
  - Loop + return: (LOOP_FILTER, RETURN_LIST)
  ...

Cache behavior:
  - 10,000 LRU slots
  - Pre-load 50-100 common contexts
  - Hit rate: >90% on typical workloads
  - Time: <1ms average, <10ms worst case
```

---

## Error Handling & Fallbacks

### When Model State Not Found

```
Request: suggest_next_nodes(state=('FunctionDef', 'CustomClass'))
    ├─ Exact state not in model
    ├─ Try fallback: "Find all states ending with CustomClass"
    ├─ Aggregate probabilities from similar states
    │  └─ P(next) = average of similar state probabilities
    ├─ If still empty, return defaults
    │  └─ Most common next nodes overall
    └─ Mark confidence as 'low'
```

### When Code Doesn't Parse

```
Incomplete code: "def foo(x):\n    if x is"

Request: analyze_partial_code(incomplete)
    ├─ ast.parse() → SyntaxError
    ├─ Fall back to heuristic detection
    │  ├─ Look for "def" → FunctionDef pattern
    │  ├─ Look for "if" → If pattern
    │  └─ Look for text patterns
    ├─ Build partial pattern sequence
    ├─ Get suggestions (with low confidence)
    └─ Return best guesses with warnings
```

---

## Testing Strategy

### Unit Tests

```
trainers/
  - test_ast_extraction: Simple code → AST sequence
  - test_semantic_patterns: Code → CodePattern detection
  - test_model_export: Transitions → Executable Python

guides/
  - test_suggestions: Context → Top-k suggestions
  - test_fallback: Unknown state → Fallback behavior
  - test_temperature: Temperature scaling correctness
  - test_cache: Cache hit/miss behavior

interfaces/
  - test_data_types: Dataclass instantiation, conversions
```

### Integration Tests

```
training_pipeline/
  - Load source files → Train → Export → Load → Query

agent_integration/
  - Partial code → Suggestions → Completion → Validation

end_to_end/
  - Real LLM agent scenarios with both guides
```

---

## Deployment Checklist

Before production use:

- [ ] Phase 1 complete: Trainers work on 1000+ files
- [ ] Phase 2 complete: Guides achieve <1ms latency
- [ ] Phase 3 complete: Full agent integration tested
- [ ] Phase 4 complete: >95% test coverage
- [ ] Documentation: All guides have examples
- [ ] Performance: Meets latency/throughput targets
- [ ] Monitoring: Can track cache hit rate, query patterns
- [ ] Security: Model files validated on load
- [ ] Rollback: Can revert to previous model version

