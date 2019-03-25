import datetime

print(datetime.datetime.today())
print(datetime.datetime.today().year)
print(datetime.datetime.today().month)
print(datetime.datetime.today().day)

day = datetime.datetime.today()
day += datetime.timedelta(120)

print(day)