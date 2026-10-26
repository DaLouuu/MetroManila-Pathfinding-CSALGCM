class BeamSearch:
    def __init__(self, graph, heuristic_values, beam_width=2):
        self.graph = graph
        self.heuristic_values = heuristic_values
        self.beam_width = beam_width

    def search(self, start_node, end_node):
        # Initialize frontier with (node, cost_so_far, path)
        frontier = [(start_node, 0, [start_node])]
        visited_order = []
        max_frontier_size = 1
        visit_count = {node: 0 for node in self.graph}
        visit_count[start_node] = 1

        while frontier:
            # Sort frontier by heuristic value ascending (lowest heuristic = closest to goal)
            frontier.sort(key=lambda x: self.heuristic_values.get(x[0], float('inf')))
            frontier = frontier[:self.beam_width]
            max_frontier_size = max(max_frontier_size, len(frontier))

            # Pop the most promising city (lowest heuristic value)
            current_node, current_cost, current_path = frontier.pop(0)
            visited_order.append(current_node)

            # If current city is the destination, return results
            if current_node == end_node:
                return visited_order, current_cost, current_path, len(visited_order), max_frontier_size, visit_count

            # Expand neighbors
            for neighbor, cost in self.graph[current_node].items():
                if neighbor not in current_path:
                    frontier.append((neighbor, current_cost + cost, current_path + [neighbor]))
                    visit_count[neighbor] = visit_count.get(neighbor, 0) + 1

            if frontier:
                max_frontier_size = max(max_frontier_size, len(frontier))

        # If no path is found, return consistent tuple
        return visited_order, float('inf'), [], len(visited_order), max_frontier_size, visit_count
