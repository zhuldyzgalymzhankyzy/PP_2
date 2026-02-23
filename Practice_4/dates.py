# dates.py
from datetime import datetime, timedelta

# 1. Today date
def today():
    return datetime.now()


# 2. Add days
def add_days(date_str, days):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return dt + timedelta(days=days)


# 3. Difference in days
def days_between(d1, d2):
    dt1 = datetime.strptime(d1, "%Y-%m-%d")
    dt2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((dt2 - dt1).days)


# 4. Leap year check
def is_leap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
