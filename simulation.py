from collections import deque

from action.entity_spawn.entity_spawn import SpawnEntity
from action.loopSimulation import LiveCycle
from instance_of_the_world.simulation_objects.dinamic_objects import Predator, Herbivore
from instance_of_the_world.simulation_objects.static_objects import Grass, Tree, Rock
from map.coordinates import Coordinates
from map.maps import Map


# class Simulation:

#     __herbivore = int(input('Введите число травоядных: '))
#     __predator = int(input('Введите число хищников: '))
#     __grass = int(input('Введите число травы: '))
#     __tree = int(input('Введите число деревьев: '))
#     __rock = int(input('Введите число камней: '))
#     __population = [__herbivore, __predator, __grass, __tree, __rock]
#     __types = deque((Herbivore(), Predator(), Grass(), Tree(), Rock()))
#     map: Map = Map(4, 4)
#     for entity in __population:
#         each = __types.popleft()
#         SpawnEntity(map).add_to_map(each, entity)
#     LiveCycle(map).endless_loop()
#
# Simulation()
m = Map(4, 4)

h = Herbivore()
g = Grass()
g1 = Grass()

m.add(Coordinates(4, 4), g1)
m.add(Coordinates(3, 1), g)
m.add(Coordinates(1, 1), h)

LiveCycle(m).endless_loop()


