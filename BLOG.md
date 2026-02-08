# Marky: Markov Chain-Based Code Guidance for LLM Agents

## Table of Contents

1. **Introduction**
   - What is Marky?
   - The Problem It Solves
   - Why Markov Chains for Code?

2. **Core Concept**
   - Two-Level Architecture (AST + Semantic)
   - How Markov Models Learn Code Patterns
   - From Training to Deployment

3. **Architecture Deep Dive**
   - Level 1: AST Patterns (Syntactic Correctness)
   - Level 2: Semantic Patterns (Code Style & Idioms)
   - How They Work Together

4. **The Two-Level Approach Explained**
   - Why Not Just AST?
   - Why Not Just Semantic?
   - The Sweet Spot: Combined Validation

5. **Practical Examples**
   - Training Marky on Your Codebase
   - Using Marky to Validate Generated Code
   - Real-World Validation Output with Diagnostics
   - Understanding Coverage & Confidence Scores

6. **52 Semantic Patterns**
   - Control Flow Patterns
   - Loop Patterns
   - Return Patterns
   - Data Structure Patterns
   - Error Handling Patterns
   - And More...

7. **Integration with LLM Agents**
   - How Agents Use Marky for Guidance
   - Temperature Sampling for Diversity
   - Logit Biasing for LLM Steering
   - Real-Time Validation During Generation

8. **Performance Characteristics**
   - Query Latency (<1ms cached, <10ms uncached)
   - Training Speed (1000 files/min for AST)
   - Throughput & Scalability
   - Memory Footprint

9. **Use Cases**
   - Code Quality Assurance
   - Style Enforcement
   - Training Data Analysis
   - Model-Driven Code Generation
   - Identifying Code Anomalies

10. **Getting Started**
    - Installation & Setup
    - Training Your First Model
    - Running Validation
    - Integration Patterns

11. **Under the Hood**
    - How Markov Chains Work
    - N-gram Orders (1st, 2nd, 3rd)
    - Probability Calculations
    - State Representation

12. **Lessons Learned & Design Decisions**
    - Why Export Models as Python?
    - Flexible N-gram Orders
    - Location Tracking for Diagnostics
    - Confidence Scoring Strategy

13. **Comparison with Alternatives**
    - Linters vs. Marky
    - Type Checkers vs. Marky
    - AST Analysis Tools vs. Marky
    - Machine Learning Approaches vs. Marky

14. **Future Roadmap**
    - REST API Service
    - Prompt Enhancement Module
    - Reference Agent Framework
    - Browser Integration
    - IDE Plugins

15. **Conclusion**
    - Why Markov Chains Matter for Code
    - The Power of Pattern Learning
    - Building Better Code Generation Tools

---

## Outline Details

### 1. Introduction

**What is Marky?**
- Marky is a Markov Chain-based code guidance system designed to help LLM agents generate better code
- It learns patterns from existing codebases and uses those patterns to validate and guide code generation
- Built specifically for Python (but architecture is language-agnostic)

**The Problem It Solves**
- LLMs generate syntactically correct code but not always stylistically correct
- No way to check if generated code follows project conventions
- Hard to enforce organizational coding standards programmatically
- Gap between "valid code" and "idiomatic code"

