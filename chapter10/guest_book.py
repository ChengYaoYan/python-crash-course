with open("guest_book.txt", "a") as file_object:
	while True:
		name = input("What's your name? ")
		if name == "":
			break
		file_object.write(f"{name}\n")
		print(f"Hello, {name}.")

