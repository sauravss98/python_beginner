from operator import le
import re


def letter(text):
    pattern=r"\w{8}"
    x=re.findall(pattern,text)
    print(x)

letter("jnfajnss assdwdfe asdf kam as ssasdsad")