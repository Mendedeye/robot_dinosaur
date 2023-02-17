class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 50

    def attack(self, target):
        target.health -= self.attack_power
        print(f"\nYou did {self.attack_power} damage to {target.name}")
        print(f"{target.name} has {target.health} now")