# Initialize the board
board = {f"{row}{col}": "   " for row in "abc" for col in "123"}

def print_board():
    print(f"""
|{board['a1']}|{board['b1']}|{board['c1']}|
|{board['a2']}|{board['b2']}|{board['c2']}|
|{board['a3']}|{board['b3']}|{board['c3']}|
""")

# Main game loop
for turn in range(9):
    print_board()
    player = "X" if turn % 2 == 0 else "O"
    move = input(f"Player {player}, input your move: ")
    if move in board and board[move] == "   ":
        board[move] = f" {player} "
    else:
        print("Invalid move, try again.")
        continue

print_board()
