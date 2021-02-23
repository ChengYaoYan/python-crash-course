my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend favorite foods are:")
print(friend_foods)

my_foods.append('ice cream')
print(my_foods)
print(friend_foods)

another_friend_foods = my_foods
print(another_friend_foods)
another_friend_foods.append('fried chicken')
print(another_friend_foods)
print(my_foods)
