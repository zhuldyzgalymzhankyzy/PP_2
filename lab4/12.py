import json
import sys
def deep_diff(obj1, obj2, path=""):
    diffs = []
    keys = set(obj1.keys()) | set(obj2.keys())

    for key in keys:
        new_path = f"{path}.{key}" if path else key

        if key not in obj1:
            diffs.append((new_path, "<missing>", json.dumps(obj2[key], separators=(',', ':'))))
        elif key not in obj2:
            diffs.append((new_path, json.dumps(obj1[key], separators=(',', ':')), "<missing>"))
        else:
            val1 = obj1[key]
            val2 = obj2[key]

            if isinstance(val1, dict) and isinstance(val2, dict):
                diffs.extend(deep_diff(val1, val2, new_path))
            elif val1 != val2:
                diffs.append((
                    new_path,
                    json.dumps(val1, separators=(',', ':')),
                    json.dumps(val2, separators=(',', ':'))
                ))

    return diffs
obj1 = json.loads(sys.stdin.readline().strip())
obj2 = json.loads(sys.stdin.readline().strip())

differences = deep_diff(obj1, obj2)

if not differences:
    print("No differences")
else:
    for path, old, new in sorted(differences):
        print(f"{path} : {old} -> {new}")