word=str(input("Enter the word"))
b=dict()
for i in word:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)