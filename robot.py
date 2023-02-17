from weapon import Weapon
from dinosaur import Dinosaur

class Robot:

    def __init__(self):
        self.name = "Gerald"
        self.health = 100
        self.active_weapon = Weapon

    def attack(self, Dinosaur):
        Dinosaur.health = Dinosaur.health - self.active_weapon
