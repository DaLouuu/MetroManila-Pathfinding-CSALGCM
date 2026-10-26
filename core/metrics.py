from dataclasses import dataclass
from typing import Dict, List

@dataclass
class BenchmarkResult:
    """Encapsulates the benchmarking metrics of a search run."""
    algorithm_name: str
    start_city: str
    end_city: str
    path: List[str]
    visited_order: List[str]
    total_cost: float
    elapsed_time_us: float
    nodes_expanded: int
    max_frontier_size: int
    memory_current_kb: float
    memory_peak_kb: float
    visit_count: Dict[str, int]

    def format_summary(self) -> str:
        path_str = " -> ".join(self.path) if self.path else "No path found"
        visited_str = " -> ".join(self.visited_order) if self.visited_order else "None"
        cost_str = str(self.total_cost) if self.total_cost != float('inf') else "Unreachable"

        return (
            f"Final Path: {path_str}\n"
            f"Path Traversed: {visited_str}\n"
            f"Total Cost: {cost_str}\n"
            f"Time: {self.elapsed_time_us:.4f} microseconds\n"
            f"Nodes Expanded: {self.nodes_expanded}\n"
            f"Max Frontier Size: {self.max_frontier_size}\n"
            f"Memory Usage: Current={self.memory_current_kb:.2f}KB, Peak={self.memory_peak_kb:.2f}KB\n"
            f"Visit Count: {self.visit_count}"
        )
