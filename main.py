import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Task Manager")

def add_task():
    task_text = task_entry.get()
    if task_text != "":
        to_do_list.insert(tk.END, task_text)
        task_entry.delete(0, tk.END)
    return

def move_to_inpro():
    selected_task = to_do_list.curselection()

    if selected_task:
        task = to_do_list.get(selected_task)
        to_do_list.delete(selected_task)

        inpro_list.insert(tk.END, task)
def move_to_done():
    selected_task = inpro_list.curselection()
    if selected_task:
        task = inpro_list.get(selected_task)
        inpro_list.delete(selected_task)
        print("check")
        done_list.insert(tk.END, task)



task_entry = tk.Entry(root, width=30)
task_entry.grid(row=0, column=1, padx=0, pady=10, sticky="ew")

add_task_button = tk.Button(root, text="Add task", command = add_task)
add_task_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

to_do_list_label = tk.Label(root, text="To Do")
to_do_list_label.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
to_do_list = tk.Listbox(root, height=30, width=30)
to_do_list.grid(row=3, column=0, padx=10, pady=10, sticky = "ew")

inpro_list_label = tk.Label(text="In Progress")
inpro_list_label.grid(row=2, column = 1, padx=10, pady = 10, sticky = "ew")
inpro_list = tk.Listbox(root, height=30, width=30)
inpro_list.grid(row=3, column=1, padx=10, pady=10, sticky = "ew")
move_to_inpro_button = tk.Button(root, text="Mark as progressed", command=move_to_inpro)
move_to_inpro_button.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

done_list_label = tk.Label(root,text="Done").grid(row=2, column=2, padx=10, pady=10, sticky="ew")
done_list = tk.Listbox(root, height=30, width=30)
done_list.grid(row=3, column = 2, padx=10, pady=10, sticky="ew")
move_to_done_button = tk.Button(root, text="Mark as Done", command=move_to_done)
move_to_done_button.grid(row=4, column=1, padx=10, pady=10, sticky="ew")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

root.mainloop()