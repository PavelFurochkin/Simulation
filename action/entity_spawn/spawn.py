from collections import deque

from instance_of_the_world.entitys import Entity
from instance_of_the_world.simulation_objects.dinamic_objects import Herbivore, Predator
from instance_of_the_world.simulation_objects.static_objects import Grass, Tree, Rock
from map.maps import Map


class Spawn:

    def __init__(self, map: Map):
        self.__map = map

    __herbivore = int(input('Введите число травоядных: '))
    __predator = int(input('Введите число хищников: '))
    __grass = int(input('Введите число травы: '))
    __tree = int(input('Введите число деревьев: '))
    __rock = int(input('Введите число камней: '))
    __population = deque((__herbivore, __predator, __grass, __tree, __rock))
    __types = deque((Herbivore(), Predator(), Grass(), Tree(), Rock()))
    quantity: int = __population.popleft()

    def create_herbivore(self):
        for q in range(self.quantity):
            create = Herbivore()
            self.__map.add(create.coordinates, create)
            print(self.__map)

m = Map(5, 5)
s = Spawn(m).create_herbivore()



