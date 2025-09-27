import tkinter as tk
import random

window = tk.Tk()
window.title("Background Colour Changer")
window.geometry("400x300")
colours = ["RED", "GREEN", "BLUE", "YELLOW", "ORANGE", "PURPLE", "PINK", "WHITE", "BLACK"]

def change_bg_colour():
    current_colour = window.cget("bg")
    new_colour = current_colour
    while new_colour == current_colour:
        new_colour = random.choice(colours)
    window.config(bg=new_colour)

label = tk.Label(text="Click the button to change background colour", fg="BLACK", font=("Arial", 15))
label.pack(pady=20)

button = tk.Button(text="Click me!", bg="WHITE", fg="BLACK", font=("Arial", 15), command=change_bg_colour)
button.pack(pady=20)

window.mainloop()