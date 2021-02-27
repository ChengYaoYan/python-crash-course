import json

filename = "username.josn"
with open(filename) as f:
	username = json.load(f)
	print(f"Welcome come back, {username}!")