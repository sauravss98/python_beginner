t=(1, 2, 3)
#print(t)

# SET
a={"apple", "orange", "banana", "cherry", "coconut"}
a.add("mango")
a.update(["pineapple", "grapes", "lemon"])
#print(a)
b = {"apple", "orange", "banana", "strawberry", "pineapple", "coconut"}
#print(b)
'''x=a.union(b)
print(x)
y=b.union(a)
print(y)'''
x=a.intersection(b)
y=b.intersection(a)
#print(x)
#print(y)
z=a.difference(b)
#print(z)
c=b.difference(a)
#print(c)

# Dictionary

d = {"Brand": "Ford", "Model": "Ecosport", "Color": "Black"}
print(d)
p = d["Model"]
print(p)
q=d.get("Brand")
print(q)
d["Color"]="Silver"
print(d)
d.update({"Trim": "GTX+", "Year": "2020"})
print(d)
x=d.items()
print(x)
y=d.keys()
print(y)
z=d.values()
print(z)

i = ["Item1", "Item2"]
j = ["One", "Two"]
k=dict.fromkeys(i,j)
print(k)
r=zip(i,j)
s=zip(i,j)
t=zip(i,j)
#print(r)
print(dict(r))
print(list(s))
print(tuple(t))
