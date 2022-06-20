def display(sample):
    with open(sample, 'r') as f:
        a = f.read().split()
        for i in a:
            i = '#'.join(i)
            print(i)


display("sample.txt")
