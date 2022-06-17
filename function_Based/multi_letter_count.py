# 8. Write a function called multipleLetterCount. This function takes in one parameter (a string) and returns a dictionary with the keys being the letters and the value being the count of the letter.
#  Example output:
# multipleLetterCount('awesome')
#  {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
def multipleLetterCount(word):
    a=dict()
    for i in word:
        if i in a:
            a[i]+=1
        else:
            a[i]=1
    print(a)
word=str(input("Enter the word: "))
multipleLetterCount(word)