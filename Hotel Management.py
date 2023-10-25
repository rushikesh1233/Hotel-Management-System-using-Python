import tkinter as tk
from tkinter import messagebox

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.guests = []
        
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.room_label = tk.Label(root, text="Room Number:")
        self.room_label.pack()
        self.room_entry = tk.Entry(root)
        self.room_entry.pack()

        self.checkin_button = tk.Button(root, text="Check In", command=self.check_in_guest)
        self.checkin_button.pack()

        self.checkout_button = tk.Button(root, text="Check Out", command=self.check_out_guest)
        self.checkout_button.pack()

        self.listbox = tk.Listbox(root, width=150, height=30)
        self.listbox.pack()

        self.display_guests()

    def check_in_guest(self):
        name = self.name_entry.get()
        room_number = self.room_entry.get()
        if name and room_number:
            guest = {"name": name, "room_number": room_number, "status": "Checked In"}
            self.guests.append(guest)
            self.display_guests()
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter both name and room number.")

    def check_out_guest(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            del self.guests[selected_index[0]]
            self.display_guests()

    def display_guests(self):
        self.listbox.delete(0, tk.END)
        for guest in self.guests:
            display_text = f"Name: {guest['name']}, Room: {guest['room_number']}, Status: {guest['status']}"
            self.listbox.insert(tk.END, display_text)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.room_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagementSystem(root)
    root.mainloop()
