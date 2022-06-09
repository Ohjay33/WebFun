import pet


class Ninja():
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self
# feed() - feeds the ninja's pet invoking the pet eat() method

    def feed(self):
        self.pet.eat()
        return self
# bathe() - cleans the ninja's pet invoking the pet noise() method

    def bathe(self):
        self.pet.noise()
        return self


ohjay = Ninja("oscar", "moore", "dog", 'beef jerky', 'purana')

print(ohjay.treats)
print(ohjay.pet)
print(ohjay.)
