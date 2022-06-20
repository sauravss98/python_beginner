def copyFile(sample,test):
    with open(test,'r') as f:
        b=f.read()
    with open(sample,'a') as d:
        d.writelines(b)
copyFile("sample.txt","test.txt")