import datetime as dt

class DateUtils():
    def filtered_date_format_to_correct_format(self, now):
        now_date = dt.datetime.strftime(now, "%Y-%m-%d")
        
        return now_date
