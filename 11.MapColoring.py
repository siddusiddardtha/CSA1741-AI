def is_valid_coloring(node, color, graph, colors):
    """Check if the current color assignment is valid."""
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def color_map(graph, colors, node, color_choices):
    """Recursive function to perform backtracking to color the map."""
    if node == len(graph):
        return True

    for color in color_choices:
        if is_valid_coloring(node, color, graph, colors):
            colors[node] = color
            if color_map(graph, colors, node + 1, color_choices):
                return True
            colors[node] = None

    return False

def solve_map_coloring(graph, color_choices):
    """Solve the map coloring problem using backtracking."""
    colors = [None] * len(graph)
    if color_map(graph, colors, 0, color_choices):
        return colors
    else:
        return None


if __name__ == "__main__":
    
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2]
    }
    color_choices = ["Red", "Green", "Blue"]

    solution = solve_map_coloring(graph, color_choices)
    if solution:
        print("Color assignment:", solution)
    else:
        print("No solution found.")
