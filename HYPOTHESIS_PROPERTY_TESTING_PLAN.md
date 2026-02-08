# Hypothesis Property-Based Testing Plan for Marky

**Date:** February 8, 2026  
**Purpose:** Document which properties in the Marky codebase should be tested using the Hypothesis library for more robust property-based testing.

## Overview

Property-based testing is a technique where, instead of writing specific test cases, you write properties that should hold true for all inputs. **Hypothesis** is a Python library that generates random inputs to test these properties, helping find edge cases that manual tests might miss.

The Marky codebase has several dataclasses and methods where property-based testing would significantly improve test coverage and robustness.

---

## 1. NextNodeSuggestion Properties

### File
`src/interfaces/model_types.py` → `NextNodeSuggestion` class

### Existing Tests
Manual unit tests covering happy path and basic validation.

### Property-Based Testing Opportunities

#### Property 1: Probability Bounds Invariant
**What it tests:** Any valid `NextNodeSuggestion` must have a probability in `[0.0, 1.0]`.

```python
@given(
    node_type=st.text(min_size=1),  # non-empty string
    probability=st.floats(min_value=0.0, max_value=1.0),
    confidence=st.sampled_from(['HIGH', 'MEDIUM', 'LOW'])
)
def test_probability_always_in_bounds(node_type, probability, confidence):
    """Property: Valid suggestions always have probability in [0, 1]."""
    suggestion = NextNodeSuggestion(node_type, probability, confidence)
    assert 0.0 <= suggestion.probability <= 1.0
```

**Why this matters:** Ensures the invariant is preserved across all input combinations.

#### Property 2: Confidence Level Invariant
**What it tests:** Only valid confidence levels are accepted.

```python
@given(
    node_type=st.text(min_size=1),
    probability=st.floats(min_value=0.0, max_value=1.0),
    confidence=st.sampled_from(['HIGH', 'MEDIUM', 'LOW'])
)
def test_confidence_always_valid(node_type, probability, confidence):
    """Property: Confidence is always one of the three valid levels."""
    suggestion = NextNodeSuggestion(node_type, probability, confidence)
    assert suggestion.confidence in ('HIGH', 'MEDIUM', 'LOW')
```

#### Property 3: Common Patterns List Consistency
**What it tests:** Common patterns list is always a list and never None.

```python
@given(
    node_type=st.text(min_size=1),
    probability=st.floats(min_value=0.0, max_value=1.0),
    common_patterns=st.lists(st.text(min_size=1))
)
def test_common_patterns_always_list(node_type, probability, common_patterns):
    """Property: common_patterns is always a list, never None."""
    suggestion = NextNodeSuggestion(
        node_type, 
        probability, 
        'HIGH',
        common_patterns
    )
    assert isinstance(suggestion.common_patterns, list)
    assert suggestion.common_patterns is not None
```

#### Property 4: is_high_confidence Correctness
**What it tests:** The `is_high_confidence()` method returns True iff confidence is 'HIGH'.

```python
@given(
    confidence=st.sampled_from(['HIGH', 'MEDIUM', 'LOW'])
)
def test_is_high_confidence_correctness(confidence):
    """Property: is_high_confidence() is true iff confidence == 'HIGH'."""
    suggestion = NextNodeSuggestion('If', 0.5, confidence)
    assert suggestion.is_high_confidence() == (confidence == 'HIGH')
```

---

## 2. NextPatternSuggestion Properties

### File
`src/interfaces/model_types.py` → `NextPatternSuggestion` class

### Property-Based Testing Opportunities

#### Property 1: Probability Bounds
**What it tests:** Probability always in `[0.0, 1.0]` (same invariant as NextNodeSuggestion).

```python
@given(
    probability=st.floats(min_value=0.0, max_value=1.0),
    description=st.text(min_size=1),
    code_template=st.text(min_size=1)
)
def test_pattern_suggestion_probability_bounds(probability, description, code_template):
    """Property: Pattern suggestion probability always in [0, 1]."""
    suggestion = NextPatternSuggestion(
        CodePattern.LOOP_FILTER,
        probability,
        description,
        code_template,
        'HIGH'
    )
    assert 0.0 <= suggestion.probability <= 1.0
```

