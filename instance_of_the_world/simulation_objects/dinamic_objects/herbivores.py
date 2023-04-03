from random import choice

from map.coordinates import Coordinates
from instance_of_the_world.creatures import Creature


class Hearvibore(Creature):
    def __init__(self, coordinates: Coordinates = Coordinates(row=0, column=0),
                 spead: int = 5, health: int = 20):
        super().__init__(coordinates, spead, health)
        self.health = health
        self.spead = spead
        self.sprite = 'Hb'
        self.gender = choice([1, 0])
