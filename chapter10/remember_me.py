import json

username = input("what's your name? ")

file_name = "username.json"
with open(file_name, "w") as f:
	json.dump(username, f)
	print(f"We'll remember you when you are come back, {username}!")