# Summary: Hypothesis Property-Based Testing Analysis

**Generated:** February 8, 2026  
**Status:** Planning Complete  
**Related Document:** `HYPOTHESIS_PROPERTY_TESTING_PLAN.md`  
**Mindmap Node:** [37]

## Quick Summary

I've analyzed the Marky codebase for opportunities to apply Hypothesis property-based testing. The analysis identified **5 primary dataclasses** and **30+ distinct properties** that should be tested to ensure robustness.

## What is Property-Based Testing?

Instead of writing specific test cases like:
```python
# Traditional: specific example
def test_suggestion_with_high_probability():
    suggestion = NextNodeSuggestion('If', 0.9, 'HIGH')
    assert suggestion.probability <= 1.0
```

Property-based testing writes invariants:
```python
# Property: all valid suggestions have probability in [0, 1]
@given(
    probability=st.floats(min_value=0.0, max_value=1.0),
    confidence=st.sampled_from(['HIGH', 'MEDIUM', 'LOW'])
)
def test_suggestion_probability_always_valid(probability, confidence):
    suggestion = NextNodeSuggestion('If', probability, confidence)
    assert 0.0 <= suggestion.probability <= 1.0
```

Hypothesis generates **hundreds of random inputs** to test the property with unusual edge cases that humans wouldn't write manually.

## Target Classes and Property Count

| Class | File | Properties | Focus Areas |
|-------|------|-----------|------------|
| **NextNodeSuggestion** | `model_types.py` | 4 | Probability bounds, confidence invariant, list consistency, method correctness |
| **NextPatternSuggestion** | `model_types.py` | 3 | Probability bounds, non-empty strings, name/value consistency |
| **ASTContext** | `model_types.py` | 6 | State tuple length, element types, order preservation, depth formula, push() validity, metadata copying |
| **ValidationResult** | `model_types.py` | 5 | Confidence bounds, list non-nullability, issue count formula, completeness, boolean flags |
| **SemanticNode** | `model_types.py` | 5 | Equality & hash consistency, set operations, pattern consistency, context lookup, context checking |
| **Cross-Module** | `model_types.py` | 2 | State as dict key, suggestion validity from context |
| **TOTAL** | — | **25+** | — |

## Key Properties by Category

### 1. **Bounds Invariants** (5 properties)
Ensure values stay within valid ranges:
- Probability always in [0.0, 1.0]
- Confidence score always in [0.0, 1.0]
- Confidence level always one of: HIGH, MEDIUM, LOW

### 2. **Non-Null Consistency** (4 properties)
Ensure collections and critical fields are never None:
- common_patterns list always exists
- warnings, errors, suggestions lists always exist
- Essential strings (description, code_template) never empty

### 3. **Method Correctness** (8 properties)
Ensure methods produce correct results:
- `is_high_confidence()` returns True iff confidence == 'HIGH'
- `issue_count()` equals len(warnings) + len(errors)
- `all_issues()` contains all warnings and errors
- `pattern_name()` returns proper enum member name
- `pattern_value()` returns kebab-case variant
- `to_state(order=n)` returns tuple of exactly n elements
- `get_context()` returns value or default correctly
- `has_context()` returns True iff key exists

### 4. **State Preservation** (4 properties)
Ensure complex operations preserve invariants:
- `to_state()` returns strings only
- Higher order states contain lower order as suffix
- `push()` creates valid child with correct depth
- `push()` copies metadata (not shared reference)
- Identical contexts produce identical states

### 5. **Mathematical Relationships** (3 properties)
Ensure formulas always hold:
- `get_depth() == len(ancestor_chain) + 1`
- `issue_count() == len(warnings) + len(errors)`
- `all_issues()` length equals warning + error count

### 6. **Equality and Hashing** (2 properties)
Ensure objects work correctly in collections:
- Equal nodes have equal hashes (hash contract)
- Nodes work in sets without errors
- Nodes work as dictionary keys

## Why Hypothesis Improves Our Tests

### 1. Discovers Edge Cases
**Example:** Our manual test might check `NextNodeSuggestion('If', 0.5, 'HIGH')`, but Hypothesis generates:
- Probability = 0.0 (boundary)
- Probability = 1.0 (boundary)
- Probability = 0.3333333333... (floating point weirdness)
- Node type = very long string
- Node type = unicode with special characters

