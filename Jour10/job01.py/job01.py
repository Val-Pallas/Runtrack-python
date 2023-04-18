"""Développez une version en ligne du fameux Tic Tac Toe, à l’aide de tkinter.
Dans ce jeu, deux joueurs s'affrontent. À tour de rôle, ils désignent une case et y
insèrent alternativement un signe (‘X’ et ‘O’). Le premier joueur qui arrive à faire un
alignement vertical, horizontal ou diagonal de trois signes gagne la partie. Si le plateau
de jeu est rempli de signes et qu’il n’y a pas d'alignement de trois, alors c’est un match
nul."""

# case alternative: Input= x / o
# alignement vertical 3 signes = gagnat
# alignetment horizontal 3 signes = gagnat
# alignement diagonal 3 signes =  gagnat 
# pas d'alignement = nul
# a grid of three-by-three cells

# tic_tac_toe.py

import tkinter as tk
from tkinter import font

class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        self._cells = {}
        
    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label (
            master=display_frame,
            text="Ready?",
            font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()