import random

class Weapon:

    def __init__(self):
        self.weapons_list = ["Sword", "Axe", "Shotgun"]
        self.name = self.choose_weapon()
        self.attack_power = self.weapon_damage(self.name)

# Allows the user to choose a weapon from the given list
    def choose_weapon(self):
        self.user_choice = ""

        self.print_list(self.weapons_list)
        self.user_choice = input("\nPlease enter in a weapon from the given list: ")
        
        return self.user_choice
# Prints a list
    def print_list(self, selected_list):
        for item in selected_list:
            print(f"{item}")

# 
    def weapon_damage(self, name):
        damage = 0

        if name == "Sword":
            damage = 12
        elif name == "Axe":
            damage = 14
        elif name == "Shotgun":
            damage = 25
        else:
            damage = random.randomint(10,18)

        return damage