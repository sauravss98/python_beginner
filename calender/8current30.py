from datetime import date,timedelta
dte=date.today()
print("Current date:")
print(dte)
print("Date after 30 days of the current date:")
print(dte+timedelta(30))
print("Date before 30 days of the current date")
print(dte-timedelta(30))