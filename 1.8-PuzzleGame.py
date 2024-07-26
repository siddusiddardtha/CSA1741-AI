import heapq

class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.blank_pos = self.board.index(0)
        self.priority = self.moves + self.manhattan_distance()

    def manhattan_distance(self):
        distance = 0
        for i, tile in enumerate(self.board):
            if tile == 0:
                continue
            target_x, target_y = divmod(tile - 1, 3)
            current_x, current_y = divmod(i, 3)
            distance += abs(target_x - current_x) + abs(target_y - current_y)
        return distance

    def is_goal(self):
        return self.board == list(range(1, 9)) + [0]

    def possible_moves(self):
        x, y = divmod(self.blank_pos, 3)
        moves = []
        if x > 0: moves.append(-3)  
        if x < 2: moves.append(3)   
        if y > 0: moves.append(-1)  
        if y < 2: moves.append(1)   
        return moves

    def next_states(self):
        next_states = []
        for move in self.possible_moves():
            new_blank_pos = self.blank_pos + move
            new_board = self.board[:]
            new_board[self.blank_pos], new_board[new_blank_pos] = new_board[new_blank_pos], new_board[self.blank_pos]
            next_states.append(PuzzleState(new_board, self.moves + 1, self))
        return next_states

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(self.board))

def solve_puzzle(start_board):
    start_state = PuzzleState(start_board)
    if start_state.is_goal():
        return start_state.moves, []

    open_set = []
    heapq.heappush(open_set, start_state)
    closed_set = set()
    closed_set.add(start_state)

    while open_set:
        current_state = heapq.heappop(open_set)

        if current_state.is_goal():
            moves = current_state.moves
            path = []
            while current_state.previous:
                path.append(current_state.board)
                current_state = current_state.previous
            path.append(current_state.board)
            path.reverse()
            return moves, path

        for next_state in current_state.next_states():
            if next_state in closed_set:
                continue
            if next_state not in open_set or next_state.moves < current_state.moves:
                heapq.heappush(open_set, next_state)
                closed_set.add(next_state)

    return None, None

start_board = [1, 2, 3, 4, 5, 6, 7, 0, 8]
moves, path = solve_puzzle(start_board)
if moves is not None:
    print(f"Solved in {moves} moves.")
    for step in path:
        print(step[:3])
        print(step[3:6])
        print(step[6:])
        print()
else:
    print("No solution found.")
