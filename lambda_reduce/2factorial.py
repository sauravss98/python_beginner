from functools import reduce
num=int(input("Enter the number: "))
a=list()
for i in range(num,0,-1):
    a.append(i)
factorial=reduce(lambda x,y:x*y,a)
print(factorial)