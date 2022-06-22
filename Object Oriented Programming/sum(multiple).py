class Number1:
    def input1(self):
        self.num1=int(input("Enter the first number: "))
class Number2:
    def input2(self):
        self.num2=int(input("Enter the second number: "))
class Add(Number1,Number2):
    def sum(self):
        super().input1()
        super().input2()
        self.s=self.num1+self.num2
        print("Sum = ",self.s)
obj=Add()
obj.sum()