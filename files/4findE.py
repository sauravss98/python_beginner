def counte(sample):
    with open(sample,'r') as f:
        count=0
        word=f.read().split()
        for i in word:
            length=len(i)
            if i[length-1]=='e':
                count+=1
        print(count)
    return ''
counte("sample.txt")