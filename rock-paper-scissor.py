import tkinter as tk
from tkinter import messagebox
import random

user_score = 0
computer_score = 0
choices = ["Rock", "Paper", "Scissor"]

def play(user_choice):
    global user_score, computer_score
    
    computer_choice = random.choice(choices)
    result_text = f"You choice: {user_choice}\nComputer choice: {computer_choice}\n"
    
   
    if user_choice == computer_choice:
        result_text += "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissor") or \
         (user_choice == "Scissor" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result_text += "You win!"
        user_score += 1
    else:
        result_text += "Computer wins!"
        computer_score += 1

    
    result_label.config(text=result_text)
    score_label.config(text=f"Score -> You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Make your choice!")
    score_label.config(text="Score -> You: 0 | Computer: 0")


root = tk.Tk()
root.title("Rock-Paper-Scissor Game")
root.geometry("400x300")
root.resizable(False, False)


instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissor:")
instruction_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

for choice in choices:
    button = tk.Button(button_frame, text=choice, width=10, height=2, command=lambda c=choice: play(c))
    button.pack(side="left", padx=10)


result_label = tk.Label(root, text="Make your choice!", font=("Arial", 12), fg="blue")
result_label.pack(pady=20)

score_label = tk.Label(root, text="Score -> You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)


reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=10)


root.mainloop()
