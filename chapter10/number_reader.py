import json

file_name = "number.json"
with open(file_name) as f:
	numbers = json.load(f)

print(numbers)