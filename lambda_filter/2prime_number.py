num=int(input("Enter the number of terms"))
prime_check=filter(lambda x:x%prime_check(x+1),num)
print(list(prime_check))