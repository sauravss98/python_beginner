import re
text="The rain in spain 34123"
x=re.findall("\w",text)
print(x)
if x:
    print("Found")
else:
    print("Not found")