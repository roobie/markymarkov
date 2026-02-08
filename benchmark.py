#!/usr/bin/env python3
"""
Benchmark script for Marky performance testing.
Tests training and validation against /usr/lib/python3.13
"""

import time
import subprocess
import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple
import statistics

def count_python_files(directory: str) -> int:
    """Count Python files in directory."""
    result = subprocess.run(
        ["find", directory, "-name", "*.py", "-type", "f"],
        capture_output=True,
        text=True
    )
    return len(result.stdout.strip().split('\n')) if result.stdout.strip() else 0

def get_directory_size(directory: str) -> int:
    """Get total size of Python files in bytes."""
    result = subprocess.run(
        ["find", directory, "-name", "*.py", "-type", "f", "-exec", "wc", "-c", "{}", "+"],
        capture_output=True,
        text=True
    )
    total = 0
    for line in result.stdout.strip().split('\n'):
        parts = line.strip().split()
        if parts and parts[0].isdigit():
            total += int(parts[0])
    return total

def benchmark_training(source_dir: str, model_dir: str, model_type: str = "both", order: int = 2) -> Dict:
    """Benchmark training performance."""
    print(f"\n{'='*60}")
    print(f"Training Benchmark: {model_type} model (order={order})")
    print(f"{'='*60}")
    
    # Clean up old models
    model_path = Path(model_dir)
    if model_path.exists():
        for model_file in model_path.glob("*.py"):
            model_file.unlink()
    else:
        model_path.mkdir(parents=True, exist_ok=True)
    
    # Run training
    start_time = time.time()
    result = subprocess.run(
        ["uv", "run", "python", "-m", "src", "train", source_dir, model_dir, 
         "--model-type", model_type, "--order", str(order)],
        capture_output=True,
        text=True
    )
    end_time = time.time()
    
    duration = end_time - start_time
    
    if result.returncode != 0:
        print(f"ERROR: Training failed")
        print(result.stderr)
        return None
    
    # Count files processed
    file_count = count_python_files(source_dir)
    total_size = get_directory_size(source_dir)
    
    # Get model file sizes
    model_files = list(model_path.glob("*.py"))
    model_sizes = {f.name: f.stat().st_size for f in model_files}
    
    results = {
        'duration': duration,
        'file_count': file_count,
        'total_size_bytes': total_size,
        'total_size_mb': total_size / (1024 * 1024),
        'files_per_second': file_count / duration,
        'mb_per_second': (total_size / (1024 * 1024)) / duration,
        'model_files': model_sizes,
        'model_total_kb': sum(model_sizes.values()) / 1024,
        'order': order,
        'model_type': model_type,
    }
    
    print(f"Duration: {duration:.2f}s")
    print(f"Files processed: {file_count}")
    print(f"Total size: {results['total_size_mb']:.2f} MB")
    print(f"Throughput: {results['files_per_second']:.1f} files/sec")
    print(f"Throughput: {results['mb_per_second']:.2f} MB/sec")
    print(f"Model size: {results['model_total_kb']:.1f} KB")
    
    return results

def benchmark_validation(model_path: str, test_file: str, iterations: int = 100) -> Dict:
    """Benchmark validation performance."""
    print(f"\n{'='*60}")
    print(f"Validation Benchmark: {iterations} iterations")
    print(f"{'='*60}")
    
    times = []
    
    # Warmup (not counted)
    for _ in range(5):
        subprocess.run(
            ["uv", "run", "python", "-m", "src", "validate", model_path, test_file],
            capture_output=True,
            text=True
        )
    
    # Actual benchmark
    for i in range(iterations):
        start_time = time.time()
        result = subprocess.run(
            ["uv", "run", "python", "-m", "src", "validate", model_path, test_file],
            capture_output=True,
            text=True
        )
        end_time = time.time()
        
        if result.returncode == 0:
            times.append((end_time - start_time) * 1000)  # Convert to ms
        
        if (i + 1) % 10 == 0:
            print(f"  Completed {i + 1}/{iterations} iterations...")
    
    if not times:
        print("ERROR: No successful validations")
        return None
    
    results = {
        'iterations': len(times),
        'mean_ms': statistics.mean(times),
        'median_ms': statistics.median(times),
        'min_ms': min(times),
        'max_ms': max(times),
        'stdev_ms': statistics.stdev(times) if len(times) > 1 else 0,
        'p95_ms': sorted(times)[int(len(times) * 0.95)],
        'p99_ms': sorted(times)[int(len(times) * 0.99)],
    }
    
    print(f"Mean: {results['mean_ms']:.2f} ms")
    print(f"Median: {results['median_ms']:.2f} ms")
    print(f"Min: {results['min_ms']:.2f} ms")
    print(f"Max: {results['max_ms']:.2f} ms")
    print(f"StdDev: {results['stdev_ms']:.2f} ms")
    print(f"P95: {results['p95_ms']:.2f} ms")
    print(f"P99: {results['p99_ms']:.2f} ms")
    
    return results

