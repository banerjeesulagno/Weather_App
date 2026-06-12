import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        # Task storage
        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(
            self.root,
            text="My To-Do List",
            font=("Arial", 20, "bold")
        )
        title_label.pack(pady=10)

        # Entry Frame
        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(
            entry_frame,
            width=40,
            font=("Arial", 12)
        )
        self.task_entry.grid(row=0, column=0, padx=5)

        add_btn = tk.Button(
            entry_frame,
            text="Add Task",
            width=15,
            command=self.add_task
        )
        add_btn.grid(row=0, column=1, padx=5)

        # List Frame
        list_frame = tk.Frame(self.root)
        list_frame.pack(pady=10)

        # Scrollbar
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Task Listbox
        self.task_listbox = tk.Listbox(
            list_frame,
            width=60,
            height=15,
            font=("Arial", 12),
            yscrollcommand=scrollbar.set
        )

        self.task_listbox.pack(side=tk.LEFT)

        scrollbar.config(command=self.task_listbox.yview)

        # Button Frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=15)

        complete_btn = tk.Button(
            button_frame,
            text="Mark Complete",
            width=15,
            command=self.mark_complete
        )
        complete_btn.grid(row=0, column=0, padx=5)

        delete_btn = tk.Button(
            button_frame,
            text="Delete Task",
            width=15,
            command=self.delete_task
        )
        delete_btn.grid(row=0, column=1, padx=5)

        clear_btn = tk.Button(
            button_frame,
            text="Clear All",
            width=15,
            command=self.clear_all_tasks
        )
        clear_btn.grid(row=0, column=2, padx=5)

    def add_task(self):
        task = self.task_entry.get().strip()

        if task == "":
            messagebox.showwarning(
                "Warning",
                "Please enter a task."
            )
            return

        self.tasks.append({
            "task": task,
            "completed": False
        })

        self.task_entry.delete(0, tk.END)
        self.update_task_list()

    def mark_complete(self):
        try:
            index = self.task_listbox.curselection()[0]

            if not self.tasks[index]["completed"]:
                self.tasks[index]["completed"] = True
                self.update_task_list()

        except IndexError:
            messagebox.showwarning(
                "Warning",
                "Please select a task."
            )

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]

            task_name = self.tasks[index]["task"]

            confirm = messagebox.askyesno(
                "Delete Task",
                f"Delete '{task_name}'?"
            )

            if confirm:
                self.tasks.pop(index)
                self.update_task_list()

        except IndexError:
            messagebox.showwarning(
                "Warning",
                "Please select a task."
            )

    def clear_all_tasks(self):
        if not self.tasks:
            messagebox.showinfo(
                "Info",
                "No tasks available."
            )
            return

        confirm = messagebox.askyesno(
            "Clear All",
            "Are you sure you want to remove all tasks?"
        )

        if confirm:
            self.tasks.clear()
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)

        for task in self.tasks:
            status = "✓" if task["completed"] else "○"
            display_text = f"{status} {task['task']}"
            self.task_listbox.insert(tk.END, display_text)


# Main Program
if __name__ == "__main__":
    root = tk.Tk()

    app = TodoApp(root)

    root.mainloop()