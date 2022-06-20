from functools import reduce
k=[1,2,43,4,5,6]
largest=reduce(lambda x,y:x if x>y else y,k)
print(largest)