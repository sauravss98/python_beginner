#5. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
def multiple(num):
    three=0
    five=0
    sum=0
    for i in range(0,num+1):
        if(i%3==0):
            three+=i
        elif(i%5==0):
            five+=i
    sum=three+five
    return sum

num=int(input("Enter the number of terms: "))
print("The sum is ",multiple(num))