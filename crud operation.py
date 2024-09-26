import tkinter as tk
from tkinter import messagebox
import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost", user="root", password="", database="school"
    )

def create_student():
    name = entry_name.get()
    age = entry_age.get()

    if name and age:
        connection = connect()
        cursor = connection.cursor()
        sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
        values = (name, age)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        messagebox.showinfo("Success", f"Student {name} added successfully!")
        clear_entries()
        read_students()  # Update listbox
    else:
        messagebox.showerror("Input Error", "Please fill in all fields")

def read_students():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    listbox_students.delete(0, tk.END)  # Clear listbox
    if result:
        for student in result:
            listbox_students.insert(tk.END, f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}")
    cursor.close()
    connection.close()

def update_student():
    selected_student = listbox_students.get(tk.ACTIVE)
    if not selected_student:
        messagebox.showerror("Selection Error", "Please select a student to update")
        return

    student_id = selected_student.split(',')[0].split(': ')[1]  # Extract ID
    name = entry_name.get()
    age = entry_age.get()

    if name or age:
        connection = connect()
        cursor = connection.cursor()
        if name and age:
            sql = "UPDATE students SET name = %s, age = %s WHERE id = %s"
            values = (name, age, student_id)
        elif name:
            sql = "UPDATE students SET name = %s WHERE id = %s"
            values = (name, student_id)
        elif age:
            sql = "UPDATE students SET age = %s WHERE id = %s"
            values = (age, student_id)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        messagebox.showinfo("Success", f"Student ID {student_id} updated successfully!")
        clear_entries()
        read_students()  # Update listbox
    else:
        messagebox.showerror("Input Error", "Please provide new name or age to update")

def delete_student():
    selected_student = listbox_students.get(tk.ACTIVE)
    if not selected_student:
        messagebox.showerror("Selection Error", "Please select a student to delete")
        return

    student_id = selected_student.split(',')[0].split(': ')[1]  # Extract ID
    connection = connect()
    cursor = connection.cursor()
    sql = "DELETE FROM students WHERE id = %s"
    values = (student_id,)
    cursor.execute(sql, values)
    connection.commit()
    cursor.close()
    connection.close()
    messagebox.showinfo("Success", f"Student ID {student_id} deleted successfully!")
    read_students()  

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)

root = tk.Tk()
root.title("Student Management System")

label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=10)

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_age = tk.Label(root, text="Age:")
label_age.grid(row=1, column=0, padx=10, pady=10)

entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1, padx=10, pady=10)

button_add = tk.Button(root, text="Add Student", command=create_student)
button_add.grid(row=2, column=0, padx=10, pady=10)

button_update = tk.Button(root, text="Update Student", command=update_student)
button_update.grid(row=2, column=1, padx=10, pady=10)

button_delete = tk.Button(root, text="Delete Student", command=delete_student)
button_delete.grid(row=3, column=0, padx=10, pady=10)

button_clear = tk.Button(root, text="Clear Fields", command=clear_entries)
button_clear.grid(row=3, column=1, padx=10, pady=10)

listbox_students = tk.Listbox(root, width=50)
listbox_students.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

read_students()

root.mainloop()
