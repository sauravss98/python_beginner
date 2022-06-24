import re


def Colon(text):
    pattern="[,. ]"
    x=re.sub(pattern,":",text)
    print(x)

Colon("My name is ,name and i am 13.")