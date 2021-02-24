class Restaurant:
    def __init__(self, restaurant_name, cuisine_name):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name

    def describe_restaurant(self):
        print(f"restaurant name: {self.restaurant_name}\ncuisine name: {self.cuisine_name}")

    def open_restaurant(self):
        print("opening restaurant...")


restaurant =  Restaurant("happiness restaurant", "apple pie")
print(restaurant.restaurant_name)
print(restaurant.cuisine_name)
restaurant.describe_restaurant()
restaurant.open_restaurant()

chicken_restaurant = Restaurant("zhangji chicken", "fried chicken")
breakfast_restaurant = Restaurant("xiaoli breakfast", "noodle")
coffee_restaurant = Restaurant("happiness coffee", "coffee")
chicken_restaurant.describe_restaurant()
breakfast_restaurant.describe_restaurant()
coffee_restaurant.describe_restaurant()
