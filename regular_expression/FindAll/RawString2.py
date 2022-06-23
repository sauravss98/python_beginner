import re
text="The rain in spain"
x=re.findall(r"ain\b",text)
print(x)
if x:
    print("Found")
else:
    print("Not Found")