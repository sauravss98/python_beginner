num=int(input("enter the number of terms for fibonacci: "))
fib=map(lambda x:1 if x==1 else fib(x-1)+fib(x-2),num)
print(list(fib))
