with open("reasons.txt", "a") as file_object:
	while True:
		reason = input("Why are you love programming? ")
		if reason == "":
			break
		file_object.write(f"{reason}\n")
		print("python is very good")
