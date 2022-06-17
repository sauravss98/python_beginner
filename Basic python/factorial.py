
number=int(input("Enter the number: "))
factorial=1
n=number
while(n!=0):
    factorial=factorial*n
    n=n-1
print("The factorial of ",number," is ", factorial)