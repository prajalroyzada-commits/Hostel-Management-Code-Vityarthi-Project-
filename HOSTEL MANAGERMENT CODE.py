import tkinter as tk
from tkinter import messagebox

student_list = []


def add_student():

    sid = student_id.get()
    name = student_name.get()
    course = student_course.get()
    room = student_room.get()

    if sid == "" or name == "" or course == "" or room == "":
        messagebox.showwarning("Warning", "Please fill all the details")
        return

    for student in student_list:

        if student[0] == sid:
            messagebox.showerror("Error", "Student ID already exists")
            return

    student_list.append([sid, name, course, room])

    messagebox.showinfo("Success", "Student added successfully")

    clear_fields()
    show_students()


def show_students():

    output.delete("1.0", tk.END)

    if len(student_list) == 0:
        output.insert(tk.END, "No student records found.")
        return

    for student in student_list:

        output.insert(
            tk.END,
            "Student ID : " + student[0] + "\n"
            "Name       : " + student[1] + "\n"
            "Course     : " + student[2] + "\n"
            "Room No.   : " + student[3] + "\n"
            "--------------------------------\n"
        )


def delete_student():

    sid = student_id.get()

    for student in student_list:

        if student[0] == sid:

            student_list.remove(student)

            messagebox.showinfo("Success", "Student removed")

            clear_fields()
            show_students()

            return

    messagebox.showerror("Error", "Student ID not found")


def clear_fields():

    student_id.delete(0, tk.END)
    student_name.delete(0, tk.END)
    student_course.delete(0, tk.END)
    student_room.delete(0, tk.END)


# Create the main window
window = tk.Tk()

window.title("VIT Bhopal Hostel Management")
window.geometry("600x600")


# University heading
tk.Label(
    window,
    text="VIT BHOPAL UNIVERSITY",
    font=("Arial", 20, "bold")
).pack(pady=15)


# Project heading
tk.Label(
    window,
    text="Hostel Management System",
    font=("Arial", 14)
).pack()


# Student form
form = tk.Frame(window)
form.pack(pady=20)


tk.Label(
    form,
    text="Student ID"
).grid(row=0, column=0, padx=10, pady=7)

student_id = tk.Entry(form, width=30)
student_id.grid(row=0, column=1)


tk.Label(
    form,
    text="Student Name"
).grid(row=1, column=0, padx=10, pady=7)

student_name = tk.Entry(form, width=30)
student_name.grid(row=1, column=1)


tk.Label(
    form,
    text="Course"
).grid(row=2, column=0, padx=10, pady=7)

student_course = tk.Entry(form, width=30)
student_course.grid(row=2, column=1)


tk.Label(
    form,
    text="Room Number"
).grid(row=3, column=0, padx=10, pady=7)

student_room = tk.Entry(form, width=30)
student_room.grid(row=3, column=1)


# Add student button
tk.Button(
    window,
    text="Add Student",
    width=20,
    command=add_student
).pack(pady=4)


# Show students button
tk.Button(
    window,
    text="Show Students",
    width=20,
    command=show_students
).pack(pady=4)


# Delete student button
tk.Button(
    window,
    text="Delete Student",
    width=20,
    command=delete_student
).pack(pady=4)


# Clear button
tk.Button(
    window,
    text="Clear",
    width=20,
    command=clear_fields
).pack(pady=4)


# Exit button
tk.Button(
    window,
    text="Exit",
    width=20,
    command=window.destroy
).pack(pady=4)


# Area for displaying student records
output = tk.Text(
    window,
    width=65,
    height=12
)

output.pack(pady=15)


# Start the application
window.mainloop()