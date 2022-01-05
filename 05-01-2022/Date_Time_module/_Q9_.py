from datetime import datetime, timedelta
class Date_time:
    def date_module(self):
        ini_time_for_now = datetime.now()

        # printing initial_date
        print("initial_date", str(ini_time_for_now))
        future_date_after_2yrs = ini_time_for_now + timedelta(days=730)
        future_date_after_2days = ini_time_for_now + timedelta(days=2)

        # printing calculated future_dates
        print('future_date_after_2yrs:', str(future_date_after_2yrs))
        print('future_date_after_2days:', str(future_date_after_2days))

res = Date_time()
res.date_module()

