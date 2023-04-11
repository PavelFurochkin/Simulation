from typing import List

from instance_of_the_world.simulation_objects.dinamic_objects import Predator
from map.coordinates import Coordinates
from instance_of_the_world.entitys import Entity


class Map:
    def __init__(self, row_map: int, column_map: int):
        if isinstance(row_map, int) and isinstance(column_map, int):
            self.row_map = row_map
            self.column_map = column_map
        else:
            print('Введите целые числа')

        self.map = {}

    def add(self, position: Coordinates, entity: Entity) -> None:
        """
        Метод добавляет сушество по заданной координате в словарь
        """
        if isinstance(entity, Entity):
            self.map[position] = entity
            entity.coordinates = position

    def spot_is_empty(self, position: Coordinates) -> bool:
        """
        Проверяет есть ли на клетке существо
        """
        return position not in self.map

    def move_object(self, entity: Entity, old_coordinates: Coordinates,
                    new_coordinates: Coordinates):
        self.delete(old_coordinates)
        self.add(new_coordinates, entity)

    def get_object(self, position: Coordinates):
        if position in self.map:
            return self.map[position]
        return None

    def delete(self, position: Coordinates) -> None:
        """
        Удаляет существо по заданной позиции
        """
        self.map.pop(position, "на данной клетке нет существ.")

    def counting_population(self, map):
        population = []
        for spot in map:
            entity: Entity = map.get_object(spot)
            if entity is not None:
                population.append(entity)
        return population

    def __iter__(self):
        return iter(self.map)

