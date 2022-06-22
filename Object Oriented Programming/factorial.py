class Input:
    def __init__(self):
        self.num=int(input("Enter the number: "))
        self.f=1
class Step(Input):
    def fact(self):
        for i in range(1,self.num+1):
            self.f=self.f*i
class Answer(Step):
    def answer(self):
        print("The factorial of",self.num,"is",self.f)

obj=Answer()
obj.fact()
obj.answer()