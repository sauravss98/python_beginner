from itertools import accumulate
a = ["java", "anna", "amma", "maths","malayalam","radar"]
palidrome=list(accumulate(a,lambda x,y:y==y[::-1]))
print(palidrome)