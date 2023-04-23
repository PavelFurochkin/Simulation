from action.init_actions.abc_spawn import AbcSpawn
from instance_of_the_world import Predator
from map.coordinates import Coordinates


class PredatorSpawn(AbcSpawn):
    def __init__(self, map):
        super().__init__(map)
        self.quantity = round(self.map.matrix_size() * 0.02)

    def add_to_map(self) -> None:
        while self.quantity != 0:
            for each in range(self.quantity):
                coord: Coordinates = self.random_coordinates()
                if self.map.spot_is_empty(coord):
                    self.map.add(coord, Predator(self.random_coordinates()))
                    self.quantity -= 1
                else:
                    continue