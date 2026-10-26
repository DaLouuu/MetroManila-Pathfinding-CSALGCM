import time
import tracemalloc
from typing import Optional
from algorithms.base import SearchAlgorithm
from core.metrics import BenchmarkResult

def run_search(search_algorithm: SearchAlgorithm, start_city: str, end_city: str, verbose: bool = True) -> BenchmarkResult:
    """
    Executes a search algorithm with memory profiling and execution timing.

    Args:
        search_algorithm: An instance of SearchAlgorithm (UCS, A*, BeamSearch).
        start_city: Origin node.
        end_city: Destination node.
        verbose: If True, prints formatted summary.

    Returns:
        BenchmarkResult with performance metrics.
    """
    tracemalloc.start()
    start_time = time.perf_counter()

    visited_order, total_cost, path, nodes_expanded, max_frontier_size, visit_count = search_algorithm.search(start_city, end_city)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    elapsed_time_us = (end_time - start_time) * 1e6

    result = BenchmarkResult(
        algorithm_name=search_algorithm.__class__.__name__,
        start_city=start_city,
        end_city=end_city,
        path=path,
        visited_order=visited_order,
        total_cost=total_cost,
        elapsed_time_us=elapsed_time_us,
        nodes_expanded=nodes_expanded,
        max_frontier_size=max_frontier_size,
        memory_current_kb=current / 1024.0,
        memory_peak_kb=peak / 1024.0,
        visit_count=visit_count
    )

    if verbose:
        print(result.format_summary())

    return result
