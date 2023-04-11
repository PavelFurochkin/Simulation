from action.PathFinding.finding_path import FindPath
from action.entity_actions import Action
from instance_of_the_world.simulation_objects.dinamic_objects import Herbivore, Predator
from instance_of_the_world.simulation_objects.static_objects import Grass, Tree
from map.maps import Map


class LiveCycle:
    """
    Класс для запуска симуляции

        ...

    Attribute
    ---------
    self.map = map
        содержит текущую карту
    self.current_population = map.counting_population()
        содержит набор изначальный набор существ на карте

    Methods
    -------
    endless_loop(self)
        Метод запускает бесконечную симуляцию на карте

    meaninglessness_of_being(self)
        метод для проверки что на карте есть травоядные и можно продолжать симуляцию.
    """

    def __init__(self, map: Map):
        self.map = map
        self.current_population = map.counting_population(map)

    def endless_loop(self):
        while not self.meaninglessness_of_being():
            for entity in self.current_population:
                if isinstance(entity, Predator):
                    path = FindPath(entity, Herbivore, self.map).finding_path()
                    Action(self.map).make_move(entity, path)
                if isinstance(entity, Herbivore):
                    path = (FindPath(entity, Grass, self.map).
                            finding_path())
                    Action(self.map).make_move(entity, path)

    def step_of_loop(self):
        pass

    def stop_simulation(self):
        pass

    def refresh_population_statistic(self):
        pass

    def meaninglessness_of_being(self):
        herbivore_population = 0
        check_population: list = self.map.counting_population(self.map)
        for entity in check_population:
            if isinstance(entity, Herbivore):
                herbivore_population += 1

        if herbivore_population == 0:
            return True
        return False
