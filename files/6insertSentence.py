def insert(sample):
    with open(sample,'r') as f:
        a=f.readlines()
        b=list(a)
        b.insert(2,"This was made using python\n")
    with open(sample,'w') as c:
        c.writelines(b)
    return ''
print(insert("sample.txt"))
