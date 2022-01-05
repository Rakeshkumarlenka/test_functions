from datetime import date
class Date_time:
    def date_module(self):
        # date object of today's date
        today = date.today()
        print("Current year:", today.year)
        print("Current month:", today.month)
        print("Current day:", today.day)

res = Date_time()
res.date_module()
