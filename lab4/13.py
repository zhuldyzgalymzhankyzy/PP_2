import json
import sys
import re

def resolve_query(data, query):
    try:
        parts = query.split('.')
        current = data

        for part in parts:
            tokens = re.findall(r'([^\[\]]+)|\[(\d+)\]', part)

            for key, index in tokens:
                if key:
                    if not isinstance(current, dict) or key not in current:
                        return "NOT_FOUND"
                    current = current[key]
                elif index:
                    if not isinstance(current, list):
                        return "NOT_FOUND"
                    idx = int(index)
                    if idx < 0 or idx >= len(current):
                        return "NOT_FOUND"
                    current = current[idx]

        return json.dumps(current, separators=(',', ':'))
    except:
        return "NOT_FOUND"
data = json.loads(sys.stdin.readline().strip())
q = int(sys.stdin.readline().strip())

for _ in range(q):
    query = sys.stdin.readline().strip()
    result = resolve_query(data, query)
    print(result)