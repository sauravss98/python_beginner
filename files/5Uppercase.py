def uppperCase(sample):
    with open(sample,'r') as f:
        count=0
        word=f.read().split()
        for i in word:
            length=len(i)
            for j in range(0,length):
                if i[j].isupper():
                    count+=1
        print(count)
    return ''
uppperCase("sample.txt")