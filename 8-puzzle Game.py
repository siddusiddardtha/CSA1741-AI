import heapq
def manhattan(board):
    distance = 0
    for i, tile in enumerate(board):
        if tile != 0:
            correct_pos = tile - 1
            current_row, current_col = divmod(i, 3)
            correct_row, correct_col = divmod(correct_pos, 3)
            distance += abs(current_row - correct_row) + abs(current_col - correct_col)
    return distance
def get_neighbors(board):
    zero_pos = board.index(0)
    zero_row, zero_col = divmod(zero_pos, 3)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    neighbors = []
    for dr, dc in directions:
        new_row, new_col = zero_row + dr, zero_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero_pos = new_row * 3 + new_col
            new_board = board[:]
            new_board[zero_pos], new_board[new_zero_pos] = new_board[new_zero_pos], new_board[zero_pos]
            neighbors.append(new_board)
    return neighbors
def a_star(initial_board):
    open_set = []
    heapq.heappush(open_set, (manhattan(initial_board), 0, initial_board, None))
    closed_set = set()
    came_from = {}
    while open_set:
        _, moves, current_board, prev_board = heapq.heappop(open_set)
        if current_board == list(range(1, 9)) + [0]:
            path = []
            while current_board:
                path.append(current_board)
                current_board = came_from.get(tuple(current_board))
            return path[::-1]
        closed_set.add(tuple(current_board))
        for neighbor in get_neighbors(current_board):
            if tuple(neighbor) in closed_set:
                continue
            heapq.heappush(open_set, (moves + 1 + manhattan(neighbor), moves + 1, neighbor, current_board))
            came_from[tuple(neighbor)] = current_board
    return None
def print_solution(path):
    for step, board in enumerate(path):
        print(f"Step {step}:")
        for i in range(0, 9, 3):
            print(board[i:i + 3])
        print()
if __name__ == "__main__":
    initial_board = [1, 2, 3, 4, 0, 5, 6, 7, 8]  # example initial state
    solution = a_star(initial_board)
    if solution:
        print_solution(solution)
    else:
        print("No solution found.")