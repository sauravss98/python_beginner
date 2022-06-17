number=int(input("Enter the number of terms: "))
n=2
sum=2
count=1
while(count<number):
   n=(n*10)+2
   sum=sum+n
   count+=1
print("The sum of ",number," terms is: ",sum)