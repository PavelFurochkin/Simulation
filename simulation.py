from action.PathFinding.finding_path import FindPath
from instance_of_the_world.simulation_objects.dinamic_objects import Predator, Herbivore
from map.coordinates import Coordinates
from map.maps import Map


class Simulation:
    world = Map(5, 5)
    predator = Predator()
    herbivore = Herbivore()
    world.add(Coordinates(1, 1), predator)
    world.add(Coordinates(1, 4), herbivore)
    world.add(Coordinates(4, 2), herbivore)

    search_to_pray = FindPath(predator, herbivore, world)

    search_to_pray.finding_path()