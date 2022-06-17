number=int(input("Enter the number to be checked: "))
flag=0
if(number==0 or number==1):
    flag=2
for i in range(2,(int)(number/2)):
    if(number%i==0):
        flag=1
        break
if(flag==0):
    print(number," is a prime number")
elif(flag==1):
    print(number," is not a prime number")
else:
    print(number," is neither a prime or composite number")