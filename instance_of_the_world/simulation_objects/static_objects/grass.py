from instance_of_the_world.entitys import Entity
from map.coordinates import Coordinates


class Grass(Entity):

    def __init__(self, coordinates: Coordinates = Coordinates(row=0, column=0),
                 sprite='Gr'):
        super().__init__(coordinates)
        self.SPEAD: int = 0
        self.health: int = 1
        self.sprite = sprite
