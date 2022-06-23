import re
text="The rain in spain"
x=re.findall("ain\Z",text)
print(x)
if x:
    print("Found")
else:
    print("Not Found")