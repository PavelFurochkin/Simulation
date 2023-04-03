from random import choice

from map.coordinates import Coordinates
from instance_of_the_world.creatures import Creature


class Predator(Creature):
    def __init__(self, coordinates: Coordinates = Coordinates(row=0, column=0),
                 spead: int = 3, health: int = 10, fight_power: int = 2):
        super().__init__(coordinates, spead, health)
        self.health = health
        self.spead = spead
        self.fight_power: int = fight_power
        self.successful_hunting: int = 0
        self.sprite = 'Pr'
        self.gender = choice([1, 0])
