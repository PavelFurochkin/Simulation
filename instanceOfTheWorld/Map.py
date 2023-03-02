import action.Coordinates as Coordinates

import instanceOfTheWorld.Entity as Entity
import instanceOfTheWorld.Grass as Grass
import instanceOfTheWorld.Herbivore as Herbivore
import instanceOfTheWorld.Predator as Predator
import instanceOfTheWorld.Tree as Tree


class Map:
    def __init__(self):
        self.map = {}

    def add(self, position: Coordinates, entity: Entity.Entity) -> None:
        """
        Метод добавляет сушество по заданной координате в словарь
        """
        if isinstance(entity, Entity.Entity):
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
        if first_entity is isinstance(first_entity, Predator.Predator) and second_entity is isinstance(second_entity, Herbivore.Hearvibore):
            second_entity.health -= 2  # Хищник нападает на травоядное
            if second_entity.health == 0:
                self.delete(second_entity.coordinates)
        if first_entity is isinstance(first_entity, Herbivore.Hearvibore) and second_entity is isinstance(second_entity, (Grass.Grass, Tree.Tree)):
            second_entity.health -= 5  # Травоядное ест траву
            if second_entity.health == 0:
                self.delete(second_entity.coordinates)



m1 = Map()
e1 = Predator.Predator()
m1.add(Coordinates.Coordinates(1, 4), e1)
f1 = m1.checkSpotNotEmpty(Coordinates.Coordinates(1, 4))
print(m1.checkSpotNotEmpty(Coordinates.Coordinates(1, 4)))
