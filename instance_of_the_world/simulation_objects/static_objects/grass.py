from instance_of_the_world.aliveentity import AliveEntity
from map.coordinates import Coordinates


class Grass(AliveEntity):
    def __init__(self, coordinates: Coordinates, sprite="Gr", health: int = 1):
        super().__init__(coordinates, sprite, health)