#### Property 2: Non-Empty Strings
**What it tests:** Description and code_template are always non-empty strings.

```python
@given(
    description=st.text(min_size=1),
    code_template=st.text(min_size=1)
)
def test_pattern_strings_never_empty(description, code_template):
    """Property: Description and template are never empty."""
    suggestion = NextPatternSuggestion(
        CodePattern.IF_NONE_CHECK,
        0.5,
        description,
        code_template,
        'MEDIUM'
    )
    assert suggestion.description != ''
    assert suggestion.code_template != ''
    assert len(suggestion.description) > 0
    assert len(suggestion.code_template) > 0
```

#### Property 3: pattern_name() and pattern_value() Consistency
**What it tests:** `pattern_name()` returns enum member name, `pattern_value()` returns kebab-case.

```python
@given(pattern=st.sampled_from(list(CodePattern)))
def test_pattern_name_value_consistency(pattern):
    """Property: pattern_name() and pattern_value() are consistent."""
    suggestion = NextPatternSuggestion(
        pattern, 0.5, 'desc', 'template', 'HIGH'
    )
    name = suggestion.pattern_name()
    value = suggestion.pattern_value()
    
    # Name should be uppercase with underscores
    assert name == name.upper()
    assert '_' in name or len(name.split('_')) == 1
    
    # Value should be lowercase with hyphens
    assert value == value.lower()
    assert '-' in value or '_' not in value
```

---

## 3. ASTContext Properties

### File
`src/interfaces/model_types.py` → `ASTContext` class

### Property-Based Testing Opportunities

#### Property 1: to_state() Returns Correct Tuple Length
**What it tests:** `to_state(order=n)` returns a tuple of exactly `n` elements.

```python
@given(
    parent_type=st.text(min_size=1),
    current_node=st.text(min_size=1),
    ancestor_chain=st.lists(st.text(min_size=1)),
    order=st.integers(min_value=1, max_value=3)
)
def test_to_state_returns_correct_length(parent_type, current_node, ancestor_chain, order):
    """Property: to_state(order=n) always returns a tuple of length n."""
    ctx = ASTContext(parent_type, current_node, ancestor_chain)
    state = ctx.to_state(order=order)
    
    assert isinstance(state, tuple)
    assert len(state) == order
```

#### Property 2: to_state() Returns String Tuples
**What it tests:** All elements in the tuple are strings (node type names).

```python
@given(
    parent_type=st.text(min_size=1),
    current_node=st.text(min_size=1),
    ancestor_chain=st.lists(st.text(min_size=1)),
    order=st.sampled_from([1, 2, 3])
)
def test_to_state_returns_strings(parent_type, current_node, ancestor_chain, order):
    """Property: to_state() returns tuples of strings only."""
    ctx = ASTContext(parent_type, current_node, ancestor_chain)
    state = ctx.to_state(order=order)
    
    for element in state:
        assert isinstance(element, str)
        assert len(element) > 0  # No empty strings
```

#### Property 3: to_state() Preserves Order Information
**What it tests:** Higher order states contain all information from lower orders.

```python
@given(
    parent_type=st.text(min_size=1),
    current_node=st.text(min_size=1),
    ancestor_chain=st.lists(st.text(min_size=1), max_size=10)
)
def test_to_state_order_subset_property(parent_type, current_node, ancestor_chain):
    """Property: state[order=2] contains state[order=1] as suffix."""
    ctx = ASTContext(parent_type, current_node, ancestor_chain)
    
    state1 = ctx.to_state(order=1)
    state2 = ctx.to_state(order=2)
    state3 = ctx.to_state(order=3)
    
    # Current node should be the last element in all
    assert state1[-1] == current_node
    assert state2[-1] == current_node
    assert state3[-1] == current_node
    
    # Higher orders should contain lower orders as suffix
    assert state2[-1:] == state1
    assert state3[-1:] == state1
```

#### Property 4: get_depth() Equals Ancestor Chain Length + 1
**What it tests:** Depth is always `len(ancestor_chain) + 1`.

