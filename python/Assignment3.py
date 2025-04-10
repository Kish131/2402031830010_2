import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.turn = "X"
        self.board = [None] * 9
        self.buttons = []

        # Create the game board buttons
        for i in range(9):
            button = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            row, col = divmod(i, 3)
            button.grid(row=row, column=col)
            self.buttons.append(button)

    def on_button_click(self, index):
        if self.board[index] is None:
            self.board[index] = self.turn
            self.buttons[index].config(text=self.turn)
            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.reset_game()
            elif all(cell is not None for cell in self.board):
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.turn = "O" if self.turn == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)               # Diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != None:
                return self.board[combo[0]]
        return None

    def reset_game(self):
        self.board = [None] * 9
        for button in self.buttons:
            button.config(text="")
        self.turn = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
