prime=int(input("Enter the number to be checked: "))
check_prime=lambda a:all(a%i!=0 for i in range(2,prime))
print(check_prime(prime))
