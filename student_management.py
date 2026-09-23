"""A small command-line student management application.

The application stores records in memory and demonstrates input validation,
functions, type hints, and a simple menu-driven interface.
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Student:
    """Represent one student record."""

    name: str
    roll_no: str
    marks: float


students: List[Student] = []


def find_student(roll_no: str) -> Optional[Student]:
    """Return a student by roll number, or None if not found."""
    return next((student for student in students if student.roll_no == roll_no), None)


def read_marks() -> Optional[float]:
    """Read marks between 0 and 100 from the user."""
    value = input("Enter marks (0-100): ").strip()
    try:
        marks = float(value)
    except ValueError:
        print("Marks must be a valid number.")
        return None

    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
        return None
    return marks


def add_student() -> None:
    """Validate and add a student record."""
    name = input("Enter student name: ").strip()
    roll_no = input("Enter roll number: ").strip()

    if not name or not roll_no:
        print("Name and roll number cannot be empty.")
        return
    if find_student(roll_no) is not None:
        print(f"A student with roll number '{roll_no}' already exists.")
        return

    marks = read_marks()
    if marks is None:
        return

    students.append(Student(name=name, roll_no=roll_no, marks=marks))
    print(f"Student '{name}' added successfully!")


def view_students() -> None:
    """Display all students in a readable table."""
    if not students:
        print("No students found.")
        return

    print("\nStudent List")
    print("-" * 48)
    print(f"{'Name':<20} {'Roll No':<12} {'Marks':>8}")
    print("-" * 48)
    for student in students:
        print(f"{student.name:<20} {student.roll_no:<12} {student.marks:>8.2f}")


def search_student() -> None:
    """Find and display a student by roll number."""
    roll_no = input("Enter roll number to search: ").strip()
    student = find_student(roll_no)
    if student is None:
        print("Student not found.")
        return

    print(f"Name: {student.name}")
    print(f"Roll No: {student.roll_no}")
    print(f"Marks: {student.marks:.2f}")


def delete_student() -> None:
    """Delete a student by roll number."""
    roll_no = input("Enter roll number to delete: ").strip()
    student = find_student(roll_no)
    if student is None:
        print("Student not found.")
        return

    students.remove(student)
    print(f"Student '{student.name}' deleted successfully!")


def main() -> None:
    """Run the interactive menu."""
    actions = {
        "1": add_student,
        "2": view_students,
        "3": search_student,
        "4": delete_student,
    }

    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()
        if choice == "5":
            print("Exiting program. Goodbye!")
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Please enter a number from 1 to 5.")
        else:
            action()


if __name__ == "__main__":
    main()
