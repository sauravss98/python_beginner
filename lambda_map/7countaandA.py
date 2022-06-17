lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
cnt=map(lambda x:x.lower().count("a"),lst1)
print(list(cnt))