from action import GrassSpawn, HerbivoreSpawn, PredatorSpawn, RockSpawn, TreeSpawn
from action.turn_actions.loopSimulation import LiveCycle
from map.maps import Map


class Simulation:
    def __init__(self, map: Map = Map(8, 8)):
        self.map = map
        self.init_action = [GrassSpawn(self.map),
                            HerbivoreSpawn(self.map),
                            PredatorSpawn(self.map),
                            RockSpawn(self.map),
                            TreeSpawn(self.map)]
        for action in self.init_action:
            action.perform()
        LiveCycle(map).perform()


if __name__ == '__main__':
    Simulation()
