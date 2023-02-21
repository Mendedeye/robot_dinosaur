from robot import Robot

class Fleet:

    def __init__(self):
        self.fleet_list = []
        self.fleet_size = self.get_fleet_size()

    def get_fleet_size(self):
        user_input = input("\nPlese enter in how many Robots you want in your fleet: ")
        return user_input

    def form_fleet(self, fleet_list, list_size):
        pass
    
