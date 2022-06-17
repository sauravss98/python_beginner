word=str(input("Enter the string to be checked: "))
start=0
end=len(word)-1
flag=0
while(start<end):
        if(word[start]==word[end]):
                flag=0
        else:
                flag=1
        start+=1
        end-=1
if(flag==0):
        print("It is a palindrome")
else:
        print("It is not a palindrome")



n=str(input("enter the string"))
a=n[::-1]
if a==n:
        print("pallindrome")
else:
        print("not pallindrome")