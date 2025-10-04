import tkinter as tk

window = tk.Tk()
window.title("Counter App")
window.geometry("400x300")

count = 0
 
def increase():
    global count
    count += 1
    label.config(text="Counter: " + str(count))

def decrease():
    global count
    count -= 1
    label.config(text="Counter: " + str(count))

def reset():
    global count
    count = 0
    label.config(text="Counter: " + str(count))

def set_custom():
    global count
    try:
        value = int(entry.get())
        count = value
        label.config(text="Counter: " + str(count))
    except ValueError:
        label.config(text="Counter: Invalid Input")


label = tk.Label(text = "Counter: ", bg = "RED", fg = "WHITE", font=("Arial", 20))
label.pack(pady = 10)

label2 = tk.Label(text="Made by Ammar", font=("Arial", 10), fg = "BLACK",)
label2.pack(side = tk.BOTTOM, pady = 10)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

increase_button = tk.Button(button_frame, text="Increase", bg="GREEN", fg="WHITE", font=("Arial", 15), command=increase)
increase_button.pack(side=tk.LEFT, padx=10)

reset_button = tk.Button(button_frame, text="Reset", bg="YELLOW", fg="BLACK", font=("Arial", 15), command=reset)
reset_button.pack(side=tk.LEFT, padx=10)

decrease_button = tk.Button(button_frame, text="Decrease", bg="BLUE", fg="WHITE", font=("Arial", 15), command=decrease)
decrease_button.pack(side=tk.LEFT, padx=10)

entry_frame = tk.Frame(window)
entry_frame.pack(pady=10)

entry = tk.Entry(entry_frame, font=("Arial", 15), width=10)
entry.pack(side=tk.LEFT, padx=10)

set_button = tk.Button(entry_frame, text="Set Value", font=("Arial", 15), command=set_custom)
set_button.pack(side=tk.LEFT, padx=10)

window.mainloop()