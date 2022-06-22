class Student:
    def __init__(self):
        self.name=str(input("Enter your name: "))
        self.rollno=int(input("Enter your roll no:"))
        self.marks=int(input("Enter your marks in 100: "))

class Test(Student):
    def check(self):
        if self.marks>50:
            print("You move on to next level")
        else:
            print("You repeat")
class Admin(Test):
    def details(self):
        print("These are the student info")
        print("Name : ",self.name)
        print("Roll no: ",self.rollno)
        print("Marks: ",self.marks)

obj= Admin()
obj.details()
obj.check()