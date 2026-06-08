import tkinter as tk
from tkinter import ttk, messagebox

contacts = []

# Add Contact
def add_contact():
    store = store_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not store or not phone:
        messagebox.showerror("Error", "Store Name and Phone Number are required!")
        return

    for contact in contacts:
        if contact["phone"] == phone:
            messagebox.showerror("Error", "Phone number already exists!")
            return

    contacts.append({
        "store": store,
        "phone": phone,
        "email": email,
        "address": address
    })

    refresh_table()
    clear_fields()
    messagebox.showinfo("Success", "Contact Added Successfully!")

# View Contacts
def refresh_table():
    for row in tree.get_children():
        tree.delete(row)

    for contact in contacts:
        tree.insert("", tk.END, values=(
            contact["store"],
            contact["phone"],
            contact["email"],
            contact["address"]
        ))

# Search Contact
def search_contact():
    keyword = search_entry.get().lower()

    for row in tree.get_children():
        tree.delete(row)

    for contact in contacts:
        if (keyword in contact["store"].lower() or
                keyword in contact["phone"]):
            tree.insert("", tk.END, values=(
                contact["store"],
                contact["phone"],
                contact["email"],
                contact["address"]
            ))

# Select Contact
def select_contact(event):
    selected = tree.focus()

    if selected:
        values = tree.item(selected, "values")

        store_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)

        store_entry.insert(0, values[0])
        phone_entry.insert(0, values[1])
        email_entry.insert(0, values[2])
        address_entry.insert(0, values[3])

# Update Contact
def update_contact():
    selected = tree.focus()

    if not selected:
        messagebox.showwarning("Warning", "Select a contact first!")
        return

    old_phone = tree.item(selected, "values")[1]

    for contact in contacts:
        if contact["phone"] == old_phone:
            contact["store"] = store_entry.get()
            contact["phone"] = phone_entry.get()
            contact["email"] = email_entry.get()
            contact["address"] = address_entry.get()
            break

    refresh_table()
    clear_fields()
    messagebox.showinfo("Success", "Contact Updated!")

# Delete Contact
def delete_contact():
    selected = tree.focus()

    if not selected:
        messagebox.showwarning("Warning", "Select a contact first!")
        return

    phone = tree.item(selected, "values")[1]

    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            break

    refresh_table()
    clear_fields()
    messagebox.showinfo("Success", "Contact Deleted!")

# Clear Fields
def clear_fields():
    store_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Main Window
root = tk.Tk()
root.title("Contact book")
root.geometry("850x600")
root.configure(bg="lightblue")

title = tk.Label(
    root,
    text="CONTACT BOOK",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
title.pack(pady=10)

# Form Frame
form_frame = tk.Frame(root, bg="lightblue")
form_frame.pack(pady=10)

tk.Label(form_frame, text="Store Name", bg="lightblue").grid(row=0, column=0)
store_entry = tk.Entry(form_frame, width=30)
store_entry.grid(row=0, column=1)

tk.Label(form_frame, text="Phone Number", bg="lightblue").grid(row=1, column=0)
phone_entry = tk.Entry(form_frame, width=30)
phone_entry.grid(row=1, column=1)

tk.Label(form_frame, text="Email", bg="lightblue").grid(row=2, column=0)
email_entry = tk.Entry(form_frame, width=30)
email_entry.grid(row=2, column=1)

tk.Label(form_frame, text="Address", bg="lightblue").grid(row=3, column=0)
address_entry = tk.Entry(form_frame, width=30)
address_entry.grid(row=3, column=1)

# Buttons
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add", command=add_contact, width=12).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Update", command=update_contact, width=12).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete", command=delete_contact, width=12).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Clear", command=clear_fields, width=12).grid(row=0, column=3, padx=5)

# Search
search_frame = tk.Frame(root, bg="lightblue")
search_frame.pack(pady=10)

tk.Label(search_frame, text="Search", bg="lightblue").pack(side=tk.LEFT)

search_entry = tk.Entry(search_frame, width=30)
search_entry.pack(side=tk.LEFT, padx=5)

tk.Button(search_frame, text="Search", command=search_contact).pack(side=tk.LEFT)

# Table
columns = ("Store Name", "Phone Number", "Email", "Address")

tree = ttk.Treeview(root, columns=columns, show="headings", height=15)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=180)

tree.pack(pady=10, fill="both", expand=True)

tree.bind("<<TreeviewSelect>>", select_contact)

root.mainloop()
