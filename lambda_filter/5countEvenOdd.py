a=[1,2,3,4,5,6,7,8,9]
countEven=0
countOdd=0
evod=filter(lambda x:x%2==0,a)
countEven=len(list(evod))
print("Even numbers: ",countEven)
countOdd=len(a)-countEven
print("Odd numbers: ",countOdd)