from collections import deque
from typing import List

from action.PathFinding.finding_path import FindPath
from action.entity_actions import Action
from instance_of_the_world.simulation_objects.dinamic_objects import Herbivore, Predator
from instance_of_the_world.simulation_objects.static_objects import Grass, Tree
from map.coordinates import Coordinates
from map.maps import Map


class LiveCycle:
    """
    """
    def __init__(self, map: Map):
        self.map = map

    def endless_loop(self):
        while not self.meaninglessness_of_being():
            current_population = self.map.counting_population()
            for entity in current_population:
                if isinstance(entity, Predator):
                    path = FindPath(entity, Herbivore, self.map).finding_path()
                    Action(self.map).make_move(entity, path)
                if isinstance(entity, Herbivore):
                    path = (FindPath(entity, (Tree, Grass), self.map).
                            finding_path())
                    Action(self.map).make_move(entity, path)


    def step_of_loop(self):
        pass

    def stop_simulation(self):
        pass

    def refresh_population_statistic(self):
        pass

    def meaninglessness_of_being(self):
        pass

m = Map(5,5)
p = Predator()
h = Herbivore()
m.add(Coordinates(1, 1), p)
m.add(Coordinates(3, 3), h)

p.successful_hunting = 4
l = [p]
s = LiveCycle(m, l)
dd = s.endless_loop()
print(dd)