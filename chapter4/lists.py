import random

for value in range(1, 21):
    print(value)

# for value in range(1, 10_000_000):
#     print(value)

numbers = []
for i in range(1, 11):
    numbers.append(random.randint(1, 10_000_000))
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# odd numbers
odd_numbers = []
for value in range(1, 21, 2):
    odd_numbers.append(value)

print(odd_numbers)

for value in range(1, 11):
    print(value * 3)

# cubes
for value in range(1, 11):
    print(value ** 3)

cubes = [value ** 3 for value in range(1, 11)]
print(cubes)
