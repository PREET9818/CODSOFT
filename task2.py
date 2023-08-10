import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("400x600")  # Adjust the window size

        self.entry = tk.Entry(root, width=30, font=("Helvetica", 20))  # Increase font size
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('sqrt', 5, 0), ('^', 5, 1), ('C', 5, 2), ('Exit', 5, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, command=lambda t=text: self.on_button_click(t),
                                font=("Helvetica", 20), padx=20, pady=20)  # Increase font size and padding
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        if char == "=":
            try:
                expression = self.entry.get()
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")

        elif char == "C":
            self.entry.delete(0, tk.END)

        elif char == "sqrt":
            try:
                value = float(self.entry.get())
                result = value ** 0.5
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")

        elif char == "^":
            self.entry.insert(tk.END, "**")

        elif char == "Exit":
            self.root.destroy()

        else:
            self.entry.insert(tk.END, char)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
