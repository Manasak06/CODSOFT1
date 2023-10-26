import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

# Function to check if someone has won the game
def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to make a random AI move
def make_random_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    if empty_cells:
        return random.choice(empty_cells)
    else:
        return None

# Main game loop
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

while True:
    print_board(board)
    
    if current_player == "X":
        user_move = input("Enter your move (row and column): ")
        row, col = map(int, user_move.split())
    else:
        print("AI is thinking...")
        row, col = make_random_move(board)
    
    if board[row][col] == " ":
        board[row][col] = current_player
        if check_win(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break
        elif all([cell != " " for row in board for cell in row]):
            print_board(board)
            print("It's a draw!")
            break
        current_player = "X" if current_player == "O" else "O"
    else:
        print("Invalid move. Try again.")

