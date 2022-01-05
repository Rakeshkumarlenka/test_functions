from datetime import time
class Date_time:
    def date_module(self):
        Time = time(11, 34, 56, 2) #hr,min,sec,mili sec
        print("hour =", Time.hour)
        print("minute =", Time.minute)
        print("second =", Time.second)
        print("microsecond =", Time.microsecond)

res = Date_time()
res.date_module()


