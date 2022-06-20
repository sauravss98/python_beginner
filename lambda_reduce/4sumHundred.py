from functools import reduce
n=100
a=list()
for i in range(0,100):
    a.append(i)
hundredSum=reduce(lambda x,y:x+y,a)
print(hundredSum)
