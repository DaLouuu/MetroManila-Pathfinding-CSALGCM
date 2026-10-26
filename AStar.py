import heapq

class AStarSearch:
    def __init__(self, graph, heuristic_values):
        self.graph = graph
        self.heuristic_values = heuristic_values

    def search(self, start, goal):
        frontier = []
        heapq.heappush(frontier, (0, start))

        visit_count = {start: 1}
        max_frontier_size = 0
        cost_so_far = {start: 0}
        function_values = {start: self.heuristic_values.get(start, 0)}
        came_from = {start: None}
        visited_order = []
        explored = set()

        while frontier:
            max_frontier_size = max(max_frontier_size, len(frontier))
            current_cost, current_node = heapq.heappop(frontier)

            # Avoid re-expanding already explored nodes from stale heap entries
            if current_node in explored:
                continue
            explored.add(current_node)
            visited_order.append(current_node)

            if current_node == goal:
                path = []
                temp = current_node
                while temp is not None:
                    path.append(temp)
                    temp = came_from[temp]
                return visited_order, cost_so_far[goal], path[::-1], len(visited_order), max_frontier_size, visit_count

            for neighbor, cost in self.graph[current_node].items():
                new_cost = cost_so_far[current_node] + cost
                neighbor_cost = cost_so_far.get(neighbor, float('inf'))

                if new_cost < neighbor_cost:
                    cost_so_far[neighbor] = new_cost
                    function_values[neighbor] = new_cost + self.heuristic_values.get(neighbor, 0)
                    heapq.heappush(frontier, (function_values[neighbor], neighbor))
                    came_from[neighbor] = current_node
                    visit_count[neighbor] = visit_count.get(neighbor, 0) + 1

        return visited_order, float('inf'), [], len(visited_order), max_frontier_size, visit_count