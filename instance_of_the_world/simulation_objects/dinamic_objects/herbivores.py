from instance_of_the_world.creatures import Creature
from map.coordinates import Coordinates


class Herbivore(Creature):
    def __init__(self, coordinates: Coordinates = Coordinates(row=1, column=1),
                 spead: int = 5, health: int = 20, sprite='Hb'):
        super().__init__(coordinates, spead, health)
        self.coordinates = coordinates
        self.health = health
        self.spead = spead
        self.sprite: str = sprite
        # self.gender: str = 'male'
