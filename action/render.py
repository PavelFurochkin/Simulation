from instanceOfTheWorld.Grass import Grass
from instanceOfTheWorld.Herbivore import Hearvibore
from instanceOfTheWorld.Predator import Predator
from instanceOfTheWorld.Rock import Rock
from instanceOfTheWorld.Tree import Tree
from instanceOfTheWorld.Map import Map

from action.Coordinates import Coordinates


class RenderField:

    def render(self, field: Map):
        for row in range(10):
            for column in range(10):
                c = Coordinates(row, column)
                entity_check = field.checkSpotNotEmpty(c)
                if c in field and isinstance(entity_check, Predator):
                    print('Pr')
                elif c in field and isinstance(entity_check, Hearvibore):
                    print('Hv')
                elif c in field and isinstance(entity_check, Grass):
                    print('Gr')
                elif c in field and isinstance(entity_check, Rock):
                    print('Ro')
                elif c in field and isinstance(entity_check, Tree):
                    print('Tr')
                else:
                    print(' ')