from typing import Type

from action.Coordinates import Coordinates
from instanceOfTheWorld.Entity import Entity
from instanceOfTheWorld.Grass import Grass
from instanceOfTheWorld.Hearvibore import Hearvibore
from instanceOfTheWorld.Predator import Predator
from instanceOfTheWorld.Tree import Tree


class Map:
    def __init__(self):
        self.map = {}

    def add(self, position: Coordinates, entity: Entity) -> None:
        """
        Метод добавляет сушество по заданной координате в словарь
        """
        if isinstance(entity, Entity):
            self.map[position] = entity
            entity.coordinates = position

    def checkSpotNotEmpty(self, position: Coordinates) -> Entity:
        """
        Проверяет есть ли на клетке существо
        """
        return self.map.get(position, None)

    def delete(self, position: Coordinates) -> None:
        """
        Удаляет существо по заданной позиции
        """
        self.map.pop(position, "на данной клетке нет существ.")

    def meeting(self, first_entity: Entity, second_entity: Entity):
        if first_entity is isinstance(first_entity, Predator) and second_entity is isinstance(second_entity, Hearvibore):
            second_entity.health -= 2
            if second_entity.health == 0:
                self.delete(second_entity.coordinates)
        if first_entity is isinstance(first_entity, Hearvibore) and second_entity is isinstance(second_entity, (Grass, Tree)):
            second_entity.health -= 5
            if second_entity.health == 0:
                self.delete(second_entity.coordinates)



    def move(self, old_position: Coordinates, new_position: Coordinates) -> Coordinates:
        """
        Присваивает существу новые координаты на карте, старые удаляются
        """
        if self.checkSpotNotEmpty(old_position):
            entity = self.map[old_position]  # Присваиваем переменой старые координаты
        if
        entity.coordinates = new_position  # Обновляем координаты существа
        self.map[new_position] = entity  # Присваиваем переменой старые координаты
        return new_position



#
# m1 = Map()
# e1 = Predator()
# m1.add(Coordinates(1, 4), e1)
# f1 = m1.checkSpotNotEmpty(Coordinates(1, 4))
# print(m1.checkSpotNotEmpty(Coordinates(1, 4)))
