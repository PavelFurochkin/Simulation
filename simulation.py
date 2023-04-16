
from action.entity_spawn.entity_spawn import SpawnEntity
from action.loopSimulation import LiveCycle
from instance_of_the_world.simulation_objects.dinamic_objects import Predator, Herbivore
from instance_of_the_world.simulation_objects.static_objects import Grass, Tree, Rock
from map.maps import Map


class Simulation:
    def __init__(self):
        __herbivore = int(input('Введите число травоядных: '))
        __predator = int(input('Введите число хищников: '))
        __grass = int(input('Введите число травы: '))
        __tree = int(input('Введите число деревьев: '))
        __rock = int(input('Введите число камней: '))
        __population = [__herbivore, __predator, __grass, __tree, __rock]
        __types = [Herbivore, Predator, Grass, Tree, Rock]
        map: Map = Map(12, 12)

        for entity_type, count in zip(__types, __population):
            for i in range(count):
                each = entity_type()  # создание нового объекта каждый раз
                SpawnEntity(map).add_to_map(each, 1)
        LiveCycle(map).endless_loop()


if __name__ == '__main__':
    Simulation()
