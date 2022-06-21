def replace(sample):
    with open(sample, 'r') as f:
        a = f.read()
        for i in a:
            if i=='j':
                print('i',end='')
            else:
                print(i,end='')
    return ''





replace("sample.txt")
