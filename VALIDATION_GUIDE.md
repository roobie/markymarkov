# CLI Validation Guide

## Quick Start

### Validate with AST Model
```bash
python -m src validate examples/python3/ast_model.py <code_file>
```

### Validate with Semantic Model  
```bash
python -m src validate examples/python3/semantic_model.py <code_file>
```

## Understanding the Output

### AST Model Output

```
Loading model: examples/python3/ast_model.py
Validating code: src/__main__.py

Extracted 2974 AST transitions
Model order: 2
Validation Result (AST Model):
  Valid: True
  Confidence: 0.514
  Transitions checked: 25
  Known transitions: 23
  Issues: 2
    - Unknown context: ...
    - Unexpected transition: ...
```

**What it means**:
- `Valid`: True if confidence > 0.1 OR no issues detected
- `Confidence`: Probability-weighted score (higher is better)
  - 0.0-0.3: Low confidence (unusual patterns)
  - 0.3-0.7: Medium confidence (common patterns)
  - 0.7-1.0: High confidence (well-matched)
- `Transitions checked`: First N transitions analyzed (max 25)
- `Known transitions`: How many matched the training data
- `Issues`: Problems found (unknown contexts, unexpected transitions)

### Semantic Model Output

```
Loading model: examples/python3/semantic_model.py
Validating code: src/__main__.py

Extracted 63 semantic patterns
First 20 patterns: [patterns...]
Model order: 2
Model has 585 pattern sequences

Validation Result (Semantic Model):
  Valid: True
  Confidence: 0.164
  Pattern sequences checked: 15
  Known transitions: 12/15

  ✓ Matching sequences:
    init-method → function-transformer → if-empty-check (0.075)
    function-transformer → if-empty-check → return-none (0.244)
    
  ✗ Non-matching sequences: 3
    return-list → guard-clause → string-format [got: return-list, return-computed, guard-clause]
```

**What it means**:
- `Valid`: True if any pattern sequences matched the training data
- `Confidence`: Average log probability of matched sequences
- `Pattern sequences checked`: First N pattern sequences analyzed
- `Known transitions`: How many pattern sequences were in training data
- `Matching sequences`: Patterns found in training data with their probabilities
- `Non-matching sequences`: Patterns not found, with alternatives shown

## Interpretation

### Good Validation Results
- ✅ Valid: True
- ✅ Confidence: > 0.3
- ✅ Matching sequences: > 70%

This means the code follows common patterns from the training data.

### Warning Signs
- ⚠️ Valid: False
- ⚠️ Confidence: < 0.2
- ⚠️ Most sequences unknown

The code uses unusual patterns not seen in training data. This might indicate:
- Code that doesn't follow common conventions
- Unconventional style
- Domain-specific patterns
- Bugs or anti-patterns

### What's NOT a Problem
- Having 1-2 unknown contexts is normal (edge cases)
- Unusual but valid code will show as Valid: False but with patterns detected
- Low confidence doesn't mean the code is wrong, just uncommon

## Examples

### Example 1: Common Code Pattern
```python
def process_items(items):
    result = []
    for item in items:
        if item > 0:
            result.append(item * 2)
    return result
```

**Result**: Valid: True, Confidence: 0.25+
**Why**: Uses common patterns: init-list, loop-filter, return-computed

### Example 2: Unusual Code
```python
def weird_func():
    x = (lambda: 42)()
    y = [i for i in range(10)]
    return x, y
```

**Result**: Valid: True, Confidence: 0.1-0.3
**Why**: Has some common patterns but unusual combinations

### Example 3: Domain-Specific Code
```python
def matrix_multiply(A, B):
    # Mathematical operation
    rows = len(A)
    cols = len(B[0])
    result = [[sum(A[i][k] * B[k][j] for k in range(len(B))) 
               for j in range(cols)] 
              for i in range(rows)]
    return result
```

**Result**: Valid: True or False, Low Confidence
**Why**: Uses complex comprehensions and math patterns not common in stdlib

## Model Selection

### Use AST Model When
- You want syntactic validation (checking structure)
- You need to validate grammar correctness
- You're checking for specific AST node patterns

### Use Semantic Model When
- You want to validate high-level behavior patterns
- You're checking if code follows common conventions
- You want guidance on how functions typically work

### Use Both When
- You want comprehensive validation
- You're training a new agent on the codebase
- You want to understand both structure and semantics

## Training Your Own Models

### Train AST Model
```bash
python -m src train <code_directory> <output_dir> --model-type ast
```

### Train Semantic Model
```bash
python -m src train <code_directory> <output_dir> --model-type semantic
```

### Train Both
```bash
python -m src train <code_directory> <output_dir> --model-type both
```

## Performance Notes

- Validation latency: <50ms typically
- Model loading: ~100ms (first time), <1ms (cached)
- Works best with models trained on similar code

## Troubleshooting

### "Unknown context" Errors
- This is normal - edge cases not in training data
- If most are unknown: model doesn't match your code style
- Solution: Train a new model on your codebase

### Low Confidence
- Code might be unusual or domain-specific
- Not necessarily wrong, just uncommon
- Compare against multiple models to see patterns

### "Could not extract..." Messages
- Code might have syntax errors
- Check the file is valid Python
- Run `python -m py_compile <file>` to verify

## Advanced Usage

### Checking Multiple Files
```bash
for file in src/**/*.py; do
    python -m src validate model.py "$file" | grep "Valid:"
done
```

### Analyzing Patterns
```bash
python -m src validate model.py code.py | grep -A 20 "Matching sequences"
```

### Comparing Models
```bash
echo "=== AST Model ===" && python -m src validate ast_model.py code.py
echo "=== Semantic Model ===" && python -m src validate semantic_model.py code.py
```

---

For more details, see [PHASE_2_2_VALIDATION_COMPLETE.md](./PHASE_2_2_VALIDATION_COMPLETE.md)
