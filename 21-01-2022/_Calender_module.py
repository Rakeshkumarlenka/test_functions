import calendar

print("===================================================================================")
## display the november month calendar
yy = 2022
mm = 11
print(calendar.month(yy, mm))

print("===================================================================================")


# display the full calendar
yy = 2022
print(calendar.calendar(yy))

print("===================================================================================")
# Python code to demonstrate the working of
# isleap() and leapdays()
# using isleap() to check if year is leap or not
if (calendar.isleap(2022)):
    print("The year is leap")
else:
    print("The year is not leap")

# using leapdays() to print leap days between years
print("The leap days between 1950 and 2022 are : ", end="")
print(calendar.leapdays(1950, 2022))

print("===================================================================================")

