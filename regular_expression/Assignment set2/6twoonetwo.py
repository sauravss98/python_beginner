from operator import le
import re


def two(text):
    pattern=r"212\S+"
    x=re.findall(pattern,text)
    print(x)

two("jnfajnss assdwdfe asdf kam as 212sdsad")