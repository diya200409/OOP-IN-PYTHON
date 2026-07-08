class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        if self.marks >= 90:
            grade = "A+"
        elif self.marks >= 80:
            grade = "A"
        elif self.marks >= 70:
            grade = "B"
        elif self.marks >= 60:
            grade = "C"
        elif self.marks >= 50:
            grade = "D"
        else:
            grade = "F"

        print("Name :", self.name)
        print("Marks:", self.marks)
        print("Grade:", grade)


s1 = Student("Rahul", 95)
s1.display()