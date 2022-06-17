word=str(input("Enter the word to be checked: "))
b=word

vowels="aeiouAEIOU"
for i in word:
    if i in vowels:
        b=b.replace(i," ")
print(b)



print("The number or vowels: ",word)

