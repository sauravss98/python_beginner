import re


def Beginning(text):

    if re.search(r"\AThe",text):
        print("Found")
    else:
        print("Not found")

Beginning("The name is name")
Beginning("Wish it and go")
