def Armstrong(a,b):
    for i in range(a,b):
        num = i
        sum = 0
        count = 0
        while num > 0:
            rem = num % 10
            sum += rem**3
            num = num // 10
            count += 1
        if sum == i:
            print(i)
    return ''

a,b=100,600
print(Armstrong(a,b))