### 2. Prevents Regressions
Once a property is written, Hypothesis ensures it never breaks:
```python
# This property would have caught a hypothetical bug:
# "What if someone accidentally changed probability range to [0, 100]?"
```

### 3. Documents Expected Behavior
Properties serve as executable specifications:
> "A valid ASTContext always has depth == len(ancestor_chain) + 1"

### 4. Reduces Manual Test Code
Instead of writing 50 specific test cases, write 5 properties that cover all combinations.

### 5. Tests Interactions
Cross-module properties ensure classes work together:
- States can be dictionary keys in Markov models
- Suggestions produced from contexts are always valid

## Implementation Roadmap

### Phase 1: Setup (15 minutes)
```bash
uv add --dev hypothesis
```

### Phase 2: Create Property Tests (1-2 hours)
Create `tests/interfaces/test_model_types_properties.py` with:
- 4 properties for NextNodeSuggestion
- 3 properties for NextPatternSuggestion
- 6 properties for ASTContext
- 5 properties for ValidationResult
- 5 properties for SemanticNode
- 2 cross-module properties

### Phase 3: Verify and Debug (30 minutes)
```bash
pytest tests/interfaces/test_model_types_properties.py -v
# Should see all 25 properties passing
```

### Phase 4: Integration (15 minutes)
- Ensure existing tests still pass
- Run full test suite: `pytest tests/ -v`
- Check for any conflicts

### Phase 5: Documentation (15 minutes)
- Update test coverage reports
- Add note to development guide
- Sync MINDMAP [37]

**Total estimated time:** 2-3 hours for full implementation

## Expected Test Results

After implementation:
- ✓ All 25+ properties passing with 100 examples each
- ✓ No conflicts with existing 95+ unit tests
- ✓ Total test execution time remains < 10 seconds
- ✓ Stronger guarantee that invariants hold across all possible inputs

## Risk Mitigation

**Risk:** Hypothesis finds bugs we didn't know about  
**Mitigation:** This is actually desired—better to find them now!  
**Action:** Document any found bugs in issues, fix before merging

**Risk:** Property tests are slow  
**Mitigation:** Hypothesis runs 100 examples by default (configurable)  
**Action:** Use `@settings(max_examples=50)` if needed for CI speed

**Risk:** Properties are hard to understand  
**Mitigation:** Each property has clear docstring and example  
**Action:** Reference `HYPOTHESIS_PROPERTY_TESTING_PLAN.md` in code

## Hypothesis Framework Features

From the quickstart, we'll use:

| Feature | Purpose | Example |
|---------|---------|---------|
| `@given` | Inject random inputs | `@given(st.integers())` |
| `st.text()` | Generate strings | `st.text(min_size=1)` |
| `st.integers()` | Generate integers | `st.integers(min_value=0)` |
| `st.floats()` | Generate floats | `st.floats(min_value=0.0, max_value=1.0)` |
| `st.lists()` | Generate lists | `st.lists(st.text())` |
| `st.dictionaries()` | Generate dicts | `st.dictionaries(st.text(), st.integers())` |
| `st.sampled_from()` | Choose from options | `st.sampled_from(['HIGH', 'MEDIUM', 'LOW'])` |
| `st.builds()` | Create instances | `st.builds(SemanticNode, pattern=...)` |
| `assume()` | Filter inputs | `assume(x > 0)` |

## Next Steps

1. ✅ **Analysis Complete** - Properties identified and documented
2. **Phase 2.2 Task** - Implement property tests in code
3. **Integration** - Merge with existing test suite
4. **Documentation** - Update test coverage reports
5. **Maintenance** - Use properties as part of regular CI/CD

## References

- **Full Plan:** `HYPOTHESIS_PROPERTY_TESTING_PLAN.md`
- **Mindmap Node:** [37]
- **Hypothesis Docs:** https://hypothesis.readthedocs.io/
- **Quickstart:** https://hypothesis.readthedocs.io/en/latest/quickstart.html

---

**Recommendation:** Proceed with Phase 2 implementation of these property tests. The investment in property-based testing will pay dividends through better test coverage and fewer bugs in production.

