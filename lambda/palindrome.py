pal=lambda word:word==word[::-1]
word=str(input("Enter the string to be checked"))
print(pal(word))