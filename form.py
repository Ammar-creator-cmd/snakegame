import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk() # Create the main window
root.title("User Information Form")
root.config(bg="lightblue")

#create a style for the widgets
style = ttk.Style()
style.theme_use("clam")
style.configure("TEntry", foreground="black", background="white")
style.configure("TLabel", foreground="black", background="lightblue")
style.configure("TButton", foreground="white", background="red")
style.configure("TCombobox", foreground="black", background="lightblue")


def submit():
    pass

name_label = ttk.Label(root, text="Name:")
name_label.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

email_label = ttk.Label(root, text="Email:")
email_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

#create password
password_label = ttk.Label(root, text="Password:")
password_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

#password confirmation
confirm_password_label = ttk.Label(root, text="Confirm Password:")
confirm_password_label.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

#create gender label
gender_label = ttk.Label(root, text="Gender:")
gender_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

#create country label
country_label = ttk.Label(root, text="Country:")
country_label.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

#create bio label
bio_label = ttk.Label(root, text="Bio:")
bio_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

#text input for every labels
name_entry = ttk.Entry(root, width=30)
name_entry.grid(row=1, column=0, padx=10, pady=10)

email_entry = ttk.Entry(root, width=30)
email_entry.grid(row=1, column=1, padx=10, pady=10)

password_entry = ttk.Entry(root, width=30, show="*")
password_entry.grid(row=1, column=0, padx=10, pady=10)

confirm_password_entry = ttk.Entry(root, width=30, show="*")
confirm_password_entry.grid(row=1, column=1, padx=10, pady=10)

gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(root, textvariable=gender_var, width=28)
gender_combobox['values'] = ('Male', 'Female', 'Other')
gender_combobox.grid(row=3, column=0, padx=10, pady=10)

country_var = tk.StringVar()
country_combobox = ttk.Combobox(root, textvariable=country_var, width=28)
country_combobox['values'] = ('USA', 'Canada', 'UK', 'Australia')
country_combobox.grid(row=3, column=1, padx=10, pady=10)

bio_text = tk.Text(root, width=30, height=5)
bio_text.grid(row=5, column=0, padx=10, pady=10, columnspan=2)




root.mainloop() # Start the main event loop