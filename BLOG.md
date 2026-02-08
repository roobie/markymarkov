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

Marky is a Markov Chain-based code guidance system designed to help LLM agents generate better code. Unlike traditional linters or type checkers that enforce fixed rules, Marky learns patterns directly from your codebase and uses those patterns to validate and guide code generation in real-time.

At its core, Marky operates on a simple but powerful principle: **code is sequential, and code patterns are learnable**. By analyzing existing code, it builds probabilistic models of what patterns typically follow other patterns—both at the syntactic level (how code is structured) and at the semantic level (what code idioms are preferred).

Key characteristics:
- **Pattern-based**: Learns from your actual codebase, not predefined rules
- **Probabilistic**: Provides confidence scores, not just pass/fail
- **Fast**: Sub-millisecond lookups enable real-time guidance during generation
- **Interpretable**: Can explain why a pattern is expected or unexpected
- **Language-agnostic architecture**: Currently focused on Python, but extensible to other languages
- **Deployable**: Exports models as executable Python modules with no external dependencies

**The Problem It Solves**

Modern LLM-based code generation has created a paradox: **generated code is often syntactically correct does not always follow stylistic idioms or algorithmic patterns**.

Consider this scenario:
- An LLM generates a Python function that uses a valid but non-idiomatic pattern
- The code parses without errors
- Type checkers are satisfied
- But it violates your team's coding conventions
- A human reviewer flags it for rewriting

This is the gap Marky addresses. Today's development teams face several related challenges:

1. **Style Enforcement at Scale**
   - Teams want consistency across codebases
   - Manual code review can't catch every style deviation
   - Linters only check static rules, not learned patterns
   - No way to programmatically enforce "this is how *we* write code"

2. **LLM Code Generation Quality**
   - LLMs generate valid code, but not idiomatic code
   - Agents can't distinguish between "correct" and "our style"
   - Temperature and sampling can't capture organizational conventions
   - Training on diverse data means diverse output

3. **Validation Gaps**
   - Linters are rule-based (hard to maintain)
   - Type checkers focus on types, not patterns
   - AST visitors can find structure but miss intent
   - No standard way to validate "does this follow our patterns?"

4. **Training Data Analysis**
   - Hard to understand what patterns dominate your codebase
   - Difficult to identify anomalies or tech debt
   - No way to measure consistency across teams
   - Can't extract "what makes our code unique?"

Marky solves these by learning patterns from your code and providing:
- **Real-time validation**: Is this pattern expected?
- **Confidence scores**: How idiomatic is this code?
- **Diagnostic information**: Where does it diverge and why?
- **Generation guidance**: What patterns should come next?

**Why Markov Chains for Code?**

You might wonder: "Why not use deep learning, LSTMs, or transformers?" The answer reveals important truths about code and pattern matching.

1. **Code is Inherently Sequential**
   - Code flows through AST traversal order
   - Control flow follows predictable paths
   - Pattern composition is chain-like
   - Markov chains were literally invented for this use case

2. **The Markov Property Holds for Code**
   - "The next pattern depends only on the current pattern" ✓
   - Previous history can be captured in n-gram state
   - Two-state or three-state context is often sufficient
   - Rare cases benefit from higher-order models

3. **Computational Efficiency**
   - Training: O(n) pass through codebase
   - Inference: O(1) hash table lookup
   - Deep learning: GPU-heavy, requires infrastructure
   - Marky: CPU-friendly, runs anywhere
   - **1000 files/minute training speed** (AST model)
   - **<1ms query latency** (cached lookups)

4. **Interpretability**
   - Deep learning: "Why did it choose this?" → Inscrutable
   - Markov chains: "What's the probability?" → Auditable
   - Can explain: "After X pattern, Y is expected 85% of the time"
   - Developers can reason about confidence scores
   - No black box; built on transparent math

5. **Data Efficiency**
   - Deep learning: Needs massive datasets
   - Markov chains: Work well with any size codebases
   - Effective with 100+ files
   - Scales gracefully to 100K+ files
   - Graceful degradation (unknown patterns still provide value)

