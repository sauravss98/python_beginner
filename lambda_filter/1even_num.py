ls=[1,2,3,4]
print("Original List: ",ls)
print("List after removing even numbers")
result=filter(lambda x:x%2==0,ls)
print(list(result))