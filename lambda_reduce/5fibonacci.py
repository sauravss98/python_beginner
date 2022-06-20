from functools import reduce
num=int(input("Enter the number of terms: "))
a=list()
fib=lambda x:x if x<2 else fib(x-1)+fib(x-2)
for i in range(0,num):
    a.append(fib(i))
print(a)
sum=reduce(lambda x,y:x+y,a)
print("The sum of all fibonacci numbers: ",sum)