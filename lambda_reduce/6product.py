from functools import reduce
my_numbers = [4, 6, 9, 23, 5]
product=reduce(lambda x,y:x*y,my_numbers)
print(product)