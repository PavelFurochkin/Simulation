from instance_of_the_world.creatures import Creature
from map.coordinates import Coordinates


class Herbivore(Creature):
    def __init__(self, coordinates: Coordinates = Coordinates(row=1, column=1),
                 spead: int = 5, health: int = 12, fight_power: int = 2,
                 sprite='Hb'):
        super().__init__(coordinates, spead, health)
        self.coordinates = coordinates
        self.health = health
        self.spead = spead
        self.sprite: str = sprite
        self.fight_power = fight_power
        # self.gender: str = 'male'
