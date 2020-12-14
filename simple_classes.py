class Animal:
    def move(self):
        print("moving...")

a = Animal()
a.move()


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("woof! woof!")


d = Dog("Andy")
d.move()
d.bark()
print(d.name)


cities = list()  # cities = []
cities.append("Dallas")
cities.append("Chicago")
cities.append("New York")


