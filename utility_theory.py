# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 01:58:14 2023

@author: vraj2
"""

import matplotlib.pyplot as plt
import numpy as np

def utility_function_linear(distance, road_quality):
    # Linear utility function
    return 100 - distance - (50 if road_quality == 'poor' else 0)

def utility_function_logarithmic(distance, road_quality):
    # Logarithmic utility function for more emphasis on lower distances
    return 100 - np.log(distance + 1) * 10 - (50 if road_quality == 'poor' else 0)

def calculate_expected_utility(route, utility_function):
    # Assuming hypothetical probabilities for different traffic conditions
    traffic_conditions = {"light": 0.3, "moderate": 0.5, "heavy": 0.2}
    expected_utility = 0
    for condition, probability in traffic_conditions.items():
        # Adjusting utility based on traffic condition (less utility in heavy traffic)
        adjusted_distance = route["distance"] * (1.2 if condition == "heavy" else 1)
        expected_utility += probability * utility_function(adjusted_distance, route["road_quality"])
    return expected_utility

def choose_best_route(routes, utility_function):
    best_route = None
    max_utility = -float('inf')
    for route_name, route_info in routes.items():
        utility = calculate_expected_utility(route_info, utility_function)
        if utility > max_utility:
            max_utility = utility
            best_route = route_name
    return best_route, max_utility

def choose_best_route_and_print(routes, utility_function, utility_function_name):
    best_route, max_utility = choose_best_route(routes, utility_function)
    print(f"Best route using utility function ({utility_function_name}): {best_route} with utility {max_utility}")

def plot_utilities(routes, utility_functions, filename="route_utilities.png"):
    labels = list(routes.keys())
    linear_utilities = [calculate_expected_utility(routes[route], utility_functions[0]) for route in routes]
    logarithmic_utilities = [calculate_expected_utility(routes[route], utility_functions[1]) for route in routes]

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, linear_utilities, width, label='Linear Utility')
    rects2 = ax.bar(x + width/2, logarithmic_utilities, width, label='Logarithmic Utility')

    ax.set_xlabel('Routes')
    ax.set_ylabel('Utilities')
    ax.set_title('Utilities by Route and Utility Function')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.savefig(filename) 
    plt.show()

# Define routes
routes = {
    "Route 1": {"distance": 30, "road_quality": "good"},
    "Route 2": {"distance": 40, "road_quality": "poor"},
    "Route 3": {"distance": 25, "road_quality": "good"}
}

# Utility functions
utility_functions = [utility_function_linear, utility_function_logarithmic]

# Display process and results
print("Calculating best routes using utility theory...")
choose_best_route_and_print(routes, utility_function_linear, "Linear")
choose_best_route_and_print(routes, utility_function_logarithmic, "Logarithmic")

# Plot utilities
plot_utilities(routes, utility_functions, filename="route_utilities.png")
