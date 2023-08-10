import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []
        self.selected_index = None

        self.task_label = tk.Label(root, text="Task:", font=("Helvetica", 14))
        self.task_label.pack()

        self.task_entry = tk.Entry(root, font=("Helvetica", 14))
        self.task_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="green", fg="white", font=("Helvetica", 12, "bold"))
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root,bg="beige" , fg= "black" ,selectbackground="lightblue", font=("Comic Sans MS", 17))
        self.task_listbox.pack()
        self.task_listbox.bind("<<ListboxSelect>>", self.select_task)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task, bg="blue", fg="white", font=("Helvetica", 12, "bold"))
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg="red", fg="white", font=("Helvetica", 12, "bold"))
        self.delete_button.pack()

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.save_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def select_task(self, event):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.selected_index = selected_index[0]
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, self.tasks[self.selected_index])

    def update_task(self):
        if self.selected_index is not None:
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[self.selected_index] = new_task
                self.update_task_listbox()
                self.save_tasks()
                self.task_entry.delete(0, tk.END)
                self.selected_index = None
            else:
                messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        if self.selected_index is not None:
            del self.tasks[self.selected_index]
            self.update_task_listbox()
            self.save_tasks()
            self.selected_index = None

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert(tk.END, f"{index}. {task}")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
            self.update_task_listbox()
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
             for index, task in enumerate(self.tasks, start=1):
                file.write(f"{index}. {task}\n")

if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap("icon.ico")
    root.configure(bg="lightgray")
    app = ToDoListApp(root)
    app.task_entry.configure(bg="lightblue")
    root.mainloop()