```python
@given(ancestor_chain=st.lists(st.text(min_size=1)))
def test_get_depth_formula(ancestor_chain):
    """Property: get_depth() == len(ancestor_chain) + 1."""
    ctx = ASTContext('Parent', 'Current', ancestor_chain)
    expected_depth = len(ancestor_chain) + 1
    assert ctx.get_depth() == expected_depth
```

#### Property 5: push() Creates Valid Child Context
**What it tests:** `push(new_type)` creates a context with correct depth and structure.

```python
@given(
    parent_type=st.text(min_size=1),
    current_node=st.text(min_size=1),
    ancestor_chain=st.lists(st.text(min_size=1), max_size=5),
    new_node_type=st.text(min_size=1)
)
def test_push_creates_valid_child(parent_type, current_node, ancestor_chain, new_node_type):
    """Property: push() creates a valid child context with correct structure."""
    parent_ctx = ASTContext(parent_type, current_node, ancestor_chain)
    child_ctx = parent_ctx.push(new_node_type)
    
    # Child's parent should be parent's current
    assert child_ctx.parent_type == parent_ctx.current_node
    
    # Child's current should be the new node type
    assert child_ctx.current_node == new_node_type
    
    # Child's depth should be parent's depth + 1
    assert child_ctx.get_depth() == parent_ctx.get_depth() + 1
    
    # Child's ancestor chain should extend parent's chain
    assert child_ctx.ancestor_chain == parent_ctx.ancestor_chain + [parent_ctx.parent_type]
```

#### Property 6: push() Preserves Metadata
**What it tests:** Metadata is copied (not shared) when pushing.

```python
@given(
    metadata_values=st.dictionaries(
        st.text(min_size=1, max_size=10),
        st.text(min_size=1, max_size=20),
        min_size=0,
        max_size=5
    )
)
def test_push_preserves_metadata(metadata_values):
    """Property: push() copies metadata to child (not shared reference)."""
    parent_ctx = ASTContext('Parent', 'Current', metadata=metadata_values)
    child_ctx = parent_ctx.push('Child')
    
    # Metadata should be equal
    assert child_ctx.metadata == parent_ctx.metadata
    
    # But should be different objects
    assert child_ctx.metadata is not parent_ctx.metadata
    
    # Modifying child's metadata shouldn't affect parent's
    if metadata_values:  # Only if there's metadata to modify
        child_ctx.metadata['test_key'] = 'test_value'
        assert 'test_key' not in parent_ctx.metadata
```

---

## 4. ValidationResult Properties

### File
`src/interfaces/model_types.py` → `ValidationResult` class

### Property-Based Testing Opportunities

#### Property 1: Confidence Score Bounds
**What it tests:** Confidence score always in `[0.0, 1.0]`.

```python
@given(
    confidence_score=st.floats(min_value=0.0, max_value=1.0),
    is_valid=st.booleans()
)
def test_validation_confidence_bounds(confidence_score, is_valid):
    """Property: Confidence score always in [0, 1]."""
    result = ValidationResult(is_valid, confidence_score)
    assert 0.0 <= result.confidence_score <= 1.0
```

#### Property 2: Lists are Always Lists
**What it tests:** warnings, errors, suggestions are always lists, never None.

```python
@given(
    warnings=st.lists(st.text()),
    errors=st.lists(st.text()),
    suggestions=st.lists(st.text())
)
def test_validation_lists_never_none(warnings, errors, suggestions):
    """Property: All list fields are always lists, never None."""
    result = ValidationResult(
        True,
        0.9,
        warnings=warnings,
        errors=errors,
        suggestions=suggestions
    )
    assert isinstance(result.warnings, list)
    assert isinstance(result.errors, list)
    assert isinstance(result.suggestions, list)
    assert result.warnings is not None
    assert result.errors is not None
    assert result.suggestions is not None
```

#### Property 3: issue_count() Consistency
**What it tests:** `issue_count()` equals `len(warnings) + len(errors)`.

```python
@given(
    warnings=st.lists(st.text()),
    errors=st.lists(st.text())
)
def test_issue_count_formula(warnings, errors):
    """Property: issue_count() == len(warnings) + len(errors)."""
    result = ValidationResult(True, 0.9, warnings=warnings, errors=errors)
    expected = len(warnings) + len(errors)
    assert result.issue_count() == expected
```

