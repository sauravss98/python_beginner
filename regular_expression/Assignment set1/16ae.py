import re


def find(text):
    pattern="[ae]\w+"
    x=re.findall(pattern,text)
    print(x)

find("asdw ae asede e af  grfd")
find("easd  asd asd grg dfgrew fv")