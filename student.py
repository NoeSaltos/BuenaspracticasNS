class student:
    def __init__(self, id, name):
        if id == "" or name == "":
            print("ID and name cannot be empty")
        self.id = id
        self.name = name
        self.gradez = []
        self.isPassed = False
        self.honor = False

    def addGrades(self, g):
        if not isinstance(g, (int, float)):
            print(f"Invalid grade {g}: must be a number")
            return
        if g < 0 or g > 100:
            print(f"Invalid grade {g}: must be between 0 and 100")
            return
        self.gradez.append(g)

    def calcaverage(self):
        if len(self.gradez) == 0:
            return 0
        t = 0
        for x in self.gradez:
            t += x
        avg = t / len(self.gradez)
        return avg

    def checkHonor(self):
        if self.calcaverage() >= 90:
            self.honor = True

    def checkPassFail(self):
        if self.calcaverage() >= 60:
            self.isPassed = True
        else:
            self.isPassed = False

    def deleteGrade(self, index):
        try:
            del self.gradez[index]
            print(f"Deleted grade at index {index}")
        except IndexError:
            print(f"Index {index} out of range")

    def removeGradeByValue(self, value):
        try:
            self.gradez.remove(value)
            print(f"Deleted grade with value {value}")
        except ValueError:
            print(f"Value {value} not found in grades")

    def report(self):
        print("ID: " + str(self.id))
        print("Name: " + self.name)
        print("Grades Count: " + str(len(self.gradez)))
        avg = self.calcaverage()
        print("Average Grade: " + str(avg))
        letter = self.getLetterGrade()
        print("Letter Grade: " + letter)
        self.checkPassFail()
        print("Passed: " + str(self.isPassed))
        self.checkHonor()
        print("Honor Roll: " + str(self.honor))

    def getLetterGrade(self):
        avg = self.calcaverage()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"


def startrun():
    a = student("123", "Diego")
    a.addGrades(100)
    a.addGrades("Fifty")  # Error control - invalid grade
    a.addGrades(85)
    a.calcaverage()
    a.checkHonor()
    a.checkPassFail()
    a.deleteGrade(10)  # IndexError control
    a.removeGradeByValue(50)  # ValueError control
    a.report()


if __name__ == "__main__":
    startrun()