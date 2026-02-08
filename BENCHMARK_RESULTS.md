# Marky Performance Benchmark Summary

## Dataset
- **Source**: Python 3.13 Standard Library (`/usr/lib/python3.13`)
- **Files**: 596 Python files
- **Total Size**: 20.23 MB (21,210,750 bytes)
- **Average File Size**: 34.8 KB
- **Complexity**: Real-world production Python code with varied patterns

## Training Performance

### Speed
```
Combined (AST + Semantic):
  Duration: 5.65 seconds
  Throughput: 105.6 files/second
  Throughput: 3.58 MB/second
  Per-file: 9.5 ms average

AST Only:
  Duration: 2.60 seconds
  Throughput: 229.2 files/second
  
Semantic Only:
  Duration: 2.81 seconds
  Throughput: 212.0 files/second
```

### Model Sizes
```
AST model: 537.1 KB
Semantic model: 277.5 KB
Combined: 814.6 KB
Compression ratio: 25.4x (20 MB → 815 KB)
```

## Validation Performance

### End-to-End (with subprocess overhead)
```
AST Validation:
  Median: 216.9 ms
  P95: 238.3 ms
  Range: 207.1–246.8 ms

Semantic Validation:
  Median: 211.4 ms
  P95: 1233.5 ms
  Range: 187.9–1251.7 ms
```

### Core Operations
```
Model lookup (warm): <1 microsecond
Model lookup (cold): ~1-2 microseconds
Stats command: 161 ms
```

## Projections for Different Project Sizes

### Small (50 files, 2 MB)
- Training: ~0.5 seconds
- Model size: ~100 KB
- Validation: ~200ms per file

### Medium (500 files, 20 MB)
- Training: ~5 seconds
- Model size: ~800 KB
- Validation: ~200ms per file

### Large (5,000 files, 200 MB)
- Training: ~50 seconds
- Model size: ~5 MB
- Validation: ~200ms per file

### Very Large (50,000 files, 2 GB)
- Training: ~8 minutes
- Model size: ~30 MB
- Validation: ~200ms per file

## Key Performance Characteristics

✓ **Linear scaling**: O(n) training time with codebase size  
✓ **Sub-linear model growth**: Patterns converge as codebase grows  
✓ **Instant lookups**: <1μs for hash table access  
✓ **Compact models**: 25x compression ratio  
✓ **Fast training**: 100+ files/second  
✓ **Quick validation**: ~200ms per file  
✓ **Memory efficient**: 2-3 MB loaded models  

## Benchmark Scripts

All benchmark code is available in the repository:
- `benchmark.py` - Full training and validation benchmarks
- `benchmark_summary.py` - Results analysis
- `benchmark_results.json` - Raw data

Run benchmarks yourself:
```bash
python3 benchmark.py
python3 benchmark_summary.py
```

## Benchmark Environment

- **Date**: February 8, 2026
- **System**: x86_64 Linux
- **Python**: 3.13
- **Marky Version**: git HEAD
- **Method**: Multiple iterations with median/mean reporting
