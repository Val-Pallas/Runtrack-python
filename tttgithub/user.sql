root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x400")

# Create a User object
user = User("username", "password")

# Create a TicTacToe object with the User object
game = TicTacToe(root, user)

root.mainloop()
