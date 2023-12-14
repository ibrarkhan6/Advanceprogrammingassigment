# At first we need to import tkinter as tk.
import tkinter as tk
# And import random.
import random
# From tkinter import messsagebox.
from tkinter import messagebox
# Selecting and keeping the class as a MyWordGuessingGame.
class MyWordGuessingGame:
    def __init__(myself, root):
        myself.root = root
        myself.root.title("Word Guessing Game")

        # Below are the variables mentioned for this task.
        myself.words = ["python", "programming", "tkinter", "developer", "keyboard", "mouse", "computer", "coding"]
        myself.score = 0
        myself.timer_seconds = 30 # Kepping the timer seconds as 30.

        # Below are my gui components which I am going to use in this task.
        myself.label_title = tk.Label(root, text="Word Guessing Game", font=("Helvetica", 16))
        myself.label_title.grid(row=0, column=0, columnspan=2, pady=10)
       # Now its mentioned a label as a score.
        myself.label_score = tk.Label(root, text="Score: 0")
        myself.label_score.grid(row=1, column=0, columnspan=2)
        # Now its mentioned as label as a timer.
        myself.label_timer = tk.Label(root, text=f"Time Remaining: {myself.timer_seconds}s")
        myself.label_timer.grid(row=2, column=0, columnspan=2)
         # Word
        myself.label_word = tk.Label(root, text="")
        myself.label_word.grid(row=3, column=0, columnspan=2, pady=20)
        # Entry
        myself.entry_guess = tk.Entry(root)
        myself.entry_guess.grid(row=4, column=0, columnspan=2, pady=10)
        # Buttons which I have created.
        myself.button_guess = tk.Button(root, text="Guess", command=myself.check_guess)
        myself.button_guess.grid(row=5, column=0, columnspan=2, pady=10)

        # Now we need to start the game which we have designed with this gui program.
        myself.start_game()

    def start_game(myself):
        myself.root.after(1000, myself.update_timer)
        myself.next_word()

    def next_word(self):
        # Now we need to pick any random word from the list mentioned.
        myword_to_guess = random.choice(self.words)
        
        # Now we need to make sure to shuffle the word.
        myshuffled_word = ''.join(random.sample(myword_to_guess, len(myword_to_guess)))

        # Now we need to make sure to display the shuffled word.
        self.label_word.config(text=myshuffled_word)

        # Now we need to reset the entry field.
        self.entry_guess.delete(0, tk.END)

        # Now we need to focus on the entry field.
        self.entry_guess.focus()

        # Now we need to  update the score display
        self.label_score.config(text=f"Score: {self.score}")

        # Now we need to schedule the next word after 5000 milliseconds (5 seconds).
        self.root.after(5000, self.next_word)
# Now I am going to use the def function for update_timer.
    def update_timer(myself):
        if myself.timer_seconds > 0:
            myself.timer_seconds -= 1
            myself.label_timer.config(text=f"Time Remaining: {myself.timer_seconds}s")
            myself.root.after(1000, myself.update_timer)
        else:
            myself.end_game() # End Game.
# Now using the def function for check_guess.
    def check_guess(myself):
        guessed_word = myself.entry_guess.get().lower()
        current_word = myself.label_word.cget("text")
     # Now using the if function for guessed_word .
        if guessed_word == current_word:
            myself.score += 1
            messagebox.showinfo("Correct!", "Good job! You guessed it right.")
            # Now using the else function.
        else:
            messagebox.showinfo("Incorrect", f"Sorry, the correct word was '{current_word}'.")
# Now using the def function for end_game.
    def end_game(self):
        messagebox.showinfo("Game Over", f"Game Over! Your final score is {self.score}.")
        self.root.destroy()
# Now using below the if function.
if __name__ == "__main__":
    finalroot = tk.Tk()# Changing the root name to finalroot.
    app = MyWordGuessingGame(finalroot)
    finalroot.mainloop()# Now start the mainloop.
