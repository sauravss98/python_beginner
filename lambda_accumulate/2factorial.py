from itertools import accumulate
num=int(input("Enter the number: "))
a=list()
for i in range(num,0,-1):
    a.append(i)
factorial=list(accumulate(a,lambda x,y:x*y))
print(factorial)