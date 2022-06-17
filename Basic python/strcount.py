word=str(input("Enter the string: "))
l=len(word)
alphabet=0
numeric=0
for i in range(0,l):
    if(word[i].isalpha()):
        alphabet+=1
    elif(word[i].isdigit()):
        numeric+=1
print("Letters in word: ",alphabet)
print("Numbers in word:",numeric)