import re


def fndZ(text):
    pattern="[z]"
    if re.search(pattern,text):
        print("Found")
    else:
        print("Not found")

fndZ("ASFDASzafasfw")
fndZ("asdfawfasfas")
fndZ("afafwzZfaewz")