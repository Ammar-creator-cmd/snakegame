import tkinter as tk

#create the main window
app = tk.Tk()
app.title("Weight Conversion Tool")
app.geometry("500x250")
3#set bg color
app.config(bg="lightblue")

#add a  label
label = tk.Label(app, text="Enter weight", bg="lightblue", fg="black",)
label.config(font=("Arial", 18))
label.pack(pady=5)

#create entry box
entry_weight = tk.Entry(app, bg ="white", fg="black")
entry_weight.config(font=("Arial", 18))
entry_weight.pack(pady=5)

#function to convert weight
unit_choice = tk.StringVar(app)
unit_choice.set("Select Unit")
unit_options = ["Kilograms to Pounds", "Pounds to Kilograms", "Kilograms to Ounces", "Ounces to Kilograms", "Pounds to Ounces", "Ounces to Pounds"]
drop = tk.OptionMenu(app, unit_choice, *unit_options)
drop.pack(pady=5)


#result label

result_text = tk.StringVar()
resultlabel = tk.Label(app, textvariable=result_text, bg="lightblue", fg="black")
resultlabel.config(font=("Arial", 18))
resultlabel.pack(pady=5)

def convert_weight():
    # All conversion results are formatted to two decimal places for consistency.
    weight = entry_weight.get()
    print(type(weight))
    selected_unit = unit_choice.get()
    print(selected_unit)
    global result_text
    try:
        weight = float(weight)
        if selected_unit == "Kilograms to Pounds":
            result = weight * 2.20462
            result_text.set(f"{weight} kg = {result:.2f} lbs")
        elif selected_unit == "Pounds to Kilograms":
            result = weight / 2.20462
            result_text.set(f"{weight} lbs = {result:.2f} kg")
        elif selected_unit == "Kilograms to Ounces":
            result = weight * 35.274
            result_text.set(f"{weight} kg = {result:.2f} oz")
        elif selected_unit == "Ounces to Kilograms":
            result = weight / 35.274
            result_text.set(f"{weight} oz = {result:.2f} kg")
        elif selected_unit == "Pounds to Ounces":
            result = weight * 16
            result_text.set(f"{weight} lbs = {result:.2f} oz")
        elif selected_unit == "Ounces to Pounds":
            result = weight / 16
            result_text.set(f"{weight} oz = {result:.2f} lbs")
        else:
            result_text.set("Please select a valid unit conversion.")
    except ValueError:
        result_text.set("Please enter a valid number.")


#create button to trigger conversion
button_convert = tk.Button(app, text="Convert", bg="green", fg="white", command=convert_weight)
button_convert.config(font=("Arial", 18))
button_convert.pack(pady=5)




app.mainloop()

