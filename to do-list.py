import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(
            self.frame, width=50, height=10, selectmode=tk.SINGLE)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        self.add_task_btn = tk.Button(
            root, text="Add Task", width=48, command=self.add_task)
        self.add_task_btn.pack(pady=5)

        self.update_task_btn = tk.Button(
            root, text="Update Selected Task", width=48, command=self.update_task)
        self.update_task_btn.pack(pady=5)

        self.delete_task_btn = tk.Button(
            root, text="Delete Selected Task", width=48, command=self.delete_task)
        self.delete_task_btn.pack(pady=5)

        self.list_tasks_btn = tk.Button(
            root, text="List All Tasks", width=48, command=self.list_tasks)
        self.list_tasks_btn.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            new_task = self.entry.get()
            if new_task != "":
                self.tasks[selected_task_index] = new_task
                self.listbox.delete(selected_task_index)
                self.listbox.insert(selected_task_index, new_task)
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def list_tasks(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
