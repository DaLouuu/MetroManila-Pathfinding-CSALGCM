from abc import ABC, abstractmethod
from typing import Any, Dict, List, Tuple

class SearchAlgorithm(ABC):
    """Abstract base class for graph search algorithms."""

    def __init__(self, graph: Dict[str, Dict[str, int]]):
        self.graph = graph

    @abstractmethod
    def search(self, start: str, goal: str) -> Tuple[List[str], float, List[str], int, int, Dict[str, int]]:
        """
        Execute search from start to goal.

        Returns:
            Tuple containing:
            - visited_order (List[str]): Order in which nodes were expanded/visited
            - total_cost (float): Total edge weight of the path found
            - path (List[str]): Sequence of nodes from start to goal
            - nodes_expanded (int): Count of expanded nodes
            - max_frontier_size (int): Maximum size reached by the frontier
            - visit_count (Dict[str, int]): Number of times each node was visited
        """
        pass
