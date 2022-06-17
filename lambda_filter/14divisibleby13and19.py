nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
divisible=filter(lambda x: True if (x%13==0 or x%19==0) else False,nums)
print(list(divisible))