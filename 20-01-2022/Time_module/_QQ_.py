#P5 : Find current date and time
from datetime import *

import dateutil.tz

now = datetime.now()
print(now)

print('Date now : {}/{}/{}'.format(now.day, now.month, now.year))
print('Time now : {}/{}/{}'.format(now.hour, now.minute, now.second))


#P6 : Todays date and time
tdm = datetime.today()
print("Todays date and time = ", tdm)
td = date.today()
print("Todays date = ", td)

#P7 : Combining date and time

d = date(2022, 1, 19)
t = time(15 ,2)
dt = datetime.combine(d, t)
print(dt)

#P8 : Create a date time objects and then changes its content

dt1 = datetime(year=2022, month=1, day=19, hour=15, minute=7, second=33)
print(dt1)

dt2 = dt1.replace(hour=17, year=2020)
print(dt2)

#P9 : Convert date in a formate
td1 = date.today()
print(td1)

str = td.strftime("%d, %B, %Y")
print(str)

#P10 : Program to find the day of the year and the week day name
td = date.today()
print(td)

s = td.strftime("%j")   # %j day of the year as zero padded decimal no
print('Today is ', s, 'th day of the year')

s1 = td.strftime("%A")  # %A Weekdays as full name
print('it is ',s1)