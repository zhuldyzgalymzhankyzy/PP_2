from datetime import datetime, timedelta
import sys
import re
import calendar

def parse_datetime(line):

    match = re.match(r"(\d{4})-(\d{2})-(\d{2}) UTC([+-])(\d{2}):(\d{2})", line)
    
    year = int(match.group(1))
    month = int(match.group(2))
    day = int(match.group(3))
    sign = match.group(4)
    hours = int(match.group(5))
    minutes = int(match.group(6))
    
    dt = datetime(year, month, day)  
    offset = timedelta(hours=hours, minutes=minutes)
    
    if sign == '+':
        dt -= offset
    else:
        dt += offset
        
    return dt, month, day

def birthday_utc(year, month, day, tz_line):
    if month == 2 and day == 29 and not calendar.isleap(year):
        day = 28
    
    match = re.search(r"UTC([+-])(\d{2}):(\d{2})", tz_line)
    sign = match.group(1)
    hours = int(match.group(2))
    minutes = int(match.group(3))
    
    dt = datetime(year, month, day)
    offset = timedelta(hours=hours, minutes=minutes)
    
    if sign == '+':
        dt -= offset
    else:
        dt += offset
        
    return dt
birth_line = sys.stdin.readline().strip()
current_line = sys.stdin.readline().strip()

birth_dt, birth_month, birth_day = parse_datetime(birth_line)
current_dt, _, _ = parse_datetime(current_line)

current_year = current_dt.year

candidate = birthday_utc(current_year, birth_month, birth_day, birth_line)

if candidate < current_dt:
    candidate = birthday_utc(current_year + 1, birth_month, birth_day, birth_line)

diff_seconds = (candidate - current_dt).total_seconds()

if diff_seconds <= 0:
    print(0)
else:
    print(int(diff_seconds // 86400))