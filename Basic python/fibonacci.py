number=int(input("Enter the number: "))
number1=0
number2=1
print("The fibonacci numbers for ",number," elements are")
print(number1)
print(number2)
for i in range(2,number):
    sum=number1+number2
    print(sum)
    number1=number2
    number2=sum
