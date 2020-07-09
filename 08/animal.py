class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('{}: I like {}!'.format(self.name, food))


class Kitten(Animal):
    def make_sound(self):
        print('{}: Meow!'.format(self.name))


class Puppy(Animal):
    def make_sound(self):
        print('{}: Woof!'.format(self.name))

    def eat(self, food):
        super().eat(food)
        print('{}: Thank you for the great meal.'.format(self.name))


class Snake(Animal):
    def make_sound(self):
        print('{}: Sssss!'.format(self.name))

    def eat(self, food):
        print('{}: I dont like {}'.format(self.name, food))


micka = Kitten('Micka')
azor = Puppy('Azor')
micka.make_sound()
azor.make_sound()
micka.eat('mouse')
azor.eat('meat')
