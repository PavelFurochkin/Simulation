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

    def meeting(self, first_entity: Entity, second_entity: Entity) -> None:
        """
        Метод моделирует взаимодействие представителей пищевых цепочек
        """
        if first_entity is isinstance(first_entity, Predator) and second_entity is isinstance(second_entity, Hearvibore):
            second_entity.health -= 2  # Хищник нападает на травоядное
            if second_entity.health == 0:
                self.delete(second_entity.coordinates)
        if first_entity is isinstance(first_entity, Hearvibore) and second_entity is isinstance(second_entity, (Grass, Tree)):
            second_entity.health -= 5  # Травоядное ест траву
            if second_entity.health == 0:
                self.delete(second_entity.coordinates)


#
# m1 = Map()
# e1 = Predator()
# m1.add(Coordinates(1, 4), e1)
# f1 = m1.checkSpotNotEmpty(Coordinates(1, 4))
# print(m1.checkSpotNotEmpty(Coordinates(1, 4)))
