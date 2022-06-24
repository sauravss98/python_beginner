import re


def number(text):
    pattern="[0-9]{3}|[0-9]{2}|[0-9]{1}"
    x=re.findall(pattern,text)
    print(x)

number("Exercises number 1, 12, 13, and 345 are important")