6. **Integration with LLMs**
   - LLMs already generate token sequences
   - Markov models provide per-token guidance
   - Natural fit for token-by-token validation
   - Easy to integrate into sampling/generation loops
   - No need to retrain LLM; validate output instead

**Real-World Example: Why This Matters**

Imagine your team uses these patterns:
- Guard clauses for early returns (not nested ifs)
- List comprehensions over manual loops
- Context managers for resource handling
- f-strings over `.format()`

An LLM might generate perfectly valid alternatives:
- Nested if-else chains (valid, not your style)
- For loops with manual appends (valid, not your style)
- Try-finally blocks (valid, not your style)
- .format() calls (valid, not your style)

Marky learns these preferences from your codebase and can:
1. **During generation**: Guide the LLM toward idiomatic patterns
2. **During validation**: Flag deviations with confidence scores
3. **During review**: Explain why code is unexpected
4. **For training**: Help fine-tune models on your patterns

**The Marky Approach**

Rather than debating "right" vs. "wrong" code style, Marky asks: **"What does this codebase do?"** and **"Does this code match those patterns?"**

This shifts the conversation from:
- "That's wrong" → "That's not how we do it"
- "Use this style" → "Your code uses different patterns than training"
- "Bad practice" → "Low confidence match to learned patterns"

The result: objective, data-driven style validation that teams can understand and trust.

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
- <1 minutes for 1000 files

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
> uv run python -m src validate examples/pytest/semantic_model.py src/__main__.py
Built marky @ file:///.../marky
Uninstalled 1 package in 0.21ms
Installed 1 package in 0.45ms
Loading model: examples/pytest/semantic_model.py
Validating code: src/__main__.py

Extracted 71 semantic patterns
First 20 patterns: ['init-method', 'function-transformer', 'if-empty-check', 'return-none', 'function-transformer', 'guard-clause', 'return-list', 'guard-clause', 'string-format', 'return-computed', 'function-transformer', 'if-empty-check', 'return-none', 'context-manager', 'string-format', 'context-manager', 'string-format', 'function-transformer', 'return-computed', 'loop-enumerate']
Model order: 2
Model has 211 pattern sequences

Validation Result (Semantic Model):
  Valid: True
  Confidence: 0.373
  Pattern sequences checked: 15
  Known transitions: 9/15

  ✓ Matching sequences (9):
    1. function-transformer → if-empty-check → return-none (0.423) @ line 118:12
    2. if-empty-check → return-none → function-transformer (0.370) @ line 135:4
    3. return-none → function-transformer → guard-clause (0.275) @ line 138:12
    4. guard-clause → return-list → guard-clause (1.000) @ line 143:8
    5. string-format → return-computed → function-transformer (0.714) @ line 149:4
    6. return-computed → function-transformer → if-empty-check (0.056) @ line 158:8
    7. function-transformer → if-empty-check → return-none (0.423) @ line 160:12

  ✗ Non-matching sequences (6):
    1. init-method → function-transformer → if-empty-check @ line 116:8
       Expected one of: return-computed, if-type-check, unpacking
    2. function-transformer → guard-clause → return-list @ line 139:16
       Expected one of: return-computed, return-none, return-bool
    3. return-list → guard-clause → string-format
       Expected one of: return-list
    4. Unknown sequence: guard-clause → string-format @ line 145:12
    5. if-empty-check → return-none → context-manager
       Expected one of: function-transformer, return-computed, guard-clause
    ... and 1 more

  Summary:
    Unique patterns found: 23
    Coverage: 9/15 transitions (60.0%)
    Issues: 4 unexpected, 2 unknown context
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
- Training: sub-second per file

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
git clone https://github.com/roobie/marky
cd marky
uv sync
```

**Training Your First Model**
```bash
# Train on your codebase
uv run python -m src train /path/to/your/code models/

# Or on specific patterns
uv run python -m src train /path/to/code models/ --model-type semantic --order 2
```

**Running Validation**
```bash
# Validate a file
uv run python -m src validate models/semantic_model.py your_file.py

# See statistics
uv run python -m src stats models/semantic_model.py

# Try the demo
uv run python -m src demo
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

### 14. Future explorations

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
- Next-edit suggestions
- Click to navigate to pattern source
- Suggestions for pattern improvements

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
