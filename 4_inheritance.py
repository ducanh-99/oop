from abc import ABC, abstractclassmethod


class Animal(ABC):
    legs: int
    weight: float
    height: float

    def eat(self):
        pass

    def drink(self):
        print("Animal Drink")

    def move(self):
        pass

class Fish(Animal):

    def drink(self):
        print("Not Drink")

class Mammal(Animal):

    def eat(self):
        print("Mammal eating")

    def drink(self):
        print("Mamal Drink")

class People(Mammal):
    pass


def drink_water(animal: Animal):
    animal.drink()

drink_water(Fish())