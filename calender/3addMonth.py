from datetime import date,timedelta
yr=int(input("Enter the year: "))
mnt=int(input("Enter the month: "))
day=int(input("Enter the date: "))
dte=date(yr,mnt,day)
print(dte)
print("Date after adding one month to the specified date is: ")
print(dte+timedelta(30))