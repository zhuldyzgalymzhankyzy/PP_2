# json.py
import json

# 1. Convert dict to JSON
def to_json(data):
    return json.dumps(data)


# 2. Convert JSON to dict
def from_json(data):
    return json.loads(data)


# 3. Pretty JSON
def pretty_json(data):
    return json.dumps(data, indent=4)


# 4. JSON patch simple replace
def replace_value(obj, key, value):
    obj[key] = value
    return obj