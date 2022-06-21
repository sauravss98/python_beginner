import calendar
yr=int(input("Enter the year: "))
mnt=int(input("Enter the month in number: "))

ans=calendar.monthrange(yr,mnt)
print("The number of days in this month is",ans[1])