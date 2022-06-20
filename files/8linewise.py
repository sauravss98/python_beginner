def lineWise(test,n):
    with open(test,'w') as f:
        x=''
        for i in range(65,91):
            a=chr(i)
            x+=a
        for i in range(0,26,n):
            f.writelines(x[i:i+n]+ '\n')



n=int(input("Enter number: "))
lineWise("test.txt",n)