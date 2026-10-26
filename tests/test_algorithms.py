import unittest
from algorithms import UniformCostSearch, AStarSearch, BeamSearch
from data import metro_manila_graph, heuristic_values
from core import run_search, BenchmarkResult
import UCS
import AStar
import beamSearch

class TestPathfindingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.graph = metro_manila_graph
        self.heuristics = heuristic_values

    def test_ucs_optimal_path_makati_to_paranaque(self):
        ucs = UniformCostSearch(self.graph)
        visited, cost, path, nodes_exp, max_f, visits = ucs.search("Makati", "Paranaque")
        self.assertEqual(path, ["Makati", "Pasay", "Paranaque"])
        self.assertEqual(cost, 7)
        self.assertTrue(nodes_exp > 0)

    def test_astar_optimal_path_makati_to_paranaque(self):
        astar = AStarSearch(self.graph, self.heuristics)
        visited, cost, path, nodes_exp, max_f, visits = astar.search("Makati", "Paranaque")
        self.assertEqual(path, ["Makati", "Pasay", "Paranaque"])
        self.assertEqual(cost, 7)

    def test_beam_search_makati_to_paranaque(self):
        beam = BeamSearch(self.graph, self.heuristics, beam_width=2)
        visited, cost, path, nodes_exp, max_f, visits = beam.search("Makati", "Paranaque")
        self.assertEqual(path, ["Makati", "Pasay", "Paranaque"])
        self.assertEqual(cost, 7)

    def test_quezon_city_to_paranaque(self):
        ucs = UniformCostSearch(self.graph)
        astar = AStarSearch(self.graph, self.heuristics)
        beam = BeamSearch(self.graph, self.heuristics, beam_width=2)

        _, ucs_cost, ucs_path, ucs_exp, _, _ = ucs.search("Quezon City", "Paranaque")
        _, astar_cost, astar_path, astar_exp, _, _ = astar.search("Quezon City", "Paranaque")
        _, beam_cost, beam_path, beam_exp, _, _ = beam.search("Quezon City", "Paranaque")

        # UCS and A* both find the optimal cost of 22
        self.assertEqual(ucs_cost, 22)
        self.assertEqual(astar_cost, 22)
        self.assertEqual(ucs_path, astar_path)

        # A* expands fewer or equal nodes compared to UCS
        self.assertLessEqual(astar_exp, ucs_exp)

        # Beam search finds a valid path
        self.assertEqual(beam_path[0], "Quezon City")
        self.assertEqual(beam_path[-1], "Paranaque")

    def test_benchmark_runner(self):
        astar = AStarSearch(self.graph, self.heuristics)
        result = run_search(astar, "Makati", "Paranaque", verbose=False)
        self.assertIsInstance(result, BenchmarkResult)
        self.assertEqual(result.total_cost, 7)
        self.assertGreater(result.elapsed_time_us, 0)
        self.assertGreater(result.memory_peak_kb, 0)

    def test_root_shims_backward_compatibility(self):
        ucs_inst = UCS.UniformCostSearch(self.graph)
        astar_inst = AStar.AStarSearch(self.graph, self.heuristics)
        beam_inst = beamSearch.BeamSearch(self.graph, self.heuristics, 2)

        self.assertIsInstance(ucs_inst, UniformCostSearch)
        self.assertIsInstance(astar_inst, AStarSearch)
        self.assertIsInstance(beam_inst, BeamSearch)

if __name__ == "__main__":
    unittest.main()
