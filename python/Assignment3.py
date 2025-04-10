def print_board(board):
    print("|---|---|---|")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("|-----------|")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("|-----------|")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("|---|---|---|")


def check_winner(board, turn):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]

    for combo in winning_combinations:
        line = board[combo[0]] + board[combo[1]] + board[combo[2]]
        if line == "XXX":
            return "X"
        elif line == "OOO":
            return "O"

    if all(cell in ['X', 'O'] for cell in board):
        return "draw"

    return None


def main():
    board = [str(i + 1) for i in range(9)]
    turn = "X"
    winner = None

    print("Welcome to 3x3 Tic Tac Toe.")
    print_board(board)
    print("X will play first. Enter a slot number to place X in:")

    while winner is None:
        try:
            num_input = int(input())
            if not 1 <= num_input <= 9:
                print("Invalid input; re-enter slot number:")
                continue
        except ValueError:
            print("Invalid input; re-enter slot number:")
            continue

        if board[num_input - 1] == str(num_input):
            board[num_input - 1] = turn
            print_board(board)
            winner = check_winner(board, turn)
            turn = "O" if turn == "X" else "X"
            if winner is None:
                print(f"{turn}'s turn; enter a slot number to place {turn} in:")
        else:
            print("Slot already taken; re-enter slot number:")

    if winner == "draw":
        print("It's a draw! Thanks for playing.")
    else:
        print(f"Congratulations! {winner}'s have won! Thanks for playing.")


if __name__ == "__main__":
    main()
