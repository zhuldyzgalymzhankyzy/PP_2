import json
import sys

def apply_patch(source, patch):
    for key, value in patch.items():
        if value is None:
            # Remove key if exists
            source.pop(key, None)
        elif key in source and isinstance(source[key], dict) and isinstance(value, dict):
            # Recursive update
            apply_patch(source[key], value)
        else:
            # Add or replace
            source[key] = value
    return source
source = json.loads(sys.stdin.readline().strip())
patch = json.loads(sys.stdin.readline().strip())
result = apply_patch(source, patch)
print(json.dumps(result, separators=(',', ':'), sort_keys=True))