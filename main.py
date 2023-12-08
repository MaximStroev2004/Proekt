import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, filedialog
import subprocess
import os


def add_task():
    filename = filedialog.askopenfilename()
    if filename:
        tasks.append(filename)
        update_tasks()

def remove_task():
    task = task_list.get(tk.ACTIVE)
    if task in tasks:
        tasks.remove(task)
        update_tasks()


def start_task():
    selected_task = task_list.get(tk.ACTIVE)
    if selected_task:
        progress_bar.start()
        task_progress_label.configure(text="Выполняется: " + selected_task)
        if condition_is_met(selected_task):
            root.after(5000, finish_task)
        else:
            task_progress_label.configure(text="Задача не выполнена: условие не выполнено")

def condition_is_met(task):
    return True

def finish_task():
    progress_bar.stop()
    task_progress_label.configure(text="Ура! Проект Загружен. Также вы его можете и удалить")
    manage_project_task()

def update_tasks():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task)

def manage_project_task():
    selected_task = task_list.get(tk.ACTIVE)
    if selected_task:
        try:
            os.system(f'"{selected_task}"')
        except Exception as e:
            print("Ошибка открытия файла:", e)
    else:
        print("Выберите задачу для управления проектом")


tasks = []
background_color = '#91B4E8'

root = tk.Tk()
root.title("Управление проектами")
root.configure(background=background_color)

style = ttk.Style()
style.configure("C.TButton", font=("Arial", 12, "bold"))

style = ttk.Style()
style.map("C.TButton",
          background=[('active', 'green'), ('disabled', 'magenta')],
          foreground=[('active', 'white'), ('disabled', 'black')]
          )

add_button = ctk.CTkButton(root, text="Добавить проект", command=add_task)
remove_button = ctk.CTkButton(root, text="Удалить проект", command=remove_task)
start_button = ctk.CTkButton(root, text="Управление проектом", command=start_task)
progress_bar = ctk.CTkProgressBar(root, mode="indeterminate")
task_progress_label = ctk.CTkLabel(root, text="", text_color='black')

task_list = tk.Listbox(root, background=background_color)
task_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ctk.CTkScrollbar(task_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=task_list.yview)

add_button.pack(side=tk.LEFT, padx=5)
remove_button.pack(side=tk.LEFT, padx=5)
start_button.pack(side=tk.LEFT, padx=5)
progress_bar.pack(side=tk.LEFT, padx=5)
task_progress_label.pack(side=tk.LEFT)

root.mainloop()
