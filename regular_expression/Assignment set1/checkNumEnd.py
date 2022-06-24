import re


def checkNum(text):
    pattern="[0-9]$"
    if re.search(pattern,text):
        print("Found")
    else:
        print("Not Found")


checkNum("asdfaed3")
checkNum("34 dfafdar  34f")