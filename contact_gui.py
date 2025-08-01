import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

CONTACTS_FILE = "contacts.json"

# Load and Save
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

# Main Class
class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.contacts = load_contacts()

        # UI Elements
        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=10)

        self.refresh_contacts()

        # Buttons
        tk.Button(root, text="Add Contact", command=self.add_contact).pack(pady=2)
        tk.Button(root, text="Edit Contact", command=self.edit_contact).pack(pady=2)
        tk.Button(root, text="Delete Contact", command=self.delete_contact).pack(pady=2)

    def refresh_contacts(self):
        self.listbox.delete(0, tk.END)
        for idx, contact in enumerate(self.contacts):
            entry = f"{idx+1}. {contact['name']} | {contact['phone']} | {contact['email']}"
            self.listbox.insert(tk.END, entry)

    def add_contact(self):
        name = simpledialog.askstring("Name", "Enter Name:")
        phone = simpledialog.askstring("Phone", "Enter Phone Number:")
        email = simpledialog.askstring("Email", "Enter Email:")
        if name and phone and email:
            self.contacts.append({"name": name, "phone": phone, "email": email})
            save_contacts(self.contacts)
            self.refresh_contacts()
        else:
            messagebox.showerror("Error", "All fields are required.")

    def edit_contact(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Select a contact to edit.")
            return
        index = selected[0]
        contact = self.contacts[index]
        name = simpledialog.askstring("Edit Name", "Enter new name:", initialvalue=contact['name'])
        phone = simpledialog.askstring("Edit Phone", "Enter new phone number:", initialvalue=contact['phone'])
        email = simpledialog.askstring("Edit Email", "Enter new email:", initialvalue=contact['email'])
        if name and phone and email:
            self.contacts[index] = {"name": name, "phone": phone, "email": email}
            save_contacts(self.contacts)
            self.refresh_contacts()

    def delete_contact(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Select a contact to delete.")
            return
        index = selected[0]
        contact = self.contacts[index]
        confirm = messagebox.askyesno("Delete", f"Delete {contact['name']}?")
        if confirm:
            self.contacts.pop(index)
            save_contacts(self.contacts)
            self.refresh_contacts()

# Run GUI
root = tk.Tk()
app = ContactManager(root)
root.mainloop()
