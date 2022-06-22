import datetime
wk=datetime.date.today()
year,week_num,day_of_week=wk.isocalendar()
print("Year %d, Week Number %d, Day of the Week %d" %(year,week_num, day_of_week))