class Animal:
    def __init__(self):
        self.age = 0
        self.name = ""
    
    def increment_age(self):
        self.age += 1

    def set_name(self, name):
        self.name = name

animal = Animal()
print("L'age de l'animal :", animal.age)
animal.increment_age()
print("L'age de l'animal après vieillissement :", animal.age)

animal.set_name("Luna")
print("L'animal se nomme :", animal.name)