def benchmark_stats(model_path: str) -> Dict:
    """Benchmark stats command."""
    print(f"\n{'='*60}")
    print(f"Stats Benchmark")
    print(f"{'='*60}")
    
    start_time = time.time()
    result = subprocess.run(
        ["uv", "run", "python", "-m", "src", "stats", model_path],
        capture_output=True,
        text=True
    )
    end_time = time.time()
    
    duration = (end_time - start_time) * 1000  # Convert to ms
    
    if result.returncode != 0:
        print(f"ERROR: Stats failed")
        return None
    
    print(f"Duration: {duration:.2f} ms")
    print(f"\nOutput:\n{result.stdout}")
    
    return {
        'duration_ms': duration,
        'output': result.stdout,
    }

def main():
    """Run all benchmarks."""
    source_dir = "/usr/lib/python3.13"
    model_dir = "benchmark_models"
    test_file = "/usr/lib/python3.13/ast.py"  # Large representative file
    
    print(f"\n{'#'*60}")
    print(f"# MARKY PERFORMANCE BENCHMARK")
    print(f"# Source: {source_dir}")
    print(f"# Test file: {test_file}")
    print(f"{'#'*60}")
    
    all_results = {}
    
    # Training benchmarks
    print("\n\n>>> TRAINING BENCHMARKS <<<")
    
    # AST model training
    ast_results = benchmark_training(source_dir, model_dir, "ast", order=2)
    if ast_results:
        all_results['training_ast'] = ast_results
    
    # Semantic model training
    semantic_results = benchmark_training(source_dir, model_dir, "semantic", order=2)
    if semantic_results:
        all_results['training_semantic'] = semantic_results
    
    # Both models training
    both_results = benchmark_training(source_dir, model_dir, "both", order=2)
    if both_results:
        all_results['training_both'] = both_results
    
    # Validation benchmarks
    print("\n\n>>> VALIDATION BENCHMARKS <<<")
    
    # AST validation
    ast_model = Path(model_dir) / "ast_model.py"
    if ast_model.exists():
        ast_val_results = benchmark_validation(str(ast_model), test_file, iterations=50)
        if ast_val_results:
            all_results['validation_ast'] = ast_val_results
    
    # Semantic validation
    semantic_model = Path(model_dir) / "semantic_model.py"
    if semantic_model.exists():
        semantic_val_results = benchmark_validation(str(semantic_model), test_file, iterations=50)
        if semantic_val_results:
            all_results['validation_semantic'] = semantic_val_results
    
    # Stats benchmark
    print("\n\n>>> STATS BENCHMARKS <<<")
    if semantic_model.exists():
        stats_results = benchmark_stats(str(semantic_model))
        if stats_results:
            all_results['stats'] = stats_results
    
    # Save results
    results_file = "benchmark_results.json"
    with open(results_file, 'w') as f:
        json.dump(all_results, f, indent=2)
    
    print(f"\n\n{'#'*60}")
    print(f"# BENCHMARK COMPLETE")
    print(f"# Results saved to: {results_file}")
    print(f"{'#'*60}")
    
    # Summary
    print("\n\n>>> SUMMARY <<<")
    if 'training_both' in all_results:
        tr = all_results['training_both']
        print(f"\nTraining Performance:")
        print(f"  Files: {tr['file_count']}")
        print(f"  Duration: {tr['duration']:.2f}s")
        print(f"  Throughput: {tr['files_per_second']:.1f} files/sec")
        print(f"  Model size: {tr['model_total_kb']:.1f} KB")
    
    if 'validation_semantic' in all_results:
        val = all_results['validation_semantic']
        print(f"\nValidation Performance (semantic):")
        print(f"  Mean: {val['mean_ms']:.2f} ms")
        print(f"  Median: {val['median_ms']:.2f} ms")
        print(f"  P95: {val['p95_ms']:.2f} ms")

if __name__ == "__main__":
    main()
