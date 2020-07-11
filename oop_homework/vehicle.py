class Vehicle:
    def __init__(self, color):
        self.consumption_coefficient = 10
        self.color = color
        self.price_fuel = 26.9
        self.max_person = 1

    def get_color(self):
        print('Your {} is {}'.format(Vehicle.__name__.lower(), self.color))
        return self.color

    def get_consumption(self):
        print('Your {} has consumption {} l/100 km.'.format(Vehicle.__name__.lower(), self.consumption_coefficient))
        return self.consumption_coefficient

    def calculate_price(self, km):
        return self.get_consumption() * self.price_fuel * km / 100

    def calculate_price_per_person(self, km):
        return self.calculate_price(km) / self.max_person

    def set_fuel_price(self, price):
        self.price_fuel = price

    def type_of_road(self):
        print('Road.')


class Car(Vehicle):
    def __init__(self, color):
        super().__init__(color)
        self.consumption_coefficient = 8
        self.max_person = 5

    def get_consumption(self):
        super().get_consumption()
        print('If you are go alone, use motorbike or bike.')
        return self.consumption_coefficient

    def type_of_road(self):
        print('Roads or motorways.')


class Bike(Vehicle):
    def __init__(self, color):
        super().__init__(color)
        self.consumption_coefficient = 0
        self.max_person = 1

    def calculate_price(self, km):
        print('It is free!')
        return 0

    def get_consumption(self):
        super().get_consumption()
        print('It is free and eco-friendly. Thanks!')

    def type_of_road(self):
        print('Roads or pavements.')
