from datetime import date
class Date_time:
    def date_module(self):
        today = date.today()
        # Converting the date to the string
        Str = date.isoformat(today)
        print("String Representation", Str)
        print(type(Str))

res = Date_time()
res.date_module()
