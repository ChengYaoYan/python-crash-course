class Restaurant:
    def __init__(self, restaurant_name, cuisine_name):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name
        self.number_served = 0

    def describe_restaurant(self):
        print(f"restaurant name: {self.restaurant_name}\ncuisine name: {self.cuisine_name}")

    def open_restaurant(self):
        print("opening restaurant...")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served = number_served
        print(f"{number_served} customers were served in")
        print("a day of busness.")


class User:
    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"hi, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


restaurant = Restaurant("happiness restaurant", "happiness")
print(restaurant.number_served)

restaurant.number_served = 10
print(restaurant.number_served)

restaurant.set_number_served(200)
print(restaurant.number_served)

restaurant.increment_number_served(1000)

user = User("Richard", "Stewart", 10)
user.describe_user()
user.greet_user()
print(user.login_attempts)
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)
