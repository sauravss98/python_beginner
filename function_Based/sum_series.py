#12. Find the sum of the following sequence : 2+22+ 222+2222+ ……… to n terms

def sum(number):
    n = 2
    sum = 2
    count = 1
    while (count < number):
        n = (n * 10) + 2
        sum = sum + n
        count += 1
    return sum
number=int(input("Enter the number of terms"))
print("Sum of ", number, " terms:", sum(number))
