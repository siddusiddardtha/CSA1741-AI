import itertools

def calculate_distance(matrix, route):
    """Calculate the total distance of a given route based on the distance matrix."""
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += matrix[route[i]][route[i+1]]
    total_distance += matrix[route[-1]][route[0]]  # Return to the starting city
    return total_distance

def traveling_salesman_brute_force(distance_matrix):
    """Solve the Traveling Salesman Problem using brute-force approach."""
    n = len(distance_matrix)
    cities = list(range(n))
    shortest_route = None
    min_distance = float('inf')

    for perm in itertools.permutations(cities):
        current_distance = calculate_distance(distance_matrix, perm)
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_route = perm

    return shortest_route, min_distance


if __name__ == "__main__":
    
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    route, distance = traveling_salesman_brute_force(distance_matrix)
    print("Shortest route:", route)
    print("Minimum distance:", distance)