#### Property 4: all_issues() Contains All Problems
**What it tests:** `all_issues()` contains all errors and warnings.

```python
@given(
    warnings=st.lists(st.text(min_size=1), max_size=10),
    errors=st.lists(st.text(min_size=1), max_size=10)
)
def test_all_issues_completeness(warnings, errors):
    """Property: all_issues() contains all warnings and errors."""
    result = ValidationResult(True, 0.9, warnings=warnings, errors=errors)
    issues = result.all_issues()
    
    # All errors should be in issues
    for error in errors:
        assert error in issues
    
    # All warnings should be in issues
    for warning in warnings:
        assert warning in issues
    
    # Should have exactly the right count
    assert len(issues) == len(warnings) + len(errors)
```

#### Property 5: has_warnings() and has_errors() Correctness
**What it tests:** Boolean flags correctly reflect list contents.

```python
@given(
    warnings=st.lists(st.text()),
    errors=st.lists(st.text())
)
def test_has_warnings_errors_correctness(warnings, errors):
    """Property: has_warnings()/has_errors() match list contents."""
    result = ValidationResult(True, 0.9, warnings=warnings, errors=errors)
    
    # has_warnings() should be True iff warnings is not empty
    assert result.has_warnings() == (len(warnings) > 0)
    
    # has_errors() should be True iff errors is not empty
    assert result.has_errors() == (len(errors) > 0)
```

---

## 5. SemanticNode Properties

### File
`src/interfaces/model_types.py` → `SemanticNode` class

### Property-Based Testing Opportunities

#### Property 1: Hashable and Equality Consistent
**What it tests:** Nodes with same pattern and context are equal and have same hash.

```python
@given(
    pattern=st.sampled_from(list(CodePattern)),
    context=st.dictionaries(
        st.text(min_size=1),
        st.integers() | st.text()
    )
)
def test_semantic_node_equality_and_hash(pattern, context):
    """Property: Equal nodes have equal hashes."""
    node1 = SemanticNode(pattern, context)
    node2 = SemanticNode(pattern, context)
    
    # Equal nodes must have equal hashes
    if node1 == node2:
        assert hash(node1) == hash(node2)
```

#### Property 2: Hashable - Can Be Used in Sets
**What it tests:** SemanticNodes can be collected in sets without error.

```python
@given(st.lists(
    st.builds(
        SemanticNode,
        pattern=st.sampled_from(list(CodePattern))
    ),
    max_size=20
))
def test_semantic_node_set_operations(nodes):
    """Property: SemanticNode can be used in sets."""
    # Should not raise any errors
    node_set = set(nodes)
    
    # Every node should be retrievable
    for node in nodes:
        assert node in node_set
```

#### Property 3: pattern_name() and pattern_value() Consistent
**What it tests:** Name is enum member name, value is kebab-case equivalent.

```python
@given(pattern=st.sampled_from(list(CodePattern)))
def test_semantic_node_pattern_consistency(pattern):
    """Property: pattern_name() and pattern_value() are consistent."""
    node = SemanticNode(pattern)
    name = node.pattern_name()
    value = node.pattern_value()
    
    # Name should be uppercase with underscores (enum format)
    assert name == name.upper()
    
    # Value should be lowercase with hyphens (kebab-case)
    assert value == value.lower()
```

#### Property 4: get_context() Returns Correct Values
**What it tests:** `get_context()` returns stored values and defaults correctly.

```python
@given(
    context=st.dictionaries(st.text(min_size=1), st.integers()),
    default_value=st.integers()
)
def test_semantic_node_get_context(context, default_value):
    """Property: get_context() returns value or default."""
    node = SemanticNode(CodePattern.LOOP_FILTER, context)
    
    # Existing keys should return their values
    for key, value in context.items():
        assert node.get_context(key) == value
    
    # Missing keys should return default
    missing_key = "definitely_not_in_context_" + str(default_value)
    assert node.get_context(missing_key, default_value) == default_value
```

#### Property 5: has_context() Correctness
**What it tests:** `has_context()` returns True iff key exists in context.

