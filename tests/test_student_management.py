import contextlib
import io
import unittest
from unittest.mock import patch

import student_management


class StudentManagementTests(unittest.TestCase):
    def setUp(self):
        student_management.students.clear()

    def test_add_student(self):
        with patch("builtins.input", side_effect=["Ada", "A1", "95"]):
            with contextlib.redirect_stdout(io.StringIO()):
                student_management.add_student()

        self.assertEqual(len(student_management.students), 1)
        self.assertEqual(student_management.students[0].name, "Ada")
        self.assertEqual(student_management.students[0].roll_no, "A1")
        self.assertEqual(student_management.students[0].marks, 95)

    def test_reject_duplicate_roll_number(self):
        student_management.students.append(
            student_management.Student(name="Ada", roll_no="A1", marks=95)
        )

        with patch("builtins.input", side_effect=["Grace", "A1"]):
            with contextlib.redirect_stdout(io.StringIO()):
                student_management.add_student()

        self.assertEqual(len(student_management.students), 1)

    def test_find_student_returns_none_when_not_found(self):
        self.assertIsNone(student_management.find_student("missing"))

    def test_read_marks_rejects_out_of_range_value(self):
        with patch("builtins.input", return_value="101"):
            with contextlib.redirect_stdout(io.StringIO()):
                result = student_management.read_marks()

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
