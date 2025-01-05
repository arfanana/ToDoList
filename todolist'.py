import customtkinter as ctk
import tkinter as tk
from CTkListbox import *

# Initialize the application
ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("blue")  

class ToDoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("To-Do List")
        self.geometry("400x500")

        # Title Label
        self.title_label = ctk.CTkLabel(self, text="To-Do List", font=("Arial", 24))
        self.title_label.pack(pady=10)

        # Task Entry
        self.task_entry = ctk.CTkEntry(self, placeholder_text="Enter a new task")
        self.task_entry.pack(pady=10, padx=20, fill="x")

        # Add Task Button
        self.add_task_button = ctk.CTkButton(self, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Task List
        self.task_listbox = CTkListbox(self, height=15, width=50)
        self.task_listbox.pack(pady=10, padx=20, fill="both", expand=True)
        # Action Buttons
        self.complete_task_button = ctk.CTkButton(self, text="Complete Task", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        self.delete_task_button = ctk.CTkButton(self, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert("end", task)
            self.task_entry.delete(0, "end")

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert("end", f"[Completed] {task}")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)

if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()
