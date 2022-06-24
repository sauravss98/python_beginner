import re


def match(text):
        x=re.findall(r"\bP+\w+ +\bP+\w+",text)
        print(x)
match("Peter Pan,afe af")