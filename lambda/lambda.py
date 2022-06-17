from functools import reduce
from itertools import accumulate
a=[2,3,4]
b=map(lambda x:x**2,a)
print(list(b))

c=filter(lambda  x:x%2==0,a)
print(list(c))

print(reduce(lambda x,y:x+y,a))
print(list(accumulate(a,lambda x,y:x+y)))