from datetime import datetime, timedelta
import sys
import re

def parse(line):
    m = re.match(r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) UTC([+-])(\d{2}):(\d{2})", line)
    date_part = m.group(1)
    time_part = m.group(2)
    sign = 1 if m.group(3) == '+' else -1
    hh = int(m.group(4))
    mm = int(m.group(5))
    
    local_dt = datetime.strptime(date_part + " " + time_part, "%Y-%m-%d %H:%M:%S")
    offset = timedelta(hours=hh, minutes=mm) * sign
    utc_dt = local_dt - offset
    return utc_dt

start_line = sys.stdin.readline().strip()
end_line = sys.stdin.readline().strip()

start_utc = parse(start_line)
end_utc = parse(end_line)

duration = int((end_utc - start_utc).total_seconds())
print(duration)