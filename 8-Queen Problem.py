# Initialize the board and variables
queens = [-1] * 8  # Tracks the column position of queens in each row
row = 0            # Start from the first row
# Function to check if it's safe to place a queen
def is_safe(queens, row, col):
    for i in range(row):
        if queens[i] == col or \
           queens[i] - i == col - row or \
           queens[i] + i == col + row:
            return False
    return True
# Start solving the problem
while row < 8:
    found_safe_place = False
    for col in range(queens[row] + 1, 8):
        if is_safe(queens, row, col):
            queens[row] = col
            found_safe_place = True
            break
    if not found_safe_place:
        queens[row] = -1
        row -= 1
        if row < 0:
            print("No solution found")
            break
    else:
        row += 1
# If solution is found, print the board
if row == 8:
    for i in range(8):
        row_str = ["."] * 8
        row_str[queens[i]] = "Q"
        print(" ".join(row_str))
