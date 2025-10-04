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
style.configure("TLabel", foreground ="black", background="lightblue")
style.configure("TButton", foreground="white", background="red")
style.configure("TCombobox", foreground="black", background="lightblue")
style.configure("TRadiobutton", foreground="black", background="lightblue")


def submit():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    gender = gender_var.get()
    country = country_var.get()
    bio = bio_text.get("1.0", tk.END).strip()
    if not name or not email or not password or not confirm_password or not gender or not country:
        messagebox.showerror("Error", "Please fill in all required fields.")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Password is invalid.")
        return
    messagebox.showinfo("Success", "Form submitted successfully!")
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_password_entry.delete(0, tk.END)
    country_combobox.delete(0, tk.END)
    bio_text.delete("1.0", tk.END)

    print("Name:", name)
    print("Email:", email)
    print("Password:", password)
    print("Confirm Password:", confirm_password)
    print("Gender:", gender)
    print("Country:", country)
    print("Bio:", bio)





name_label = ttk.Label(root, text="Name:")
name_label.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

email_label = ttk.Label(root, text="Email:")
email_label.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

#create password
password_label = ttk.Label(root, text="Password:")
password_label.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W)

#password confirmation
confirm_password_label = ttk.Label(root, text="Confirm Password:")
confirm_password_label.grid(row=6, column=1, padx=10, pady=10, sticky=tk.W)

#create gender label
gender_label = ttk.Label(root, text="Gender:")
gender_label.grid(row=8, column=1, padx=10, pady=10, sticky=tk.W)

#create country label
country_label = ttk.Label(root, text="Country:")
country_label.grid(row=10, column=1, padx=10, pady=10, sticky=tk.W)

#create bio label
bio_label = ttk.Label(root, text="Bio:")
bio_label.grid(row=12, column=1, padx=10, pady=10, sticky=tk.W)


#text input for every labels
#name
name_entry = ttk.Entry(root, width=30)
name_entry.grid(row=1, column=1, padx=10, pady=10)

#email
email_entry = ttk.Entry(root, width=30)
email_entry.grid(row=3, column=1, padx=10, pady=10)

#passwort
password_entry = ttk.Entry(root, width=30, show="*")
password_entry.grid(row=5, column=1, padx=10, pady=10)

#confirmation of password
confirm_password_entry = ttk.Entry(root, width=30, show="*")
confirm_password_entry.grid(row=7, column=1, padx=10, pady=10)

# Gender radio buttons
gender_var = tk.StringVar()
gender_var.set("Male")

# Gender radio buttons in a frame
gender_frame = tk.Frame(root, bg="lightblue")
gender_frame.grid(row=9, column=1, padx=10, pady=10, sticky=tk.W, columnspan=3)

male_radiobutton = ttk.Radiobutton(gender_frame, text="Male", value="Male", variable=gender_var)
male_radiobutton.pack(side=tk.LEFT, padx=10)

female_radiobutton = ttk.Radiobutton(gender_frame, text="Female", value="Female", variable=gender_var)
female_radiobutton.pack(side=tk.LEFT, padx=10)

other_radiobutton = ttk.Radiobutton(gender_frame, text="Other", value="Other", variable=gender_var)
other_radiobutton.pack(side=tk.LEFT, padx=10)

#country combobox
country_var = tk.StringVar()
country_combobox = ttk.Combobox(root, textvariable=country_var, width=28)
countries = [
    'USA', 'Canada', 'UK', 'Australia', 'India', 'Indonesia', 'Germany', 'France', 'Scotland', 'Italy', 'Spain', 'Mexico', 'Brazil', 'Argentina', 'Colombia', 'Chile', 'Peru', 'Venezuela', 'South Africa', 'Nigeria', 'Egypt', 'Kenya', 'Turkey', 'Russia', 'China', 'Japan', 'South Korea', 'Thailand', 'Vietnam', 'Philippines', 'Malaysia', 'Singapore', 'New Zealand', 'Cambodia', 'Laos', 'Myanmar', 'Bangladesh', 'Pakistan', 'Sri Lanka', 'Nepal', 'Bhutan', 'Maldives', 'Saudi Arabia', 'UAE', 'Palestine', 'Jordan', 'Lebanon', 'Syria', 'Iraq', 'Iran', 'Afghanistan', 'Kazakhstan', 'Uzbekistan', 'Turkmenistan', 'Kyrgyzstan', 'Tajikistan', 'Mongolia', 'North Korea', 'Wales', 'Northern Ireland', 'Ireland', 'Belgium', 'Netherlands', 'Switzerland', 'Austria', 'Portugal', 'Greece', 'Hungary', 'Poland', 'Czech Republic', 'Slovakia', 'Croatia', 'Serbia', 'Bulgaria', 'Romania', 'Ukraine', 'Belarus', 'Lithuania', 'Latvia', 'Estonia', 'Finland', 'Norway', 'Sweden', 'Denmark', 'Iceland', 'Cuba', 'Jamaica', 'Haiti', 'Dominican Republic', 'Puerto Rico', 'Costa Rica', 'Panama', 'Guatemala', 'Honduras', 'El Salvador', 'Nicaragua', 'Bolivia', 'Ecuador', 'Uruguay', 'Paraguay', 'Suria', 'Guyana', 'French Guiana', 'Libya', 'Tunisia', 'Algeria', 'Morocco', 'Sudan', 'Ethiopia', 'Tanzania', 'Uganda', 'Rwanda', 'Burundi', 'Zambia', 'Zimbabwe', 'Botswana', 'Namibia', 'Mozambique', 'Angola', 'Ghana', 'Ivory Coast', 'Senegal', 'Cameroon', 'Gabon', 'Congo', 'DR Congo', 'Mali', 'Niger', 'Chad', 'Somalia', 'Yemen', 'Oman', 'Qatar', 'Bahrain', 'Kuwait', 'Azerbaijan', 'Armenia', 'Georgia', 'Moldova', 'Cyprus', 'Singapore', 'Brunei', 'East-Timor', 'Fiji', 'Papua New Guinea', 'Samoa', 'Tonga', 'Vanuatu', 'Solomon Islands', 'Malta', 'Luxembourg', 'Monaco', 'Liechtenstein', 'San Marino', 'Andorra', 'Vatican City'
]
country_combobox['values'] = sorted(countries)
country_combobox.grid(row=11, column=1, padx=10, pady=10)

#li'l info abt urself
bio_text = tk.Text(root, width=30, height=5)
bio_text.grid(row=13, column=1, padx=10, pady=10, columnspan=2)

#submit button
submit_button = ttk.Button(root, text="Submit",cursor = "hand2",style = "TButton", command=submit)
submit_button.grid(row=14, column=1, padx=10, pady=10)



root.mainloop() # Start the main event loop