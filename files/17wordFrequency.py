def frequency(sample):
    with open(sample,'r') as f:
        word=dict()
        a=f.read().split()
        for i in a:
            if i in word:
                word[i]+=1
            else:
                word[i]=1
    print(word)
frequency("sample.txt")