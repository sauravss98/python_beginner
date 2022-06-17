nums = [2, 4, -6, -9, 11, -12, 14, -5, 17,21]
pos=filter(lambda x:x>0,nums)
neg=filter(lambda x:x<0,nums)
posn=list(pos)
negn=list(neg)
plen=len(posn)
nlen=len(negn)
spos=0
for i in range(0,plen):
    spos+=posn[i]
print("Sum of positive number: ",spos)
sneg=0
for i in range(0,nlen):
    sneg+=negn[i]
print("Sum of negative number: ",sneg)
