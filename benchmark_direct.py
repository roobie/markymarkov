#!/usr/bin/env python3
"""
Direct performance benchmark - no subprocess overhead.
"""

import time
import sys
from pathlib import Path
import statistics
import importlib.util

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.trainers.semantic_pattern_extractor import SemanticPatternExtractor
import ast

def load_model(model_path: str):
    """Load a Marky model."""
    spec = importlib.util.spec_from_file_location("model", model_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def benchmark_pattern_extraction(file_path: str, iterations: int = 100):
    """Benchmark pattern extraction speed."""
    print(f"\n{'='*60}")
    print(f"Pattern Extraction Benchmark: {iterations} iterations")
    print(f"File: {file_path}")
    print(f"{'='*60}")
    
    with open(file_path, 'r') as f:
        code = f.read()
    
    # AST extraction (just parsing)
    ast_times = []
    
    for _ in range(10):  # Warmup
        ast.parse(code)
    
    for i in range(iterations):
        start = time.perf_counter()
        tree = ast.parse(code)
        end = time.perf_counter()
        ast_times.append((end - start) * 1000)
    
    # Semantic extraction
    semantic_extractor = SemanticPatternExtractor()
    semantic_times = []
    
    for _ in range(10):  # Warmup
        semantic_extractor.extract_patterns(code)
    
    for i in range(iterations):
        start = time.perf_counter()
        patterns = semantic_extractor.extract_patterns(code)
        end = time.perf_counter()
        semantic_times.append((end - start) * 1000)
    
    print("\nAST Parsing:")
    print(f"  Mean: {statistics.mean(ast_times):.3f} ms")
    print(f"  Median: {statistics.median(ast_times):.3f} ms")
    print(f"  Min: {min(ast_times):.3f} ms")
    print(f"  Max: {max(ast_times):.3f} ms")
    print(f"  P95: {sorted(ast_times)[int(len(ast_times)*0.95)]:.3f} ms")
    
    print("\nSemantic Pattern Extraction:")
    print(f"  Mean: {statistics.mean(semantic_times):.3f} ms")
    print(f"  Median: {statistics.median(semantic_times):.3f} ms")
    print(f"  Min: {min(semantic_times):.3f} ms")
    print(f"  Max: {max(semantic_times):.3f} ms")
    print(f"  P95: {sorted(semantic_times)[int(len(semantic_times)*0.95)]:.3f} ms")
    
    return {
        'ast': {
            'mean_ms': statistics.mean(ast_times),
            'median_ms': statistics.median(ast_times),
            'min_ms': min(ast_times),
            'max_ms': max(ast_times),
            'p95_ms': sorted(ast_times)[int(len(ast_times)*0.95)],
        },
        'semantic': {
            'mean_ms': statistics.mean(semantic_times),
            'median_ms': statistics.median(semantic_times),
            'min_ms': min(semantic_times),
            'max_ms': max(semantic_times),
            'p95_ms': sorted(semantic_times)[int(len(semantic_times)*0.95)],
        }
    }

def benchmark_model_lookup(model_path: str, iterations: int = 10000):
    """Benchmark model lookup speed."""
    print(f"\n{'='*60}")
    print(f"Model Lookup Benchmark: {iterations} iterations")
    print(f"{'='*60}")
    
    model = load_model(model_path)
    transitions = model.TRANSITIONS
    
    # Get sample transitions
    sample_keys = list(transitions.keys())[:100]
    
    # Cold lookups (first time, no cache)
    cold_times = []
    for key in sample_keys[:10]:
        start = time.perf_counter()
        result = transitions.get(key, {})
        end = time.perf_counter()
        cold_times.append((end - start) * 1_000_000)  # microseconds
    
    # Warm lookups (cached)
    warm_times = []
    for _ in range(iterations):
        key = sample_keys[_ % len(sample_keys)]
        start = time.perf_counter()
        result = transitions.get(key, {})
        end = time.perf_counter()
        warm_times.append((end - start) * 1_000_000)  # microseconds
    
    print("\nCold Lookup (first access):")
    print(f"  Mean: {statistics.mean(cold_times):.3f} µs")
    print(f"  Median: {statistics.median(cold_times):.3f} µs")
    
    print("\nWarm Lookup (cached):")
    print(f"  Mean: {statistics.mean(warm_times):.3f} µs")
    print(f"  Median: {statistics.median(warm_times):.3f} µs")
    print(f"  Min: {min(warm_times):.3f} µs")
    print(f"  Max: {max(warm_times):.3f} µs")
    print(f"  P95: {sorted(warm_times)[int(len(warm_times)*0.95)]:.3f} µs")
    print(f"  P99: {sorted(warm_times)[int(len(warm_times)*0.99)]:.3f} µs")
    
    return {
        'cold_lookup_us': {
            'mean': statistics.mean(cold_times),
            'median': statistics.median(cold_times),
        },
        'warm_lookup_us': {
            'mean': statistics.mean(warm_times),
            'median': statistics.median(warm_times),
            'min': min(warm_times),
            'max': max(warm_times),
            'p95': sorted(warm_times)[int(len(warm_times)*0.95)],
            'p99': sorted(warm_times)[int(len(warm_times)*0.99)],
        }
    }

def main():
    test_file = "/usr/lib/python3.13/ast.py"
    model_file = "benchmark_models/semantic_model.py"
    
    print("\n" + "="*60)
    print("MARKY DIRECT PERFORMANCE BENCHMARK")
    print("(No subprocess overhead)")
    print("="*60)
    
    # Pattern extraction benchmark
    extraction_results = benchmark_pattern_extraction(test_file, iterations=100)
    
    # Model lookup benchmark
    lookup_results = benchmark_model_lookup(model_file, iterations=10000)
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"\nPattern Extraction (AST): {extraction_results['ast']['median_ms']:.2f} ms median")
    print(f"Pattern Extraction (Semantic): {extraction_results['semantic']['median_ms']:.2f} ms median")
    print(f"\nModel Lookup (warm): {lookup_results['warm_lookup_us']['median']:.3f} µs median")
    print(f"Model Lookup (warm): {lookup_results['warm_lookup_us']['mean']:.3f} µs mean")
    print(f"Model Lookup (P99): {lookup_results['warm_lookup_us']['p99']:.3f} µs")
    
    # Convert to ms for easier reading
    print(f"\nModel Lookup (warm): {lookup_results['warm_lookup_us']['median']/1000:.6f} ms median")
    print(f"Model Lookup (warm): {lookup_results['warm_lookup_us']['p99']/1000:.6f} ms P99")
    
    import json
    with open('benchmark_direct.json', 'w') as f:
        json.dump({
            'extraction': extraction_results,
            'lookup': lookup_results,
        }, f, indent=2)
    print("\nResults saved to: benchmark_direct.json")

if __name__ == "__main__":
    main()
