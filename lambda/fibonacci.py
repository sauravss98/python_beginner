num=int(input("Enter the number of terms: "))
fib=lambda x:x if x<2 else fib(x-1)+fib(x-2)
for i in range(0,num):
    print(fib(i))