import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Address Book")
root.geometry("400x200")
root.configure(bg="lightgrey")

contacts = []

def update_contact():
    # Refresh the listbox contents with contact names only
    contacts_listbox.delete(0, tk.END)
    for contact in contacts:
        contacts_listbox.insert(tk.END, contact['name'])

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()

    if name and phone and address:
        contact = {"name": name, "phone": phone, "address": address}
        contacts.append(contact)
        update_contact()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")


#entries
name_label = tk.Label(root, text="Name:", bg="lightblue", fg="black", font=("Arial", 12))
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

phone_label = tk.Label(root, text="Phone:", bg="lightblue", fg="black", font=("Arial", 12))
phone_label.grid(row=1, column=0, padx=10, pady=10)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=10, pady=10)

address_label = tk.Label(root, text="Address:", bg="lightblue", fg="black", font=("Arial", 12))
address_label.grid(row=2, column=0, padx=10, pady=10)
address_entry = tk.Entry(root)
address_entry.grid(row=2, column=1, padx=10, pady=10)


def delete_contact():
    selected_index = contacts_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        del contacts[index]
        update_contact()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Contact deleted successfully!")


def view_details(event=None):
    selected_index = contacts_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        contact = contacts[index]
        messagebox.showinfo("Contact Details", f"Name: {contact['name']}\nPhone: {contact['phone']}\nAddress: {contact['address']}")
    else:
        messagebox.showerror("Error", "Please select a contact to view details.")


# Now create buttons after callback functions are defined
add_button = tk.Button(root, text="Add Contact", bg="white", fg="black", font=("Arial", 12), command=add_contact)
add_button.grid(row=3, column=0, padx=10, pady=10)

contacts_listbox = tk.Listbox(root, width=50)
contacts_listbox.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

view_button = tk.Button(root, text="View Details", bg="white", fg="black", font=("Arial", 12), command=view_details)
view_button.grid(row=5, column=0, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Contact", bg="red", fg="white", font=("Arial", 12), command=lambda: delete_contact())
delete_button.grid(row=6, column=0, padx=10, pady=10)

update_button = tk.Button(root, text="Update Contact", bg="white", fg="black", font=("Arial", 12))  
update_button.grid(row=7, column=0, padx=10, pady=10)
                   
# Bind double-click on listbox items to view details
contacts_listbox.bind('<Double-Button-1>', view_details)












root.mainloop() 



