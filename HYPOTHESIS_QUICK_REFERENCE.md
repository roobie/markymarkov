# Hypothesis Property Testing Quick Reference

**For:** Marky Development Team  
**Date:** February 8, 2026  
**Files:** `model_types.py`, `test_model_types_properties.py`

## What's Property-Based Testing?

**One sentence:** Instead of testing specific values, test invariants that should hold for ALL valid inputs.

**Visual example:**

```
Manual Testing:              Property Testing:
─────────────────           ─────────────────
test_prob_0_5 ──────┐       @given(st.floats(0, 1))
test_prob_0_9 ──────┼──→    def test_prob_bounds(p):
test_prob_0_0 ──────┤        assert 0 ≤ p ≤ 1
test_prob_1_0 ──────┘
                              → Tests 1,000s of values
                              → Finds edge cases
                              → Prevents regression
```

## Why Use It for Marky?

Our dataclasses have **invariants** that must ALWAYS be true:

| Class | Invariant |
|-------|-----------|
| `NextNodeSuggestion` | `0 ≤ probability ≤ 1` |
| `NextPatternSuggestion` | `0 ≤ probability ≤ 1` AND `confidence in {HIGH, MEDIUM, LOW}` |
| `ASTContext` | `to_state(n).length == n` AND `to_state(n)` is all strings |
| `ValidationResult` | `0 ≤ confidence_score ≤ 1` AND `warnings` is not None |
| `SemanticNode` | Two equal nodes have equal hashes |

Property tests **guarantee** these invariants survive changes.

## Quick Start: Writing a Property Test

### 1. Import Hypothesis
```python
from hypothesis import given, settings
from hypothesis import strategies as st
from src.interfaces.model_types import NextNodeSuggestion
```

### 2. Write the Property
```python
@given(
    probability=st.floats(min_value=0.0, max_value=1.0),
    confidence=st.sampled_from(['HIGH', 'MEDIUM', 'LOW'])
)
def test_suggestion_always_valid(probability, confidence):
    """Property: All valid suggestions have probability in [0, 1]."""
    suggestion = NextNodeSuggestion('If', probability, confidence)
    
    # This must ALWAYS be true, for any generated input
    assert 0.0 <= suggestion.probability <= 1.0
```

### 3. Run It
```bash
pytest tests/interfaces/test_model_types_properties.py::test_suggestion_always_valid -v
```

**Output:**
```
test_suggestion_always_valid PASSED                                    [100%]
✓ 100 examples passed
```

## Common Strategies

### Generate Basic Types
```python
st.integers()                           # Any integer
st.integers(min_value=0, max_value=10)  # 0-10
st.floats(min_value=0.0, max_value=1.0) # 0.0-1.0
st.text()                               # Any string
st.text(min_size=1)                     # Non-empty string
st.booleans()                           # True or False
```

### Generate Collections
```python
st.lists(st.integers())                 # List of integers
st.lists(st.text(), min_size=1)         # Non-empty list of strings
st.dictionaries(st.text(), st.integers()) # Dict[str, int]
```

### Choose From Specific Values
```python
st.sampled_from(['HIGH', 'MEDIUM', 'LOW'])
st.sampled_from(list(CodePattern))
```

### Combine Strategies
```python
st.builds(
    SemanticNode,
    pattern=st.sampled_from(list(CodePattern)),
    context=st.dictionaries(st.text(), st.integers())
)
```

## Common Patterns

### Pattern 1: Bounds Checking
```python
@given(st.floats(min_value=0.0, max_value=1.0))
def test_confidence_in_bounds(score):
    result = ValidationResult(True, score)
    assert 0.0 <= result.confidence_score <= 1.0
```

### Pattern 2: Method Consistency
```python
@given(st.lists(st.text()))
def test_issue_count_formula(warnings):
    result = ValidationResult(True, 0.9, warnings=warnings)
    expected = len(warnings)
    assert result.issue_count() >= expected
```

### Pattern 3: State Preservation
```python
@given(
    parent=st.text(min_size=1),
    current=st.text(min_size=1),
    ancestors=st.lists(st.text())
)
def test_depth_formula(parent, current, ancestors):
    ctx = ASTContext(parent, current, ancestors)
    assert ctx.get_depth() == len(ancestors) + 1
```

### Pattern 4: Collection Operations
```python
@given(st.lists(
    st.builds(SemanticNode, pattern=st.sampled_from(list(CodePattern)))
))
def test_nodes_hashable(nodes):
    # Should not raise
    s = set(nodes)
    assert len(s) <= len(nodes)
```

## Debugging Failed Properties

### Example Failure
```
Falsifying example: test_prob_bounds(probability=-0.1, confidence='HIGH')
AssertionError: assert 0.0 <= -0.1 <= 1.0
```

