from operator import le
import re


def letter(text):
    x=re.split("\W",text)
    for i in x:
        l=len(i)
        if l==8:
            print(i)



letter("jnfajns44s assdwdfe asdf kam as ssasdsad")