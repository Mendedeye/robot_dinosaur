from weapon import Weapon

class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon()


    def attack(self, target):
        damage = self.active_weapon.attack_power

        print(f"\nYou did {damage} damage to {target.name}")
        target.health -= damage
        print(f"{target.name} has {target.health} now")
