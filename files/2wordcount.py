def lessThanFour(sample):
    with open(sample,'r') as f:
        word=f.read().split()
        for i in word:
            a=len(i)
            if a<4:
                print(i)
    return ''
lessThanFour("sample.txt")