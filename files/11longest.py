from functools import reduce


def longest(sample):
    with open(sample, 'r') as f:
        a = f.read().split()
        red = reduce(lambda x, y: x if len(x) > len(y) else y, a)
    print(red)


longest("sample.txt")
