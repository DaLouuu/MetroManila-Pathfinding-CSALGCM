from typing import Dict, List, Tuple
from algorithms.base import SearchAlgorithm

class BeamSearch(SearchAlgorithm):
    """
    Beam Search Algorithm.
    Maintains a maximum of `beam_width` nodes at each frontier stage,
    selecting the candidates with the lowest heuristic values.
    """

    def __init__(self, graph: Dict[str, Dict[str, int]], heuristic_values: Dict[str, int], beam_width: int = 2):
        super().__init__(graph)
        self.heuristic_values = heuristic_values
        self.beam_width = beam_width

    def search(self, start: str, goal: str) -> Tuple[List[str], float, List[str], int, int, Dict[str, int]]:
        # Initialize frontier with (node, cost_so_far, path)
        frontier = [(start, 0, [start])]
        visited_order = []
        max_frontier_size = 1
        visit_count = {node: 0 for node in self.graph}
        visit_count[start] = 1

        while frontier:
            # Sort frontier by lowest heuristic value (closest to goal)
            frontier.sort(key=lambda x: self.heuristic_values.get(x[0], float('inf')))
            frontier = frontier[:self.beam_width]
            max_frontier_size = max(max_frontier_size, len(frontier))

            # Pop the most promising city
            current_node, current_cost, current_path = frontier.pop(0)
            visited_order.append(current_node)

            # If current city is the goal, return results
            if current_node == goal:
                return visited_order, current_cost, current_path, len(visited_order), max_frontier_size, visit_count

            # Expand neighbors
            for neighbor, cost in self.graph.get(current_node, {}).items():
                if neighbor not in current_path:
                    frontier.append((neighbor, current_cost + cost, current_path + [neighbor]))
                    visit_count[neighbor] = visit_count.get(neighbor, 0) + 1

            if frontier:
                max_frontier_size = max(max_frontier_size, len(frontier))

        return visited_order, float('inf'), [], len(visited_order), max_frontier_size, visit_count
