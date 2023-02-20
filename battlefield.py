from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot("Jerry")
        self.dinosaur = Dinosaur("Fredrick",40)

    def run_game(self):

        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print(f"\n\nHello today you will be witnessing a battle between {self.robot.name} and {self.dinosaur.name}")



    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            if self.dinosaur.health <= 0:
                print(f"\n{self.dinosaur.name} is dead.")
                break
            self.dinosaur.attack(self.robot)
            if self.robot.health <= 0:
                print(f"\n{self.robot.name} is dead.")
                break

    def display_winner(self):
        if self.robot.health > self.dinosaur.health:
            print(f"{self.robot.name} is the winner!!!")
            print("Humanity's creation made them extinct!!! Again....")
        else: 
            print(f"{self.dinosaur.name} is the winner!!!")
            print("Welcome to the dark ages...")