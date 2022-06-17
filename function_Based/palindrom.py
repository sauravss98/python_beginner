def palin(word):
    a=word[::-1]
    if a==word:
        print("It is palindrome")
    else:
        print("It is not a palindrome")
word=str(input("Enter the word"))
palin(word)