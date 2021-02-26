class Restaurant:
    def __init__(self, restaurant_name, cuisine_name):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name
    def describe_restaurant(self):
        print(f"restaurant name: {self.restaurant_name}\ncuisine name: {self.cuisine_name}")

    def open_restaurant(self):
        print("opening restaurant...")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_name):
        super().__init__(restaurant_name, cuisine_name)
        self.flavors = ['Marilyn', 'Franklin']

    def show_flavors(self):
        print(self.flavors)


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"hi, {self.first_name}!")


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(['can add post', 'can delete post'])


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("priivleges of admin user:")
        [print(f"\t{privilege}") for privilege in self.privileges]


user = User("Richard", "Stewart")
user.describe_user()
user.greet_user()


ice_cream = IceCreamStand("ice_cream_stand", "ice cream")
ice_cream.show_flavors()
admin = Admin('Richard', 'Stewart')
admin.privileges.show_privileges()
