from collections import deque
def is_valid(state):
    m1, c1, b, m2, c2 = state
    if m1 < 0 or c1 < 0 or m2 < 0 or c2 < 0:
        return False
    if (m1 > 0 and m1 < c1) or (m2 > 0 and m2 < c2):
        return False
    return True
def get_successors(state):
    m1, c1, b, m2, c2 = state
    successors = []
    if b == 1:  # Boat is on the original side
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for m, c in moves:
            new_state = (m1 - m, c1 - c, 0, m2 + m, c2 + c)
            if is_valid(new_state):
                successors.append(new_state)
    else:  # Boat is on the other side
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for m, c in moves:
            new_state = (m1 + m, c1 + c, 1, m2 - m, c2 - c)
            if is_valid(new_state):
                successors.append(new_state)
    return successors
def solve_missionaries_cannibals():
    initial_state = (3, 3, 1, 0, 0)
    goal_state = (0, 0, 0, 3, 3)
    queue = deque([initial_state])
    visited = set()
    visited.add(initial_state)
    parent = {initial_state: None}
    while queue:
        current_state = queue.popleft()
        if current_state == goal_state:
            return reconstruct_path(parent, goal_state)
        for successor in get_successors(current_state):
            if successor not in visited:
                queue.append(successor)
                visited.add(successor)
                parent[successor] = current_state
    return "No solution found"
def reconstruct_path(parent, state):
    path = []
    while state is not None:
        path.append(state)
        state = parent[state]
    path.reverse()
    return path
def print_solution(solution):
    for step in solution:
        m1, c1, b, m2, c2 = step
        side1 = f"{m1}M {c1}C"
        side2 = f"{m2}M {c2}C"
        boat_side = "Left" if b == 1 else "Right"
        print(f"Left bank: {side1} | Boat: {boat_side} | Right bank: {side2}")
    print()
solution = solve_missionaries_cannibals()
if solution != "No solution found":
    print("Solution found:")
    print_solution(solution)
else:
    print(solution)
