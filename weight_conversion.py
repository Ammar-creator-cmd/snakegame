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
unit_options = ["Kilograms to Pounds", "Pounds to Kilograms", "Kilograms to Ounces", "Ounces to Kilograms", "Pounds to Ounces", "Ounces to Pounds", "Kilograms to Grams", "Grams to Kilograms", "Pounds to Grams", "Grams to Pounds", "Ounces to Grams", "Grams to Ounces"]
drop = tk.OptionMenu(app, unit_choice, *unit_options)
drop.pack(pady=5)

app.mainloop

