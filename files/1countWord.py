def count(sample):
    with open(sample,'r') as FileObject:
        a = 0
        b=FileObject.read().split()
        for i in b:
            a=a+1
        print(a)
    return ''
print(count("sample.txt"))
