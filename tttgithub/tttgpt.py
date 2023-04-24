import tkinter as tk
from tkinter import messagebox
import random

class MyClass:
    def __init__(self, master, user):
        self.master = master
        self.user = user
        # additional initialization code can go here
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.games_won = 0
        self.games_played = 0

class TicTacToeGame:
    def __init__(self, master, user):
        self.master = master
        self.user = user
        self.master.title("Tic Tac Toe")

class RegistrationWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("User Registration")

        # Create username and password labels and entries
        self.username_label = tk.Label(self.master, text="Username:")
        self.username_label.grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = tk.Entry(self.master)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        self.password_label = tk.Label(self.master, text="Password:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Create register button
        self.register_button = tk.Button(self.master, text="Register", command=self.register)
        self.register_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        
class TicTacToeGame:
    def __init__(self, master, user):
        self.master = master
        self.master.title("Tic Tac Toe")

        # Create buttons
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.master, text="", width=10, height=5, command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        # Create game status label
        self.status_label = tk.Label(self.master, text="Player X's turn", font=("Helvetica", 16))
        self.status_label.grid(row=3, column=0, columnspan=3)

        # Initialize game state
        self.player = "X"
        self.game_over = False
        self.board = [["" for _ in range(3)] for _ in range(3)]

        # User account
        self.user = user

    def on_button_click(self, row, col):
        if not self.game_over:
            button = self.buttons[row][col]
            if button["text"] == "":
                button["text"] = self.player
                self.board[row][col] = self.player
                self.check_for_winner()
                if not self.game_over:
                    self.switch_player()
                    if self.player == "O":
                        self.make_ai_move()

    def switch_player(self):
        self.player = "O" if self.player == "X" else "X"
        self.status_label.config(text=f"Player {self.player}'s turn")

    def make_ai_move(self):
        # Find empty cells and choose one at random
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ""]
        row, col = random.choice(empty_cells)

        # Update button and board state
        button = self.buttons[row][col]
        button["text"] = self.player
        self.board[row][col] = self.player

        # Check for winner and switch player
        self.check_for_winner()
        if not self.game_over:
            self.switch_player()

    def check_for_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                self.game_over = True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                self.game_over = True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            self.game_over = True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            self.game_over = True

        if self.game_over:
            self.status_label.config(text=f"Player {self.player} wins!")
        elif all([self.board[i][j] != "" for i in range(3) for j in range(3)]):
            self.game_over = True
            self.status_label.config(text="It's a tie!")
            
root = tk.Tk()
user = User("default_user", "default_password")
game = TicTacToeGame(root, user)
root.destroy()
root.mainloop()
