import tkinter as tk
import random

root = tk.Tk()
root.title("High or Low")
root.geometry("350x250")

label = tk.Label(
    root,
    text="Computer picked a number (1-10)",
    font=("Arial", 12)
)
label.pack(pady=20)

result = tk.Label(root, text="", font=("Arial", 14))
result.pack(pady=20)

def check_guess(guess):
    num = random.randint(1, 10)

    if guess == "Low" and num <= 5:
        result.config(text=f"Correct! Number was {num}", fg="green")
    elif guess == "High" and num > 5:
        result.config(text=f"Correct! Number was {num}", fg="green")
    else:
        result.config(text=f"Wrong! Number was {num", fg="red")

low_button = tk.Button(
    root,
    text="Low (1-5)",
    font=("Arial", 12),
    command=: check_guess("Low")
)
low_button.pack(pady=5)

high_button = tk.Button(
    root,
    text="High (6-10)",
    font=("Arial", 12),
    command=lambda: check_guess("High")
)
high_button.pack(pady=5)

root.mainloop()