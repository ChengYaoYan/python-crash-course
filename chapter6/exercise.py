# exercise1
marilyn = {
    'name': 'Marilyn',
    'sex': 'female',
    'work': 'desinger',
}
richard = {
    'name': 'Richard',
    'sex': 'male',
    'work': 'photographer'
}
people = [marilyn, richard]
for person in people:
    print(f"{person['name']:}")
    print(f"\tsex: {person['sex']}")
    print(f"\twork: {person['work']}")

# exercise2
dog = {
    'owner': 'Marilyn',
    'type': 'dog'
}
cat = {
    'owner': 'Robbie',
    'type': 'cat'
}
pets = [dog, cat]
for pet in pets:
    print(f"{pet['type']:}")
    print(f"\towner: {pet['owner']}")
