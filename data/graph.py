"""Metro Manila city road network graph."""

metro_manila_graph = {
    "Makati": {"Taguig": 5, "Pasay": 3, "Mandaluyong": 6},
    "Taguig": {"Makati": 5, "Pasig": 7},
    "Pasay": {"Makati": 3, "Paranaque": 4},
    "Mandaluyong": {"Makati": 6, "San Juan": 4, "Quezon City": 10},
    "Pasig": {"Taguig": 7, "Marikina": 5, "Quezon City": 8},
    "San Juan": {"Mandaluyong": 4, "Quezon City": 5},
    "Quezon City": {"Mandaluyong": 10, "San Juan": 5, "Pasig": 8, "Marikina": 7},
    "Marikina": {"Pasig": 5, "Quezon City": 7},
    "Paranaque": {"Pasay": 4}
}
