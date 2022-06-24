import re


def date(text):
    pattern=r"(\d{4})-(\d{2})-(\d{2})"
    print(pattern)
    x=re.sub(pattern,r"\3-\2-\1",text)
    print(x)


date("2022-04-22")