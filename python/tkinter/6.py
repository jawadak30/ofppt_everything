import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")

        # Create buttons for rock, paper, and scissors
        self.rock_button = tk.Button(root, text="Rock", command=lambda: self.play("rock"))
        self.paper_button = tk.Button(root, text="Paper", command=lambda: self.play("paper"))
        self.scissors_button = tk.Button(root, text="Scissors", command=lambda: self.play("scissors"))

        # Create a label to display game results
        self.result_label = tk.Label(root, text="Choose your move!")

        # Place buttons and label in the window
        self.rock_button.pack(side=tk.LEFT, padx=10)
        self.paper_button.pack(side=tk.LEFT, padx=10)
        self.scissors_button.pack(side=tk.LEFT, padx=10)
        self.result_label.pack(pady=20)

    def play(self, player_move):
        moves = ["rock", "paper", "scissors"]
        computer_move = random.choice(moves)

        result = self.determine_winner(player_move, computer_move)

        self.result_label.config(text=f"Player: {player_move}   Computer: {computer_move}\nResult: {result}")

    def determine_winner(self, player_move, computer_move):
        if player_move == computer_move:
            return "It's a tie!"
        elif (
            (player_move == "rock" and computer_move == "scissors") or
            (player_move == "paper" and computer_move == "rock") or
            (player_move == "scissors" and computer_move == "paper")
        ):
            return "You win!"
        else:
            return "Computer wins!"

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()