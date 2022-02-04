#Difference Between Two Points in Time Using timedelata
from datetime import timedelta
class Date_time:
    def date_module(self):
        t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
        t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
        t3 = t1 - t2
        print("t3 =", t3)

res = Date_time()
res.date_module()



