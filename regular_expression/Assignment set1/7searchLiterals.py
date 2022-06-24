import re


def search(text):
    pattern=str(input("Enter the word to be searched"))
    x=re.findall(pattern,text)
    if x:
        print("Found")
    else:
        print("Not Found")

search("he quick brown fox jumps over the lazy dog")
