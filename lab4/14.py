from datetime import datetime, timedelta
import sys
import re

def parse_datetime(line):
    match = re.match(r"(\d{4}-\d{2}-\d{2}) UTC([+-])(\d{2}):(\d{2})", line)
    
    date_part = match.group(1)
    sign = match.group(2)
    hours = int(match.group(3))
    minutes = int(match.group(4))
    
    dt = datetime.strptime(date_part, "%Y-%m-%d")
    
    offset = timedelta(hours=hours, minutes=minutes)
    
    if sign == '+':
        dt_utc = dt - offset
    else:
        dt_utc = dt + offset
        
    return dt_utc
line1 = sys.stdin.readline().strip()
line2 = sys.stdin.readline().strip()
dt1 = parse_datetime(line1)
dt2 = parse_datetime(line2)
diff_seconds = abs((dt1 - dt2).total_seconds())
full_days = int(diff_seconds // 86400)
print(full_days)