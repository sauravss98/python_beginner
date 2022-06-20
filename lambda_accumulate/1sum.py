from itertools import accumulate
arr=[1,2,3,4,5,6,7]
sum=list(accumulate(arr,lambda x,y:x+y))
print(sum)