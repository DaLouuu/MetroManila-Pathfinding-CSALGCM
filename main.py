from algorithms import UniformCostSearch, AStarSearch, BeamSearch
from data import metro_manila_graph, heuristic_values
from core import run_search

def display_cities_and_heuristics():
    """Display available cities and their heuristic values."""
    print("Cities and their heuristic values (Goal: Paranaque):")
    for city, heuristic in heuristic_values.items():
        print(f"  {city}: {heuristic}")

def display_graph(graph):
    """Display graph nodes and weighted adjacency list."""
    print("\nGraph connections:")
    for city, connections in graph.items():
        connections_str = ", ".join(f"{neighbor}({cost})" for neighbor, cost in connections.items())
        print(f"  {city} -> {connections_str}")

def resolve_city_name(name: str, graph: dict):
    """Normalize and match city name case-insensitively."""
    clean = name.strip()
    for city in graph:
        if city.lower() == clean.lower():
            return city
    return None

def get_user_input():
    """Prompt user for starting city and destination."""
    start_input = input("\nEnter the start city: ").strip()
    end_input = input("Enter the end city: ").strip()
    return start_input, end_input

def main():
    display_cities_and_heuristics()
    display_graph(metro_manila_graph)

    start_input, end_input = get_user_input()

    start_city = resolve_city_name(start_input, metro_manila_graph)
    end_city = resolve_city_name(end_input, metro_manila_graph)

    if not start_city or not end_city:
        print("\nInvalid city names. Please enter valid city names from the graph.")
        return

    print(f"\n--- Routing from {start_city} to {end_city} ---")

    print("\n[1] Uniform Cost Search (UCS):")
    ucs = UniformCostSearch(metro_manila_graph)
    run_search(ucs, start_city, end_city)

    print("\n[2] A* Search:")
    a_star = AStarSearch(metro_manila_graph, heuristic_values)
    run_search(a_star, start_city, end_city)

    print("\n[3] Beam Search (beam_width=2):")
    beam_search = BeamSearch(metro_manila_graph, heuristic_values, beam_width=2)
    run_search(beam_search, start_city, end_city)

if __name__ == "__main__":
    main()
