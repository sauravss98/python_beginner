# 10. Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.
def prime(num):
    for i in range(0,num):
        if i>1:
            for j in range(2,i):
                if((i%j)==0):
                    break
            else:
                print(i)
num=int(input("Enter the number: "))
prime(num)