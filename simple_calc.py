import tkinter as tk

#create the main window
app = tk.Tk()
app.title("Simple Calculator")
app.geometry("500x400")
#set bg color
app.config(bg="lightgreen")
#add a  label and entry box for first number
num1_label = tk.Label(app, text="Enter first number", bg="lightgreen", fg="black",)
num1_label.config(font=("Arial", 18))
num1_label.pack(pady=5)

entry_num1 = tk.Entry(app, bg ="white", fg="black")
entry_num1.config(font=("Arial", 18))
entry_num1.pack(pady=5)

#create entry box and label for second number
num2_label = tk.Label(app, text="Enter second number", bg="lightgreen", fg="black",)
num2_label.config(font=("Arial", 18))
num2_label.pack(pady=5)

entry_num2 = tk.Entry(app, bg ="white", fg="black")
entry_num2.config(font=("Arial", 18))
entry_num2.pack(pady=5)

#create a frame for buttons
button_frame = tk.Frame(app, bg="lightgreen")
button_frame.pack(pady=5)

#create result label
result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text, bg="lightgreen", fg="black")
result_label.config(font=("Arial", 18))
result_label.pack(pady=5)

def add():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        result_text.set(f"Result: {result}")
    except ValueError:
        result_text.set("Please enter valid numbers.")

def subtract():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 - num2
        result_text.set(f"Result: {result}")
    except ValueError:
        result_text.set("Please enter valid numbers.")

def multiply():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 * num2
        result_text.set(f"Result: {result}")
    except ValueError:
        result_text.set("Please enter valid numbers.")

def divide():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            result_text.set("Division by zero is not allowed.")
        else:
            result = num1 / num2
            result_text.set(f"Result: {result}")
    except ValueError:
        result_text.set("Please enter valid numbers.")


# create 4 buttons for addition, subtraction, multiplication, division
add_button = tk.Button(button_frame, text="+", bg="white", fg="black", font=("Arial", 18), width=5, command=add)
sub_button = tk.Button(button_frame, text="-", bg="white", fg="black", font=("Arial", 18), width=5, command=subtract)
mul_button = tk.Button(button_frame, text="*", bg="white", fg="black", font=("Arial", 18), width=5, command=multiply)
div_button = tk.Button(button_frame, text="/", bg="white", fg="black", font=("Arial", 18), width=5, command=divide)

add_button.pack(side=tk.LEFT, padx=5)
sub_button.pack(side=tk.LEFT, padx=5)
mul_button.pack(side=tk.LEFT, padx=5)
div_button.pack(side=tk.LEFT, padx=5)

app.mainloop()