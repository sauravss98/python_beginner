import re
text="The rain in spain"
x=re.findall("\AThe",text)
print(x)
if x:
    print("There is a match")
else:
    print("There is not match")