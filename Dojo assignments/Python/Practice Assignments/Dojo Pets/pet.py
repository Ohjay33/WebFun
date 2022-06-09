class Pet():
    def __init__(self, name, type, tricks, sound):
      self.name = name
      self.type = type
      self.tricks = tricks
      self.sound = sound
      self.energy = 100
      self.health = 100
    

# implement the following methods:
# sleep() - increases the pets energy by 25
    def sleep(self):
      self.energy += 25
      return self

# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
      self.energy += 5
      self.health += 10
      return self
# play() - increases the pet's health by 5
    def play(self):
      self.health += 5
# noise() - prints out the pet's sound
    def noise(self):
      print(self.sound)
      return self

#SENSEI BONUS: Use Inheritance to create sub classes of pets.

class Cat(Pet):
    def __init__(self, name, type, tricks, sound):
      super().__init__(name, type, tricks, sound)

class Dog(Pet):
    def __init__(self, name, type, tricks, sound):
      super().__init__(name, type, tricks, sound)
