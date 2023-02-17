from weapon import Weapon

class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Sword", 15)

    def attack(self, target):
        target.health -= self.active_weapon.attack_power
        print(f"\nYou did {self.active_weapon.attack_power} to {target.name}")
        print(f"{target.name} has {target.health} now")

