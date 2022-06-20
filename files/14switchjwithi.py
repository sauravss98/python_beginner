def replace(sample):
    with open(sample,'r') as f:
        a=f.read().split()
        for i in a:
            length=len(i)
            for j in range(0,length):
                if i[j]!='i':
                    print(i[j])
                elif i[j]=='i':
                    b=i[j].replace('i','j')
                    print(b)




replace("sample.txt")