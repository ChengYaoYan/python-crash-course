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


ice_cream = IceCreamStand("ice_cream_stand", "ice cream")
ice_cream.show_flavors()
