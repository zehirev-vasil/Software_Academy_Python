class Animal:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = int(age)
        self.gender = gender

    def make_sound(self):
        pass


class Dog(Animal):

    def make_sound(self):
        return 'Bau Bau'


class Cat(Animal):

    def make_sound(self):
        return 'Miau Miau'


myCat = Cat('Sun',5, 'female')
myDog = Dog('Moon', 5, 'male')

list_of_animals = [myCat, myDog]

for animal in list_of_animals:
    print(animal.make_sound())
