import re
text="The rain in spain 34123"
x=re.findall("\d",text)
print(x)
if x:
    print("Found")
else:
    print("Not found")