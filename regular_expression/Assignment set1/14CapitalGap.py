import re


def func(text):
    x=re.sub(r"(\w)([A-Z])",(r"\1 \2"),text)
    print(x)
func("HelloWorld")
func("anhfnajn XkafkaBdefa")