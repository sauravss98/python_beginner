class Employee:
    def input1(self):
        self.id=int(input("Enter your id: "))
class Details:
    def input2(self):
        self.name=str(input("Enter your name: "))
        self.sal=int(input("Enter your salary: "))
class Info(Employee,Details):
    def display(self):
        super().input1()
        super().input2()
        print("Employee id: ",self.id)
        print("Employee name: ",self.name)
        print("Salary: ",self.sal)
obj=Info()
obj.display()