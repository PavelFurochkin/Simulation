from abc import abstractmethod
from maps import Map

from action.selection_of_action import Selection
from instance_of_the_world.entitys import Entity


class Creature(Entity):
    def __init__(self, coordinates, spead: int, health: int):
        super().__init__(coordinates)
        self.spead = spead
        self.health = health

    @abstractmethod
    def make_move(self, digit: int, map: Map):
        select_position = Selection(self.coordinates)  # Выбираем клетку для взаимодействия
        if 0 <= digit <= 8:  # Диапазон соседних клеток для перемещения
            self.coordinates = select_position.interact(digit)  # Перешагиваем на новую клетку
