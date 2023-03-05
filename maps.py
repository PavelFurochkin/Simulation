from action.Coordinates import Coordinates

from instance_of_the_world.entitys import Entity
from instance_of_the_world.simulation_objects.static_objects.grass import Grass
from instance_of_the_world.simulation_objects.dinamic_objects.herbivores import Hearvibore
from instance_of_the_world.simulation_objects.dinamic_objects.predators import Predator
from instance_of_the_world.simulation_objects.static_objects.trees import Tree


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

    def check_spot_not_empty(self, position: Coordinates) -> Entity:
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
            first_entity.health += 2
            if second_entity.health == 0:
                self.delete(second_entity.coordinates)
        if first_entity is isinstance(first_entity, Hearvibore) and second_entity is isinstance(second_entity, (Grass, Tree)):
            second_entity.health -= 5  # Травоядное ест траву
            first_entity.health += 2
            if second_entity.health == 0:
                self.delete(second_entity.coordinates)



m1 = Map()
e1 = Predator()
m1.add(Coordinates(1, 4), e1)
f1 = m1.check_spot_not_empty(Coordinates(1, 4))
print(m1.check_spot_not_empty(Coordinates(1, 4)))
