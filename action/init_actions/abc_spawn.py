from abc import abstractmethod
from random import randint

from action.actions import Action
from map.coordinates import Coordinates


class AbcSpawn(Action):
    """
       Базовый класс создания существ на текущей карте.

       ...

       Attributes
       ----------
       map: Map
           Представляет экземпляр текущей версии карты

       Methods
       -------
        perform(self)
           Метод базового класса для выполнения действия

        def random_coordinates(self)
            Предоставляет рандомные координаты

       add_to_map(self, entity: Entity, quantity: int)
           Вносит созданных существ на карту
       """
    def __init__(self, map):
        super().__init__(map)

    def perform(self):
        """
        Реализуем метод базового класса, путем наполнения карты существами
        :return: None
        """
        self.add_to_map()

    def random_coordinates(self):
        return Coordinates(row=randint(1, self.map.row_map),
                           column=randint(1, self.map.column_map))

    @abstractmethod
    def add_to_map(self) -> None:
        pass