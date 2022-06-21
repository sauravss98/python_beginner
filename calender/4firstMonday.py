import calendar
count=0
for i in range(1,13):
    firstDay=calendar.monthrange(2015,i)
    if firstDay[0]==0:
        count+=1
print("The number of months starting with monday between 2015 and 2016 is",count)