class Main:
    def __init__(self):
        self.num=int(input("Enter the number: "))
class Prime(Main):
    def pr(self):
        i=2
        flag=0
        while i<=self.num/2:
            if self.num%i==0:
                flag=1
                break
            i+=1

        if flag==0:
            print(self.num,"is prime")
        else:
            print(self.num,"is not prime")

obj=Prime()
obj.pr()