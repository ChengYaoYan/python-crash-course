print("Please input two number, and input 'q' for exit.\n")

while True:
	first_number = input("Input first number: ")
	if first_number == "q":
		break
	second_number = input("Input second number: ")
	if second_number == "q":
		break

	try:
		answer = int(first_number) / int(second_number)
	except ValueError:
		print("your input should be a number.\n")
	except ZeroDivisionError:
		print("can't divide by zero.\n")
	else:
		print(answer)
