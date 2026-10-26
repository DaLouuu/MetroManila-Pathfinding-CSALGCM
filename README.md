# Metro Manila Pathfinding & Algorithm Analysis (CSALGCM)

[![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![Course](https://img.shields.io/badge/Course-CSALGCM-red.svg)](#academic-context)
[![Subject](https://img.shields.io/badge/Algorithms-UCS%20%7C%20A*%20%7C%20Beam%20Search-green.svg)](#algorithms-implemented)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](#license)

An algorithmic benchmarking and pathfinding comparative analysis tool developed for **CSALGCM** (Advanced Algorithms and Complexity). This project models Metro Manila's interconnected city road network as an undirected, weighted graph and systematically evaluates the trade-offs between uninformed graph search (**Uniform Cost Search**) and informed heuristic search (**A\* Search** and **Beam Search**).

---

## Table of Contents

- [Project Overview](#project-overview)
- [Graph Representation & Problem Formulation](#graph-representation--problem-formulation)
- [Algorithms Implemented](#algorithms-implemented)
- [Benchmarking Metrics](#benchmarking-metrics)
- [Empirical Comparison & Sample Output](#empirical-comparison--sample-output)
- [Frontend Status & Visualizer Proposals](#frontend-status--visualizer-proposals)
- [Suggested Folder Hierarchy](#suggested-folder-hierarchy)
- [Installation & Usage](#installation--usage)
- [Academic Context](#academic-context)

---

## Project Overview

In urban route planning and transportation networks, selecting the optimal algorithm requires balancing **path optimality**, **time complexity**, and **memory utilization**. 

This project explores:
1. **Uninformed Search (UCS)**: Explores paths strictly based on cumulative path cost $g(n)$, guaranteeing an optimal route but potentially expanding more nodes.
2. **Informed Search (A\*)**: Combines actual path cost $g(n)$ and estimated remaining distance $h(n)$ using an evaluation function $f(n) = g(n) + h(n)$ to minimize search space while preserving optimality.
3. **Bounded-Memory Heuristic Search (Beam Search)**: Prunes the exploration frontier to a constant beam width $W$ based on heuristic values $h(n)$, minimizing memory footprint at the expense of completeness and optimality.

---

## Graph Representation & Problem Formulation

### 1. Metro Manila City Road Network

The road network connects 9 key cities across Metro Manila with undirected, weighted edges representing travel distance/cost:

```mermaid
graph LR
    QC[Quezon City] ---|10| Mand[Mandaluyong]
    QC ---|5| SJ[San Juan]
    QC ---|8| Pasig[Pasig]
    QC ---|7| Mar[Marikina]
    SJ ---|4| Mand
    Pasig ---|5| Mar
    Pasig ---|7| Tag[Taguig]
    Mand ---|6| Mak[Makati]
    Tag ---|5| Mak
    Mak ---|3| Pasay[Pasay]
    Pasay ---|4| Para[Paranaque (Goal)]
```

### 2. Heuristic Values ($h(n)$ to Paranaque)

The default heuristic table provides admissible estimated costs from each city toward the goal city (**Paranaque**, $h=0$):

| City | Estimated Cost $h(n)$ to Paranaque |
| :--- | :---: |
| **Paranaque** | **0** (Goal) |
| **Pasay** | 4 |
| **Makati** | 6 |
| **Taguig** | 9 |
| **Mandaluyong** | 10 |
| **San Juan** | 12 |
| **Pasig** | 15 |
| **Quezon City** | 17 |
| **Marikina** | 20 |

---

## Algorithms Implemented

### 1. Uniform Cost Search (UCS)
- **Strategy**: Expands the unvisited node with the lowest cumulative path cost $g(n)$ from the start node using a min-heap priority queue.
- **Completeness**: Guaranteed (with non-negative edge costs).
- **Optimality**: Guaranteed to return the shortest path.
- **Time / Space Complexity**: $O(b^{1 + \lfloor C^* / \epsilon \rfloor})$ where $C^*$ is the optimal path cost and $\epsilon$ is the minimal edge weight.

### 2. A* Search
- **Strategy**: Prioritizes nodes using $f(n) = g(n) + h(n)$, combining the known cost $g(n)$ with the estimated remaining distance $h(n)$.
- **Completeness**: Guaranteed.
- **Optimality**: Guaranteed optimal when $h(n)$ is admissible (never overestimates) and consistent.
- **Pruning Effect**: Evaluates fewer nodes than UCS by directing exploration toward the target.

### 3. Beam Search
- **Strategy**: A heuristic search with bounded memory. At each level of exploration, the search frontier is sorted by heuristic value $h(n)$, and only the top $W$ (beam width, default $W=2$) candidates are retained; all other branches are permanently pruned.
- **Completeness**: Incomplete (can get trapped or miss solutions if the optimal branch is pruned).
- **Optimality**: Non-optimal (heuristic greedy decisions can yield suboptimal paths).
- **Time / Space Complexity**: Highly efficient bounded memory $O(W \cdot d)$ where $W$ is the beam width and $d$ is depth.

---

## Benchmarking Metrics

Each algorithm run is instrumented to capture empirical performance metrics:

1. **Path Traversed (Exploration Order)**: Order of nodes expanded/visited.
2. **Final Path**: Reconstructed route from start to destination.
3. **Total Cost**: Total edge weight along the final route.
4. **Execution Time**: Measured in microseconds via `time.perf_counter()`.
5. **Nodes Expanded**: Total number of nodes removed from frontier and explored.
6. **Max Frontier Size**: Peak memory footprint of candidate states in the frontier.
7. **Traced Memory**: Current and Peak allocated memory tracked using Python's `tracemalloc`.
8. **Visit Count**: Frequency of visitation attempts per node.

---

## Empirical Comparison & Sample Output

### Test Query: `Quezon City` $\rightarrow$ `Paranaque`

```text
--- Routing from Quezon City to Paranaque ---

[1] Uniform Cost Search (UCS):
Final Path: Quezon City -> San Juan -> Mandaluyong -> Makati -> Pasay -> Paranaque
Path Traversed: Quezon City -> San Juan -> Marikina -> Pasig -> Mandaluyong -> Makati -> Taguig -> Pasay -> Paranaque
Total Cost: 22
Time: 2187.5000 microseconds
Nodes Expanded: 9
Max Frontier Size: 4
Memory Usage: Current=0.38KB, Peak=1.55KB

[2] A* Search:
Final Path: Quezon City -> San Juan -> Mandaluyong -> Makati -> Pasay -> Paranaque
Path Traversed: Quezon City -> San Juan -> Mandaluyong -> Makati -> Pasay -> Paranaque
Total Cost: 22
Time: 106.7000 microseconds
Nodes Expanded: 6
Max Frontier Size: 4
Memory Usage: Current=0.31KB, Peak=1.73KB

[3] Beam Search (beam_width=2):
Final Path: Quezon City -> Mandaluyong -> Makati -> Pasay -> Paranaque
Path Traversed: Quezon City -> Mandaluyong -> Makati -> Pasay -> Paranaque
Total Cost: 23
Time: 396.1000 microseconds
Nodes Expanded: 5
Max Frontier Size: 4
Memory Usage: Current=0.30KB, Peak=0.60KB
```

### Analysis Summary

| Metric | Uniform Cost Search (UCS) | A* Search | Beam Search ($W=2$) |
| :--- | :---: | :---: | :---: |
| **Path Found** | Optimal (Cost: 22) | Optimal (Cost: 22) | Suboptimal (Cost: 23) |
| **Nodes Expanded** | 9 (Full exploration) | 6 (33% reduction vs UCS) | 5 (Greedy exploration) |
| **Frontier Memory** | Unbounded min-heap | Unbounded min-heap | Strictly bounded to $W$ |
| **Optimality Guarantee** | Yes | Yes (admissible $h$) | No |

---

## Frontend Status & Visualizer Proposals

### Current Status
> [!NOTE]
> **This repository currently does NOT have a frontend.**
> All operations and benchmark outputs are run through the command-line interface (`main.py`).

### Suggested Frontend Roadmap
To transform this CLI tool into an interactive visual application:
1. **Interactive Web Visualizer**:
   - Built with Vanilla HTML5 Canvas or SVG + CSS + JavaScript.
   - Interactive nodes representing Metro Manila cities on an overlay map.
   - Step-by-step playback showing nodes entering the frontier, expanding, and highlighting the final path.
2. **Dashboard Alternative (Streamlit or Dash)**:
   - Python-native GUI allowing users to dynamically adjust the beam width $W$, edit heuristic tables, select start/goal cities, and plot real-time latency vs. node expansion charts.

---

## Suggested Folder Hierarchy

To maintain clean separation of concerns as the project evolves, the following modular package architecture is recommended:

```text
MetroManila-Pathfinding-CSALGCM/
├── algorithms/                  # Core pathfinding search implementations
│   ├── __init__.py
│   ├── base.py                  # Abstract base class for search algorithms
│   ├── ucs.py                   # Uniform Cost Search
│   ├── a_star.py                # A* Search
│   └── beam_search.py           # Beam Search
├── data/                        # Graph representations and heuristic models
│   ├── __init__.py
│   ├── graph.py                 # City adjacency graph definitions
│   └── heuristics.py            # Heuristic distance tables
├── core/                        # Benchmarking & performance instrumentation
│   ├── __init__.py
│   ├── benchmark.py             # Memory & runtime profiling runner
│   └── metrics.py               # Performance metric collector
├── tests/                       # Unit tests and correctness validation
│   ├── __init__.py
│   ├── test_algorithms.py       # Algorithmic path & cost verification
│   └── test_benchmark.py        # Benchmark profiling tests
├── docs/                        # Project documentation and analysis reports
│   └── analysis_report.md
├── .gitignore                   # Ignore __pycache__, pyc, and temporary files
├── requirements.txt             # Project dependencies (standard library)
├── main.py                      # Main entry point for interactive CLI
└── README.md                    # Project documentation
```

---

## Installation & Usage

### Prerequisites
- Python 3.10+ (Standard library only; no external dependencies required).

### Running the Application

1. Clone or download the repository:
   ```bash
   git clone https://github.com/DaLouuu/MetroManila-Pathfinding-CSALGCM.git
   cd MetroManila-Pathfinding-CSALGCM
   ```

2. Run the main CLI benchmark:
   ```bash
   python main.py
   ```

3. Enter any start and destination city from the displayed graph (e.g., `Quezon City` to `Paranaque`). City names are case-insensitive.

---

## Academic Context

- **Course**: CSALGCM (Advanced Algorithms and Complexity)
- **Topic**: Informed vs. Uninformed Search Strategies in Graph Networks
- **Institution**: De La Salle University (DLSU)

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.