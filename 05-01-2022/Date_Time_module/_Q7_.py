from datetime import time
class Date_time:
    def date_module(self):
        Time = time(12, 24, 36, 1212)
        Str = Time.isoformat()
        print("String Representation:", Str)
        print(type(Str))

res = Date_time()
res.date_module()

