from functools import reduce
a=[1,2,3,4]
add=reduce(lambda x,y:x+y,a)
print(add)
