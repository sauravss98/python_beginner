class Input:
    def __init__(self):
        self.num=int(input("Enter the number:"))
        self.rev=0
class Steps(Input):
    def reverse(self):
        while self.num>0:
            r=self.num%10
            self.rev=self.rev*10+r
            self.num=int(self.num/10)
class Result(Steps):
    def answer(self):
        print("The number after reversing is ",self.rev)
obj=Result()
obj.reverse()
obj.answer()