# VIT Bhopal University Hostel Management

## Project Overview

VIT Bhopal University Hostel Management is a simple desktop-based hostel management application developed in Python using the Tkinter library. The application provides a basic interface for adding, viewing, and deleting student hostel records.

The project is designed as a beginner-friendly Python GUI project and demonstrates the use of functions, lists, loops, conditional statements, Tkinter widgets, and message boxes.

## Features

- Add student hostel records
- Store Student ID, Student Name, Course, and Room Number
- Prevent duplicate Student IDs
- Display all saved student records
- Delete a student using Student ID
- Clear all input fields
- Exit the application
- Show warning, error, and success messages

## Technologies Used

- Python
- Tkinter
- Python lists
- Functions and conditional statements

## How to Run

1. Install Python on the computer.
2. Save the program as a `.py` file.
3. Open a terminal or command prompt in the project folder.
4. Run:

```bash
python filename.py
```

Tkinter is included with most standard Python installations.

## How It Works

The program stores student records in a Python list called `student_list`. Each student is stored as:

```text
[Student ID, Student Name, Course, Room Number]
```

The `add_student()` function validates the input and adds a new record. The `show_students()` function displays the records in the text area. The `delete_student()` function searches for a Student ID and removes the matching record.

## Limitation

The current version stores data only while the application is running. Closing the application clears the records because no database or file storage is used.

## Author

**PRAJAL ROYZADA**
