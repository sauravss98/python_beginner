import calendar
yr=int(input("Enter the year: "))
mnt=int(input("Enter the month in number: "))
if mnt==12:
    yr+=1
    mnt=0

ans=calendar.monthrange(yr,mnt+1)
print(ans)
if ans[0]==0:
    Day=6
else:
    Day=ans[0]-1
print(Day)
if Day==0:
    print("Monday")
elif Day==1:
    print("Tuesday")
elif Day==2:
    print("Wednesday")
elif Day==3:
    print("Thursday")
elif Day==4:
    print("Friday")
elif Day==5:
    print("Saturday")
elif Day==6:
    print("Sunday")