**Fix:** Constrain the strategy:
```python
# WRONG: allows negative values
@given(st.floats())

# RIGHT: only valid range
@given(st.floats(min_value=0.0, max_value=1.0))
```

### Example Failure 2
```
Falsifying example: test_depth_formula(parent='', current='If', ancestors=[])
ValueError: parent_type cannot be empty
```

**Fix:** Generate valid inputs:
```python
# WRONG: allows empty strings
@given(st.text())

# RIGHT: only non-empty strings
@given(st.text(min_size=1))
```

## Performance Tips

### Reduce Examples for Quick Feedback
```python
@settings(max_examples=50)  # Default is 100
@given(st.integers())
def test_something(x):
    assert True
```

### Exclude Slow Generations
```python
# Don't generate huge lists during CI
@settings(max_examples=50)
@given(st.lists(st.text(), max_size=5))
def test_something(items):
    pass
```

### Filter Invalid Cases
```python
@given(st.integers())
def test_positive_numbers(x):
    assume(x > 0)  # Skip non-positive values
    assert x > 0
```

## File Structure

```
tests/
├── interfaces/
│   ├── test_model_types.py              # Existing: unit tests (95+ tests)
│   └── test_model_types_properties.py   # New: property tests (25+ properties)
│
docs/
├── HYPOTHESIS_PROPERTY_TESTING_PLAN.md  # Full specification
├── HYPOTHESIS_ANALYSIS_SUMMARY.md       # Overview and strategy
└── HYPOTHESIS_QUICK_REFERENCE.md        # This file
```

## Running Tests

```bash
# Run all property tests
pytest tests/interfaces/test_model_types_properties.py -v

# Run specific property
pytest tests/interfaces/test_model_types_properties.py::test_suggestion_always_valid -v

# Run with verbose output
pytest tests/interfaces/test_model_types_properties.py -vv

# Run both unit and property tests
pytest tests/interfaces/ -v
```

## Expected Output

```
test_model_types_properties.py::test_probability_bounds PASSED        [ 5%]
test_model_types_properties.py::test_confidence_valid PASSED          [10%]
test_model_types_properties.py::test_to_state_returns_correct_length PASSED [15%]
test_model_types_properties.py::test_issue_count_formula PASSED       [20%]
test_model_types_properties.py::test_semantic_node_equality_and_hash PASSED [25%]
...
======================== 25 passed in 2.34s ========================
```

## Checklists

### Writing a New Property
- [ ] What invariant should always be true?
- [ ] What inputs make sense? (strategy)
- [ ] Does the test pass? (run pytest)
- [ ] Does it catch bugs? (try intentional bugs)
- [ ] Is it readable? (clear docstring)

### Code Review Checklist
- [ ] Property clearly states what should be true
- [ ] Strategies are appropriately constrained
- [ ] No `assume()` filtering out >30% of inputs
- [ ] Docstring explains the property
- [ ] Test passes with 100+ examples

## Common Gotchas

### ❌ DON'T: Use unconstrained strategies
```python
# WRONG: can generate any integer including huge ones
@given(st.integers())
def test_something(x):
    ...
```

### ✅ DO: Constrain to valid ranges
```python
# RIGHT: only valid values
@given(st.integers(min_value=1, max_value=3))
def test_something(order):
    ...
```

### ❌ DON'T: Filter too much with assume()
```python
# WRONG: wastes 90% of generated inputs
@given(st.integers())
def test_positive(x):
    assume(x > 0)  # Most integers aren't > 0
```

### ✅ DO: Use appropriate strategies
```python
# RIGHT: generates only positive integers
@given(st.integers(min_value=1))
def test_positive(x):
```

### ❌ DON'T: Test implementation details
```python
# WRONG: tests how it's stored, not what it does
@given(st.text())
def test_warning_list(w):
    result = ValidationResult(True, 0.9, warnings=[w])
    assert result.warnings[0] is w  # Too specific!
```

### ✅ DO: Test contract/behavior
```python
# RIGHT: tests the observable behavior
@given(st.text())
def test_warning_preserved(w):
    result = ValidationResult(True, 0.9, warnings=[w])
    assert w in result.warnings  # What matters
```

## Links

- **Full Plan:** Read `HYPOTHESIS_PROPERTY_TESTING_PLAN.md` for detailed property specifications
- **Summary:** Read `HYPOTHESIS_ANALYSIS_SUMMARY.md` for strategic overview
- **Hypothesis Docs:** https://hypothesis.readthedocs.io/
- **Strategies:** https://hypothesis.readthedocs.io/en/latest/reference/strategies.html

## Questions?

Refer to:
1. This quick reference for syntax/patterns
2. `HYPOTHESIS_PROPERTY_TESTING_PLAN.md` for property details
3. Hypothesis official docs for advanced features
4. Existing tests in `test_model_types.py` for examples

---

**Next Step:** Implement the properties in `test_model_types_properties.py` using this guide!

