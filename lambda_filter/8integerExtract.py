str1="Winter Olympics in 2022 will take place in Beijing China"
a=len(str1)
# extract=filter(lambda x:(x[i]=='0' or x[i]=='1' or x[i]=='2' or x[i]=='3' or x[i]=='4' or x[i]=='5'or x[i]=='6' or x[i]=='7' or x[i]=='8' or x[i]=='9'), str1)
# for i in range(0,a):
#     print(list(extract))
extract=filter(lambda x:True if x in "0123456789" else False,str1)
print(list(extract))