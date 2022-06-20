def countThe(sample):
    with open(sample,'r') as fileObject:
        count=0
        word=fileObject.read().split()
        for i in word:
            if i=="the" or i=="The":
                count+=1
        print(count)
    return ''
countThe("sample.txt")