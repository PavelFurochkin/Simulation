from instance_of_the_world.entitys import Entity
from map.coordinates import Coordinates


class Tree(Entity):

    def __init__(self, coordinates: Coordinates = Coordinates(row=0, column=0),
                 sprite='Tr'):
        super().__init__(coordinates)
        self.SPEAD: int = 0
        self.health: int = 200
        self.sprite = sprite
