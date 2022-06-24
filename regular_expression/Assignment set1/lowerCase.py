import re


def match(text):
    pattern="^[a-z]+_[a-z]+$"
    x=re.search(pattern,text)
    print(x)
    if x:
        print("Pattern found")
    else:
        print("Pattern not found")
print(match("asdas_das"))
print(match("adfa_AAwfsd"))