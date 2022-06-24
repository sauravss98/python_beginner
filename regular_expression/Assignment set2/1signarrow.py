from ast import pattern
import re


def arrow(text):
    pattern=">\w"
    x=re.findall(pattern,text)
    print(x)
    if x:
        print("found")
    else:
        print("not found")

arrow(">asd3w dasf >f32")
arrow("as faf wa >2sad ")