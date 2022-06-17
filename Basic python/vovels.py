word=str(input("Enter the word to be checked: "))
vowels=0
consonents=0
lenght=len(word)
for i in range(0,lenght):
    if(word[i]=='a' or word[i]=='A' or word[i]=='e' or word[i]=='E' or word[i]=='i' or word[i]=='I' or word[i]=='o' or word[i]=='O' or word[i]=='u' or word[i]=='U'):
        vowels+=1
    else:
        consonents+=1
print("The number or vowels: ",vowels)
print("The number of consonents: ",consonents)