from action.Coordinates import Coordinates

from instanceOfTheWorld.Creature import Creature


class Hearvibore(Creature):
    def __init__(self, coordinates: Coordinates = Coordinates(row=0, column=0),
                 spead: int = 5, health: int = 20):
        super().__init__(coordinates, spead, health)
        self.health = health
        self.spead = spead

    def set_start_position(self):
        pass


    def make_move(self, digit: int):
        pass


