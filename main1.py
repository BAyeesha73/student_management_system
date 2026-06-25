import tkinter as tk
from tkinter import ttk, messagebox
import database as db

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Student Management System")
root.geometry("750x500")

# ---------------- VARIABLES ----------------
name_var = tk.StringVar()
age_var = tk.StringVar()
course_var = tk.StringVar()
search_var = tk.StringVar()

# ---------------- INPUT FIELDS ----------------
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=name_var).grid(row=0, column=1)

tk.Label(root, text="Age").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=age_var).grid(row=1, column=1)

tk.Label(root, text="Course").grid(row=2, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=course_var).grid(row=2, column=1)

# ---------------- FUNCTIONS ----------------
def clear_fields():
    name_var.set("")
    age_var.set("")
    course_var.set("")


def load_students():
    for row in tree.get_children():
        tree.delete(row)

    for row in db.fetch_students():
        tree.insert("", tk.END, values=row)


def add_student():
    if name_var.get() == "" or age_var.get() == "" or course_var.get() == "":
        messagebox.showerror("Error", "All fields are required")
        return

    db.insert_student(name_var.get(), age_var.get(), course_var.get())
    messagebox.showinfo("Success", "Student Added Successfully")
    clear_fields()
    load_students()


def delete_student():
    selected = tree.focus()
    if not selected:
        messagebox.showerror("Error", "Select a student")
        return

    data = tree.item(selected)['values']
    db.delete_student(data[0])
    load_students()


def update_student():
    selected = tree.focus()
    if not selected:
        messagebox.showerror("Error", "Select a student")
        return

    data = tree.item(selected)['values']
    db.update_student(
        data[0],
        name_var.get(),
        age_var.get(),
        course_var.get()
    )
    messagebox.showinfo("Updated", "Student Updated Successfully")
    load_students()


def search_student():
    keyword = search_var.get()

    for row in tree.get_children():
        tree.delete(row)

    results = db.search_student(keyword)

    for row in results:
        tree.insert("", tk.END, values=row)


def show_all():
    load_students()

# ---------------- BUTTONS ----------------
tk.Button(root, text="Add Student", command=add_student).grid(row=3, column=0, pady=10)
tk.Button(root, text="Update", command=update_student).grid(row=3, column=1)
tk.Button(root, text="Delete", command=delete_student).grid(row=3, column=2)

tk.Entry(root, textvariable=search_var).grid(row=4, column=0)
tk.Button(root, text="Search", command=search_student).grid(row=4, column=1)
tk.Button(root, text="Show All", command=show_all).grid(row=4, column=2)

# ---------------- TABLE ----------------
tree = ttk.Treeview(root, columns=("ID", "Name", "Age", "Course"), show="headings")

tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Course", text="Course")

tree.column("ID", width=50)
tree.column("Name", width=150)
tree.column("Age", width=100)
tree.column("Course", width=150)

tree.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

# ---------------- LOAD DATA ----------------
load_students()

# ---------------- RUN APP ----------------
root.mainloop()