import calendar,datetime
print(calendar.month(1998,4,2,1))
t=datetime.datetime.now()
print(t)
print(t.strftime("%B"))
print(t.strftime("%I : %M %p"))
print(calendar.calendar(1998,1,1,1))
calendar.prmonth(1998,4)
print(calendar.isleap(2019))
print(calendar.weekheader(3))
print(calendar.monthcalendar(1998,4))
c=calendar.Calendar()
for i in c.itermonthdays(1998,4):
    print(i,end=" ")
print("\n")
for i in c.itermonthdays3(1998,4):
    print(i,end=" ")