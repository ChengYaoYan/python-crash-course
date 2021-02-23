my_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream', 'fried chicken']

print(my_foods[:3])
print(my_foods[1:4])
print(my_foods[2:])


pizzas = [
    'Neapolitan Pizza',
    'Chicago Pizza',
    'New York-Style Pizza',
    'Sicilian Pizza'
    ]
copy_pizzas = pizzas[:]

print(f"pizzas: {pizzas}")
print(f"copy_pizzas: {copy_pizzas}")

pizzas.append('New Pizza')
print(f"pizzas: {pizzas}")
print(f"copy_pizzas: {copy_pizzas}")

for pizza in pizzas:
    print(pizza)

print()

[print(pizza) for pizza in pizzas]
