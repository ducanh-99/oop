class People:
    name: str
    age: int
    address: str

    def __init__(self, name="My", age=19, address="Ninh Binh") -> None:
        self.name = name
        self.age = age
        self.address = address

    def move(self) -> None:
        print("MOVEEE")

    def eat(self, food) -> None:
        print("eat " + food)


# instance
person_1 = People()
# person_2 = People()


print(person_1.name, person_1.address, person_1.age)

# print(person_1.name)

# person_1.move()
# person_1.eat(food="Tom hum")
