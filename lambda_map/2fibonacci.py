num=int(input("enter the number of terms for fibonacci: "))
fib=lambda x:x if x<2 else fib(x-1)+fib(x-2)
print(list(map(fib,range(0,num))))
