class Number:
    def __init__(self):
        self.a=int(input("Enter the first numebr: "))
        self.b=int(input("Enter the second number: "))
class Add(Number):
    def sum(self):
        self.s=self.a+self.b
        print("Sum= ",self.s)
class Substract(Number):
    def sub(self):
        self.s=self.a-self.b
        print("Substracted value = ",self.s)
class Multiply(Number):
    def mul(self):
        self.s=self.a*self.b
        print("Multiplied number= ",self.s)
obj1=Add()
obj1.sum()
obj2=Substract()
obj2.sub()
obj3=Multiply()
obj3.mul()