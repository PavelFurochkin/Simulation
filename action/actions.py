from abc import ABC, abstractmethod

from map.maps import Map


class Action(ABC):
    def __init__(self, map: Map):
        self.map = map

    @abstractmethod
    def perform(self):
        pass