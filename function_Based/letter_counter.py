#9. Write a Python program that accepts a string and calculate the number of digits and letters.
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2

def countWord(word):
    l = len(word)
    alphabet = 0
    numeric = 0
    for i in range(0, l):
        if (word[i].isalpha()):
            alphabet += 1
        elif (word[i].isdigit()):
            numeric += 1
    print("Letters in word: ", alphabet)
    print("Digits in word:", numeric)
word=str(input("Enter the string: "))
countWord(word)
