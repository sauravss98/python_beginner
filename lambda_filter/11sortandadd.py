lst1=[1000, 500, 600, 700, 5000, 90000, 17500]
number=list(map(lambda x:x+2000,filter(lambda x:x<8000,lst1)))
print(number)