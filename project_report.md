# VIT Bhopal University Hostel Management

**Project Report**

**Author:** PRAJAL ROYZADA

---

## 1. Introduction

VIT Bhopal University Hostel Management is a simple desktop application developed using Python and Tkinter. The purpose of the project is to provide an easy way to manage basic student hostel records through a graphical user interface.

The application focuses on common operations such as adding student details, viewing records, deleting records, clearing input fields, and exiting the application.

---

## 2. Problem Statement

Maintaining student hostel information manually can be inconvenient and difficult to organize as the number of students increases. Important information such as Student ID, student name, course, and room number should be maintained in a structured manner.

This project provides a basic computerized solution that allows hostel records to be entered and managed through a simple GUI.

---

## 3. Objectives

The main objectives of the project are:

- To create a simple hostel management application.
- To provide a graphical user interface using Tkinter.
- To add student hostel records.
- To prevent duplicate Student IDs.
- To display stored student records.
- To delete records using Student ID.
- To apply fundamental Python programming concepts to a practical problem.

---

## 4. Technologies Used

### Programming Language
Python

### GUI Library
Tkinter

### Data Storage
Python list

### Development Concepts

- Functions
- Variables
- Lists
- Loops
- Conditional statements
- Input validation
- Tkinter widgets
- Message boxes

---

## 5. System Features

### Add Student

The user enters Student ID, Student Name, Course, and Room Number. The program checks whether all fields are filled and whether the Student ID already exists. If the details are valid, the record is added.

### Show Students

The application displays all currently stored student records in the output text area.

### Delete Student

The user enters a Student ID. If a matching record is found, it is removed from the list.

### Clear

The Clear button removes all text from the four input fields.

### Exit

The Exit button closes the application window.

---

## 6. Working of the Program

The program begins by creating an empty list named `student_list`.

Each student record is stored in the following format:

```text
[Student ID, Student Name, Course, Room Number]
```

When the Add Student button is pressed, the `add_student()` function reads the values from the input fields. It checks for empty fields and duplicate Student IDs before adding the record.

The `show_students()` function clears the output area and prints every student record stored in the list.

The `delete_student()` function searches the list for the Student ID entered by the user. If the ID is found, the corresponding record is removed.

The `clear_fields()` function clears the input fields using the Tkinter `delete()` method.

Finally, `window.mainloop()` keeps the graphical application running and waits for user actions.

---

## 7. User Interface

The application contains:

1. University heading
2. Project heading
3. Student ID input field
4. Student Name input field
5. Course input field
6. Room Number input field
7. Add Student button
8. Show Students button
9. Delete Student button
10. Clear button
11. Exit button
12. Student record display area

---

## 8. Input Validation

The program checks whether any required field is empty.

If a field is empty, a warning message is displayed:

```text
Please fill all the details
```

Before adding a student, the program also checks all existing records to make sure that the Student ID has not already been used.

If the ID already exists, an error message is displayed.

---

## 9. Advantages

- Simple and easy to use
- Beginner-friendly graphical interface
- Prevents duplicate Student IDs
- Provides basic record management
- Uses standard Python and Tkinter
- Demonstrates important Python programming concepts

---

## 10. Limitations

The application has a few limitations:

- Data is stored only in a Python list.
- Records are lost when the application is closed.
- There is no database connection.
- There is no login or authentication system.
- The application does not currently check whether a room is already occupied.
- There is no facility to edit an existing record.

---

## 11. Future Scope

The project can be improved by adding:

- SQLite or MySQL database integration
- Student search functionality
- Edit/update student records
- Room availability management
- Student check-in and check-out
- Login and authentication
- Export of records to CSV or Excel
- Better GUI design and styling
- Automatic data backup

---

## 12. Conclusion

The VIT Bhopal University Hostel Management project demonstrates how Python and Tkinter can be used to create a simple desktop application for managing student hostel records.

Although the current version is basic and stores data only during the application session, it successfully implements the core operations of adding, displaying, and deleting student records. The project also provides practical experience with Python functions, lists, loops, conditions, input validation, and GUI programming.

---

## 13. Author

**PRAJAL ROYZADA**
