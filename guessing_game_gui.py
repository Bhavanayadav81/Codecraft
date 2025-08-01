import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("🎮 Number Guessing Game")
        master.geometry("400x300")
        master.config(bg="#f0f8ff")

        self.secret_number = 42
        self.attempts = 0

        self.label = tk.Label(master, text="Guess a number between 1 and 100", font=("Helvetica", 14), bg="#f0f8ff")
        self.label.pack(pady=20)

        self.entry = tk.Entry(master, font=("Helvetica", 12))
        self.entry.pack()

        self.check_button = tk.Button(master, text="Check Guess", command=self.check_guess, font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.check_button.pack(pady=10)

        self.feedback_label = tk.Label(master, text="", font=("Helvetica", 12), bg="#f0f8ff", fg="#333")
        self.feedback_label.pack(pady=5)

        self.reset_button = tk.Button(master, text="Reset Game", command=self.reset_game, font=("Helvetica", 10), bg="#f44336", fg="white")
        self.reset_button.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.secret_number:
                self.feedback_label.config(text="🔻 Too low! Try a higher number.")
            elif guess > self.secret_number:
                self.feedback_label.config(text="🔺 Too high! Try a lower number.")
            else:
                messagebox.showinfo("🎉 Congratulations!", f"You guessed it in {self.attempts} attempts!")
                self.reset_game()
        except ValueError:
            self.feedback_label.config(text="⚠️ Please enter a valid number.")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")

# Run the GUI app
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
