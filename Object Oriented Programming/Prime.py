class prime:
    def __init__(self,num):
        self.num=num

    def check(self):
        flag=0
        if self.num<2:
            flag =1
        else:
            for i in range(2,self.num):
                if self.num%i==0:
                    flag=1

        if flag==0:
            print("The number is prime")
        else:
            print("The number is not prime")
num=int(input("Enter the number to be checked: "))
obj=prime(num)
obj.check()