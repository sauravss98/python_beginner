n=["amma","anna","aleena","agi"]
palindrome=filter(lambda x:x==x[::-1],n)
print(list(palindrome))