import tkinter as tk
from tkinter import messagebox
import json

class HotelBookingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Booking System")
        self.bookings = []

        # GUI Components
        self.label_name = tk.Label(root, text="Guest Name:")
        self.entry_name = tk.Entry(root)

        self.label_room = tk.Label(root, text="Room Number:")
        self.entry_room = tk.Entry(root)

        self.btn_book = tk.Button(root, text="Book Room", command=self.book_room)
        self.btn_display = tk.Button(root, text="Display Bookings", command=self.display_bookings)
        self.btn_save = tk.Button(root, text="Save to JSON", command=self.save_to_json)

        # Layout
        self.label_name.grid(row=0, column=0, padx=10, pady=5)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.label_room.grid(row=1, column=0, padx=10, pady=5)
        self.entry_room.grid(row=1, column=1, padx=10, pady=5)

        self.btn_book.grid(row=2, column=0, columnspan=2, pady=10)
        self.btn_display.grid(row=3, column=0, columnspan=2, pady=10)
        self.btn_save.grid(row=4, column=0, columnspan=2, pady=10)

    def book_room(self):
        guest_name = self.entry_name.get()
        room_number = self.entry_room.get()

        if guest_name and room_number:
            booking = {"Guest Name": guest_name, "Room Number": room_number}
            self.bookings.append(booking)
            messagebox.showinfo("Booking Successful", f"Room {room_number} booked for {guest_name}.")
            self.clear_entries()
        else:
            messagebox.showwarning("Incomplete Information", "Please enter both guest name and room number.")

    def display_bookings(self):
        if not self.bookings:
            messagebox.showinfo("No Bookings", "No bookings have been made yet.")
        else:
            booking_info = "\n".join([f"{i + 1}. {booking['Guest Name']} - Room {booking['Room Number']}" for i, booking in enumerate(self.bookings)])
            messagebox.showinfo("Bookings", booking_info)

    def save_to_json(self):
        if not self.bookings:
            messagebox.showwarning("No Data", "No bookings to save.")
        else:
            with open("bookings.json", "w") as file:
                json.dump(self.bookings, file)
            messagebox.showinfo("Save Successful", "Bookings saved to bookings.json.")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_room.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = HotelBookingSystem(root)
    root.mainloop()