```python
@given(context=st.dictionaries(st.text(min_size=1), st.integers()))
def test_semantic_node_has_context(context):
    """Property: has_context() is True iff key exists."""
    node = SemanticNode(CodePattern.LOOP_FILTER, context)
    
    # Existing keys should return True
    for key in context.keys():
        assert node.has_context(key) is True
    
    # Non-existing keys should return False
    missing_key = "definitely_not_in_context"
    assert node.has_context(missing_key) is False
```

---

## 6. Cross-Module Properties

### File
`src/interfaces/model_types.py` → Interactions between classes

#### Property 1: Model Query Consistency
**What it tests:** ASTContext state can be used as a dictionary key in Markov models.

```python
@given(
    parent_type=st.text(min_size=1),
    current_node=st.text(min_size=1),
    ancestor_chain=st.lists(st.text(min_size=1))
)
def test_ast_context_state_as_dict_key(parent_type, current_node, ancestor_chain):
    """Property: ASTContext states work as Markov model keys."""
    ctx1 = ASTContext(parent_type, current_node, ancestor_chain)
    ctx2 = ASTContext(parent_type, current_node, ancestor_chain)
    
    state1 = ctx1.to_state(order=2)
    state2 = ctx2.to_state(order=2)
    
    # Identical contexts should produce identical states
    assert state1 == state2
    
    # States should be usable as dict keys
    model = {state1: [NextNodeSuggestion('If', 0.5, 'HIGH')]}
    assert state2 in model
    assert model[state2] is model[state1]
```

#### Property 2: Suggestion Validation Compatibility
**What it tests:** Suggestions produced from contexts are always valid.

```python
@given(
    node_type=st.text(min_size=1),
    probability=st.floats(min_value=0.0, max_value=1.0)
)
def test_suggestion_from_context_always_valid(node_type, probability):
    """Property: Suggestions produced from contexts are always valid."""
    # Simulate creating a suggestion from model query
    suggestion = NextNodeSuggestion(
        node_type=node_type,
        probability=probability,
        confidence='HIGH'
    )
    
    # Should always be valid
    assert 0.0 <= suggestion.probability <= 1.0
    assert suggestion.confidence in ('HIGH', 'MEDIUM', 'LOW')
```

---

## 7. Implementation Strategy

### Phase 1: Add hypothesis to test dependencies
```bash
uv add --dev hypothesis
```

### Phase 2: Create property tests file
Create `tests/interfaces/test_model_types_properties.py` with all property tests organized by class.

### Phase 3: Run and refine
```bash
pytest tests/interfaces/test_model_types_properties.py -v
```

### Phase 4: Integration with existing tests
Keep existing unit tests for:
- Edge case documentation
- Clear failure messages
- Specific regression tests

Augment with property tests for:
- Invariant verification
- Exhaustive input coverage
- Finding unexpected interactions

---

## 8. Expected Benefits

1. **Better coverage of edge cases** - Hypothesis will generate unusual but valid inputs that manual tests might miss
2. **Regression detection** - Properties encode invariants that must always hold
3. **Clearer documentation** - Properties explicitly state what should be true
4. **Reduced manual test code** - Fewer hand-written test cases needed
5. **Confidence in refactoring** - Properties ensure invariants survive changes

---

## 9. Hypothesis Features Used

From the quickstart, we'll use:

- **`@given` decorator** - Inject random inputs
- **`st.text()`, `st.integers()`, `st.floats()`** - Basic strategies
- **`st.lists()`, `st.dictionaries()`** - Collection strategies
- **`st.sampled_from()`** - Choose from enum values
- **`st.builds()`** - Generate instances of classes
- **`assume()`** - Filter invalid inputs (for complex constraints)

---

## 10. Success Metrics

- [ ] Property tests written for all 5 dataclasses
- [ ] All properties pass with default settings (100 examples)
- [ ] No conflicts with existing unit tests
- [ ] Test execution time < 5 seconds
- [ ] Documentation updated with property test results

---

## References

- Hypothesis Quickstart: https://hypothesis.readthedocs.io/en/latest/quickstart.html
- Strategies Reference: https://hypothesis.readthedocs.io/en/latest/reference/strategies.html
- Property-Based Testing Concepts: https://hypothesis.readthedocs.io/en/latest/explanation/index.html

