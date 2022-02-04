from datetime import datetime
class Date_time:
    def date_module(self):
        # Getting Datetime from timestamp
        date_time = datetime.fromtimestamp(1887639468)
        print("Datetime from timestamp:", date_time)


res = Date_time()
res.date_module()
