import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, complexity):
    if complexity == "low":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
    else:
        raise ValueError("Invalid complexity level")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_clicked():
    try:
        length = int(length_entry.get())
        complexity = complexity_var.get()

        password = generate_password(length, complexity)
        generated_password_label.config(text="Generated Password: " + password)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid password length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Increase font size
font = ("Helvetica", 12)

# Create widgets
length_label = tk.Label(root, text="Enter the desired password length:", font=font)
length_entry = tk.Entry(root, width=5, font=font)  # Adjust the width here
complexity_label = tk.Label(root, text="Select complexity level:", font=font)
complexity_var = tk.StringVar()
complexity_var.set("medium")
complexity_menu = tk.OptionMenu(root, complexity_var, "low", "medium", "high")
complexity_menu.config(font=font)  # Set font for the option menu
generate_button = tk.Button(root, text="Generate Password", command=generate_button_clicked, font=font)
generated_password_label = tk.Label(root, text="Generated Password: ", font=font)

# Add colors
root.configure(bg="lightgray")
length_label.configure(bg="lightgray")
length_entry.configure(bg="white")
complexity_label.configure(bg="lightgray")
complexity_menu.configure(bg="white")
generate_button.configure(bg="green", fg="white")
generated_password_label.configure(bg="lightgray")

# Place widgets in the layout
length_label.pack(pady=10)
length_entry.pack(pady=5)
complexity_label.pack(pady=5)
complexity_menu.pack(pady=5)
generate_button.pack(pady=10)
generated_password_label.pack()

# Start the GUI event loop
root.mainloop()
