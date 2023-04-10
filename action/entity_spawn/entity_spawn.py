from random import randint

from instance_of_the_world.entitys import Entity
from map.coordinates import Coordinates
from map.maps import Map


class SpawnEntity():
    """
    Описывает процесс создания существ на текущей карте.

    ...

    Attributes
    ----------
    map: Map
        Представляет экземпляр текущей версии карты

    Methods
    -------
     __create(self, entity: Entity, quantity: int)
        описывает создание существ конкретного типа

    add_to_map(self, entity: Entity, quantity: int)
        Вносит созданных существ на карту
    """

    def __init__(self, map: Map):
        self.map = map

    def __create(self, entity: Entity, quantity: int) -> list:
        animal_list = []
        for each in range(quantity):
            create_entity: Entity = entity
            animal_list.append(create_entity)
        return animal_list

    # Нереализованная механика при наличии размножения
    # def __choose_a_gender(self, kit: list, entity: Entity) -> None:
    #     if isinstance(entity, (Herbivore, Predator)):
    #         gender = 'female'
    #         for animal in kit[1:]:
    #             animal.gender = gender
    #             gender = 'female' if gender == 'male' else 'male'

    def add_to_map(self, entity: Entity, quantity: int) -> None:
        redy_to_add = self.__create(entity, quantity)
        # self.__choose_a_gender(redy_to_add, entity) # Нереализованная механика при наличии размножения
        for each in range(len(redy_to_add)):
            coord: Coordinates = (
                Coordinates(row=randint(1, self.map.row_map),
                            column=randint(1, self.map.column_map))
            )
            self.map.add(coord, entity)

