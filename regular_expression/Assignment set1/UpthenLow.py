import re


def checkCase(text):
    pattern="[A-Z]+[a-z]"
    if re.search(pattern,text):
        print("Match found")
    else:
        print("Match not found")

checkCase("Hello")
checkCase("safaaf3wfas")
checkCase("AFWsada")