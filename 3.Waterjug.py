from collections import deque
def is_visited(state, visited):
    return state in visited
def solve_water_jug(capacity1, capacity2, target):
    queue = deque([(0, 0)])
    visited = set([(0, 0)])
    path = {(0, 0): None}
    while queue:
        (jug1, jug2) = queue.popleft()
        if jug1 == target or jug2 == target:
            return reconstruct_path((jug1, jug2), path)
        next_states = [
            (capacity1, jug2),  
            (jug1, capacity2),  
            (0, jug2),          
            (jug1, 0),          
            (jug1 - min(jug1, capacity2 - jug2), jug2 + min(jug1, capacity2 - jug2)), 
            (jug1 + min(jug2, capacity1 - jug1), jug2 - min(jug2, capacity1 - jug1))   
        ]
        for state in next_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)
                path[state] = (jug1, jug2)
    return "No solution found"
def reconstruct_path(state, path):
    result = []
    while state is not None:
        result.append(state)
        state = path[state]
    result.reverse()
    return result
capacity1 = 4  
capacity2 = 3  
target = 2     
solution = solve_water_jug(capacity1, capacity2, target)
if solution != "No solution found":
    print("Steps to reach the target:")
    for step in solution:
        print(step)
else:
    print(solution)
