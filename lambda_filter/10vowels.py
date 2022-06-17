str1="Winter Alympics in 2022 will take place in Beijing China"
str1=str1.lower()
print(str1)
vowel=filter(lambda x:True if x in "aeiou" else False,str1)
print("These are the vowels",list(vowel))
consonents=filter(lambda x:False if x in "aeiou" else True,str1)
print("These are the consonents", list(consonents))