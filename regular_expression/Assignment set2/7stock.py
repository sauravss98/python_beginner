import re


def stock(text):
    pattern=r"\b[A-Z]+:\d.+"
    x=re.findall(pattern,text)
    print(x)

stock("Some of the prices were as following TSLA:423.4,ORCL:2532,GE:342.43,MSFT:324,BIDU:213.As the macroeconomic developments continue we will update the prices")
