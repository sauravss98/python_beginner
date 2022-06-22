class Input:
    def __init__(self):
        self.num1=int(input("Enter the first number"))
        self.num2=int(input("Enter the second number"))
        self.num3=int(input("Enter the third number"))
class Calculation(Input):
    def largest(self):
        if self.num1> self.num2 and self.num1>self.num3:
            print("Largest number is",self.num1)
        elif self.num2> self.num3:
            print("Largest number is",self.num2)
        else:
            print("Largest number is", self.num3)
obj=Calculation()
obj.largest()