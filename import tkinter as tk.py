import tkinter as tk
from tkinter import messagebox
import pyodbc

# 连接到SQL Server数据库
conn = pyodbc.connect('DRIVER={your Server};'
                      'SERVER=your ip;'
                      'DATABASE=your database;'
                      'UID=your uid;'
                      'PWD=your pwd')

# 创建游标对象
cursor = conn.cursor()

# 检查表是否存在
cursor.execute("IF OBJECT_ID('students', 'U') IS NULL CREATE TABLE students (id INT IDENTITY(1,1) PRIMARY KEY, name NVARCHAR(255), age INT)")

def add_student():
    name = name_entry.get()
    age = age_entry.get()
    if name and age:
        cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
        conn.commit()
        messagebox.showinfo("Success", "Student added successfully!")
    else:
        messagebox.showerror("Error", "Please enter both name and age.")

def show_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    if students:
        for i, student in enumerate(students, start=1):
            student_listbox.insert(tk.END, f"{i}. Name: {student.name}, Age: {student.age}")
    else:
        messagebox.showinfo("Info", "No students found.")

# 创建主窗口
root = tk.Tk()
root.title("Student Management System")

# 创建界面组件
tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Age:").grid(row=1, column=0, padx=5, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=5, pady=5)

add_button = tk.Button(root, text="Add Student", command=add_student)
add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")

show_button = tk.Button(root, text="Show Students", command=show_students)
show_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

student_listbox = tk.Listbox(root)
student_listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

# 设置列表框和主窗口的拉伸性
root.rowconfigure(4, weight=1)
root.columnconfigure(0, weight=1)

root.mainloop()
