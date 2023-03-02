from abc import abstractmethod

import action.SelectionOfAction as Selection

import instanceOfTheWorld.Entity as Entity


class Creature(Entity):
    def __init__(self, coordinates, spead: int, health: int):
        super().__init__(coordinates)
        self.spead = spead
        self.health = health

    @abstractmethod
    def make_move(self, digit: int):
        select_position = Selection.Selection(self.coordinates)  # Выбираем клетку для взаимодействия
        if 0 <= digit <= 8:  # Диапазон соседних клеток для перемещения
            self.coordinates = select_position.interact(digit)  # Перешагиваем на новую клетку
