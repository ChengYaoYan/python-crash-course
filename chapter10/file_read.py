file_name = "learning_python.txt"

with open(file_name) as file_object:
    print(file_object.read())

with open(file_name) as file_object:
    for line in file_object:
        print(line)

with open(file_name) as file_object:
    lines = file_object.readlines()

print("######################")
[print(line) for line in lines]

[print(line.replace('Python', 'C')) for line in lines]
