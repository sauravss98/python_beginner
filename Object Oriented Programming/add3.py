class Input:
    def  __init__(self):
        self.num1=int(input("Enter the first number: "))
        self.num2=int(input("Enter the second number: "))
        self.num3=int(input("Enter the third number: "))

class Sum(Input):
    def add(self):
        self.sum=self.num1+self.num2+self.num3
    def display(self):
        print("The sum of ",self.num1,"+",self.num2,"+",self.num3,"=",self.sum)
obj=Sum()
obj.add()
obj.display()