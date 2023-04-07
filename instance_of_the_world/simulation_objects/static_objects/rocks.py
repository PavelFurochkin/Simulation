from instance_of_the_world.entitys import Entity
from map.coordinates import Coordinates


class Rock(Entity):

    def __init__(self, coordinates: Coordinates = Coordinates(row=0, column=0), sprite='Rc'):
        super().__init__(coordinates)
        self.SPEAD: int = 0
        self.health: int = 1000
        self.sprite = sprite

