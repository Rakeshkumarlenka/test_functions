from datetime import date
class Date_time:
    def date_module(self):
        # format year, month, date
        my_date = date(1996, 12, 11)
        # my_date = date(1996, 12, 39)  #ValueError as it is outside range
        # my_date = date('1996', 12, 11)  #TypeError as a string is passed instead of integer

        print("Date passed as argument is", my_date)

res = Date_time()
res.date_module()



