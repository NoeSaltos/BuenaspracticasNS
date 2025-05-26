"""
Module for managing students and their grades with functions such as
addition and average calculation, and reporting.
"""


class Student:
    """Class that represents a student and manages their grades."""

    def __init__(self, student_id, name):
        """Initialize a student with an ID, name, and empty grade list."""
        if student_id == "" or name == "":
            print("ID and name cannot be empty")
        self.student_id = student_id
        self.name = name
        self.gradez = []
        self.is_passed = False
        self.honor = False

    def add_grades(self, g):
        """Add a valid grade (0-100) to the student's grades."""
        if not isinstance(g, (int, float)):
            print(f"Invalid grade {g}: must be a number")
            return
        if g < 0 or g > 100:
            print(f"Invalid grade {g}: must be between 0 and 100")
            return
        self.gradez.append(g)

    def calc_average(self):
        """Calculate and return the average of the student's grades."""
        if len(self.gradez) == 0:
            return 0
        t = 0
        for x in self.gradez:
            t += x
        avg = t / len(self.gradez)
        return avg

    def check_honor(self):
        """Set honor flag to True if average grade is 90 or above."""
        if self.calc_average() >= 90:
            self.honor = True

    def check_pass_fail(self):
        """Set is_passed flag to True if average grade is 60 or above."""
        if self.calc_average() >= 60:
            self.is_passed = True
        else:
            self.is_passed = False

    def delete_grade(self, index):
        """Delete a grade by its index; handle out-of-range errors."""
        try:
            del self.gradez[index]
            print(f"Deleted grade at index {index}")
        except IndexError:
            print(f"Index {index} out of range")

    def remove_grade_by_value(self, value):
        """Delete a grade by its value; handle value-not-found errors."""
        try:
            self.gradez.remove(value)
            print(f"Deleted grade with value {value}")
        except ValueError:
            print(f"Value {value} not found in grades")

    def report(self):
        """Print a summary report of the student's grades and status."""
        print("ID: " + str(self.student_id))
        print("Name: " + self.name)
        print("Grades Count: " + str(len(self.gradez)))
        avg = self.calc_average()
        print("Average Grade: " + str(avg))
        letter = self.get_letter_grade()
        print("Letter Grade: " + letter)
        self.check_pass_fail()
        print("Passed: " + str(self.is_passed))
        self.check_honor()
        print("Honor Roll: " + str(self.honor))

    def get_letter_grade(self):
        """Return the letter grade corresponding to the average grade."""
        avg = self.calc_average()
        if avg >= 90:
            return "A"
        if avg >= 80:
            return "B"
        if avg >= 70:
            return "C"
        if avg >= 60:
            return "D"
        return "F"


def startrun():
    """Function to demonstrate the Student class functionality."""
    a = Student("123", "Diego")
    a.add_grades(100)
    a.add_grades("Fifty")  # Error control - invalid grade
    a.add_grades(85)
    a.calc_average()
    a.check_honor()
    a.check_pass_fail()
    a.delete_grade(10)  # IndexError control
    a.remove_grade_by_value(50)  # ValueError control
    a.report()


if __name__ == "__main__":
    startrun()
