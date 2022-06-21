from datetime import date,timedelta
yr=int(input("Enter the year: "))
mnt=int(input("Enter the month: "))
day=int(input("Enter the date: "))
dte=date(yr,mnt,day)
print("Original date:")
print(dte)
print("Consecutive dates after 20 days for 12 times are given below: ")
for i in range(1,13):
    print(i,".",dte+timedelta(20*i))