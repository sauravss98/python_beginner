def countT(sample):
    with open(sample,'r') as f:
        a=f.read().split()
        count=0
        for i in a:
            if i[0]!='T':
                count+=1
        print(count)
countT("sample.txt")