**Why Markov Chains for Code?**
- Markov chains excel at learning sequential patterns
- Code is inherently sequential (AST traversal, control flow, pattern chains)
- Computationally efficient compared to deep learning
- Interpretable: can explain why a pattern is (or isn't) expected

### 2. Core Concept

**Two-Level Architecture (AST + Semantic)**
- Level 1 (AST): Ensures syntactic correctness
- Level 2 (Semantic): Ensures stylistic/idiomatic correctness
- Complementary, not redundant

**How Markov Models Learn Code Patterns**
- Parse code into AST or semantic patterns
- Extract sequences of transitions (parent→child, pattern→pattern)
- Build frequency tables of what typically follows what
- Calculate probabilities for each transition

**From Training to Deployment**
- Train models offline on your codebase
- Export as executable Python modules (no parsing needed)
- Load and use for real-time validation during code generation
- Sub-millisecond lookup times with caching

### 3. Architecture Deep Dive

**Level 1: AST Patterns (Syntactic Correctness)**
- Extracts (parent_type, node_type) pairs from AST
- Example: `(FunctionDef, Return)` - a return inside a function
- Validates that generated code produces expected AST sequences
- Catches structural violations early

**Level 2: Semantic Patterns (Code Style & Idioms)**
- Detects 52+ high-level coding patterns
- Examples: `init-method`, `loop-filter`, `guard-clause`, `string-format`
- Validates that generated code follows project conventions
- Understands intent, not just syntax

**How They Work Together**
- AST validates structure is correct
- Semantic validates structure is idiomatic
- Both provide confidence scores
- Fallback mechanism: if one is uncertain, check the other

### 4. The Two-Level Approach Explained

**Why Not Just AST?**
- AST only validates syntax, not style
- Two valid ASTs can have very different readability/idiomaticity
- Misses high-level code intent

**Why Not Just Semantic?**
- Semantic patterns can be ambiguous without AST context
- May miss subtle syntactic issues
- Harder to generate code from semantic constraints alone

**The Sweet Spot: Combined Validation**
- Use AST for correctness (did the code parse?)
- Use Semantic for style (does it follow conventions?)
- Combine confidence scores for overall assessment
- Example: "Valid (AST: 0.8, Semantic: 0.6) = 0.7 overall"

### 5. Practical Examples

**Training Marky on Your Codebase**
```bash
python -m src train /path/to/code models/ --model-type both
```
- Analyzes all Python files
- Builds AST and semantic models
- Exports as Python modules
- ~5 minutes for 1000 files

**Using Marky to Validate Generated Code**
```bash
python -m src validate models/semantic_model.py generated_code.py
```
- Shows pattern sequences
- Highlights known vs unknown transitions
- Provides coverage percentage
- Suggests expected alternatives

**Real-World Validation Output with Diagnostics**
```
✓ Matching sequences (12):
  1. init-method → function-transformer → if-empty-check (0.075) @ line 116:8
  2. function-transformer → if-empty-check → return-none (0.244) @ line 118:12

✗ Non-matching sequences (3):
  1. return-list → guard-clause → string-format
     Expected one of: return-list, return-computed, guard-clause

Summary:
  Unique patterns found: 23
  Coverage: 12/15 transitions (80.0%)
```

**Understanding Coverage & Confidence Scores**
- Coverage: % of transitions that match training data
- Confidence: Probability-weighted score (0.0-1.0)
- High coverage + high confidence = Very idiomatic
- Low coverage = Unusual but possibly valid style

### 6. 52 Semantic Patterns

**Control Flow Patterns**
- IF_NONE_CHECK: `if x is None:`
- IF_NOT_NONE: `if x is not None:`
- IF_EMPTY_CHECK: `if not x:` or `if len(x) == 0:`
- IF_TYPE_CHECK: `if isinstance(x, Type):`
- GUARD_CLAUSE: Early return for invalid cases

**Loop Patterns**
- LOOP_ACCUMULATE: `result = []; for item in items: result.append(...)`
- LOOP_TRANSFORM: `for item in items: yield transform(item)`
- LOOP_FILTER: `for item in items: if condition: process(item)`
- LOOP_ENUMERATE: `for i, item in enumerate(items):`
- LOOP_ZIP: `for x, y in zip(a, b):`
- LOOP_DICT_ITEMS: `for k, v in dict.items():`

**Return Patterns**
- RETURN_NONE: `return None` or bare `return`
- RETURN_BOOL: `return True` or `return False`
- RETURN_LIST: `return []` or `return [computed_value]`
- RETURN_DICT: `return {}` or `return {key: value}`
- RETURN_COMPUTED: `return a + b` or `return func(x)`

**Data Structure Patterns**
- INIT_EMPTY_LIST: `x = []`
- INIT_EMPTY_DICT: `x = {}`
- INIT_COUNTER: `x = 0`
- APPEND_TO_LIST: `list.append(item)`
- DICT_UPDATE: `dict.update(other)`
- DICT_GET_DEFAULT: `dict.get(key, default)`
- UNPACKING: `x, y = data`

**Error Handling Patterns**
- TRY_EXCEPT_PASS: `try: ...; except: pass`
- TRY_EXCEPT_LOG: `try: ...; except: logger.error(...)`
- TRY_EXCEPT_RERAISE: `try: ...; except: raise`
- TRY_FINALLY: `try: ...; finally: cleanup()`
- CONTEXT_MANAGER: `with open(file) as f:`

**Function/Class Patterns**
- FUNCTION_VALIDATOR: Function that validates input
- FUNCTION_TRANSFORMER: Function that transforms data
- INIT_METHOD: `__init__(self, ...)`
- PROPERTY_GETTER: `@property def x(self):`
- CLASS_METHOD: `@classmethod def ...`
- STATIC_METHOD: `@staticmethod def ...`

**Comprehension & Other Patterns**
- LIST_COMPREHENSION: `[x for x in items if ...]`
- DICT_COMPREHENSION: `{k: v for k, v in ...}`
- GENERATOR_EXPRESSION: `(x for x in items)`
- TERNARY_EXPRESSION: `x if condition else y`
- STRING_FORMAT: `f"{x} {y}"` or `x.format(y)`
- LOGGING_CALL: `logger.info()`, `logger.debug()`, etc.

### 7. Integration with LLM Agents

**How Agents Use Marky for Guidance**
- Agent generates token
- Marky checks if it's valid (confidence score)
- If uncertain, agent adjusts next token
- Real-time feedback loop

**Temperature Sampling for Diversity**
- Low temp (0.3): Only suggest high-probability tokens
- High temp (1.0): Allow unusual but valid patterns
- Tunable per use-case

**Logit Biasing for LLM Steering**
- Boost logits for preferred tokens
- Suppress logits for unusual patterns
- Direct LLM attention to idiomatic code

**Real-Time Validation During Generation**
- Stream tokens from LLM
- Validate each token/statement
- Provide confidence feedback
- Guide generation corrections

### 8. Performance Characteristics

**Query Latency**
- Cached lookup: <1ms
- Uncached lookup: <10ms
- Validation: <50ms
- Training: 1000 files/min (AST), 500 files/min (Semantic)

**Throughput & Scalability**
- 50K+ queries/second possible
- Cache hit rate: >90% (with warming)
- Linear scaling with codebase size

**Memory Footprint**
- AST model: 10-50MB
- Semantic model: 1-10MB
- Cache: Configurable (default 100 entries = ~10MB)

### 9. Use Cases

**Code Quality Assurance**
- Validate that generated code matches style
- Catch deviations from project norms
- Enforce consistency across team

**Style Enforcement**
- Define idiomatic patterns for your codebase
- Reject non-idiomatic code
- Guide developers toward better patterns

**Training Data Analysis**
- Understand what patterns your codebase uses
- Identify code anomalies
- Find tech debt hotspots

**Model-Driven Code Generation**
- Train models on production code
- Use to guide LLM generation
- Combine with prompt engineering

**Identifying Code Anomalies**
- Low confidence = unusual patterns
- Could indicate bugs, anti-patterns
- Helpful for code review

### 10. Getting Started

**Installation & Setup**
```bash
git clone https://github.com/your/marky
cd marky
uv sync  # or pip install -e .
```

**Training Your First Model**
```bash
# Train on your codebase
python -m src train /path/to/your/code models/

# Or on specific patterns
python -m src train /path/to/code models/ --model-type semantic --order 2
```

**Running Validation**
```bash
# Validate a file
python -m src validate models/semantic_model.py your_file.py

# See statistics
python -m src stats models/semantic_model.py

# Try the demo
python -m src demo
```

**Integration Patterns**
- Load model as Python module
- Call `MarkovCodeGuide.suggest_next_nodes()`
- Use with streaming code validator
- Integrate with LLM inference pipeline

### 11. Under the Hood

**How Markov Chains Work**
- Chain property: next state depends only on current state
- Transition matrix: P(next | current)
- Learn frequencies from data
- Look up probabilities at inference time

**N-gram Orders (1st, 2nd, 3rd)**
- Order 1: Single previous state → next
- Order 2: Two previous states → next
- Order 3: Three previous states → next
- Higher order = more specific but sparser

**Probability Calculations**
- Count transitions during training
- P(next | context) = count(context→next) / count(context)
- Use log probabilities to avoid underflow
- Normalize to get confidence scores

**State Representation**
- AST: (parent_type, node_type) tuples
- Semantic: CodePattern enum values
- N-grams: Tuple of N consecutive states
- Lookups: O(1) hash table access

### 12. Lessons Learned & Design Decisions

**Why Export Models as Python?**
- Executable modules, no parsing overhead
- Fast loading (just import)
- Easy to version control
- No runtime dependencies needed

**Flexible N-gram Orders**
- Order 1: Fast but less specific
- Order 2: Good balance (used by default)
- Order 3: More specific but larger models
- Users choose based on their data

**Location Tracking for Diagnostics**
- Store line:column for each pattern
- Help developers find issues
- Enable future IDE integration
- Improves debugging experience

**Confidence Scoring Strategy**
- Probability-based (log probabilities)
- Tunable thresholds
- Combines AST + Semantic scores
- Human-interpretable (0.0-1.0)

### 13. Comparison with Alternatives

**Linters (pylint, flake8)**
- Linters: Check static rules
- Marky: Learn patterns from data
- Complementary, not competing
- Marky finds issues linters can't express

**Type Checkers (mypy)**
- Type checkers: Validate type correctness
- Marky: Validate sequence/style correctness
- Both enhance code quality
- Use together for comprehensive checking

**AST Analysis Tools (AST, visitor patterns)**
- AST tools: Raw syntax analysis
- Marky: Probabilistic pattern learning
- Marky hides complexity behind models
- Easier to maintain and extend

**Machine Learning Approaches**
- Deep learning: Black box, hard to debug
- Marky: Interpretable, explainable
- Marky: Lightweight, fast
- Marky: Better for style (not semantics)

### 14. Future Roadmap

**REST API Service (Phase 3.1)**
- `/ast/suggest` endpoint
- `/semantic/suggest` endpoint
- Containerized deployment

**Prompt Enhancement Module (Phase 3.2)**
- Inject pattern guidance into prompts
- Generate pattern-aware hints
- Improve LLM generation quality

**Reference Agent Framework (Phase 3.3)**
- Example implementation of agent using Marky
- Iterative refinement loop
- Pattern-driven generation

**Browser Integration (Phase 4)**
- VS Code extension
- PyCharm plugin
- Real-time feedback in editor

**IDE Plugins**
- Click to navigate to pattern source
- Suggestions for pattern improvements
- One-click refactoring to idiomatic style

### 15. Conclusion

**Why Markov Chains Matter for Code**
- Code is sequential; Markov chains are made for sequences
- Efficient, interpretable, practical
- Not trying to replace deep learning, complement it

**The Power of Pattern Learning**
- Let your codebase teach the model
- Capture organizational standards
- Enforce consistency at scale

**Building Better Code Generation Tools**
- Validation is key to agent quality
- Style matters as much as correctness
- Two-level approach (AST + Semantic) is the sweet spot
- Marky enables this at production scale

---

## Key Stats to Include

- **170/170 tests passing** (100% test coverage)
- **2000+ lines of implementation code**
- **52+ semantic patterns** defined
- **<1ms query latency** (cached)
- **<50ms validation time** for typical files
- **Production-ready architecture**

---

## Tone & Style

- Technical but accessible
- Code examples throughout
- Real output examples
- Actionable guidance
- Problem-focused (start with problems)
- Solution-focused (show how Marky solves them)

---

**Current Status**: Outline complete
**Next Step**: Write full sections
