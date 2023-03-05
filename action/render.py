from instance_of_the_world import Grass
from instance_of_the_world import Hearvibore
from instance_of_the_world import Predator
from instance_of_the_world import Rock
from instance_of_the_world import Tree
from maps import Map

from action.Coordinates import Coordinates


class RenderField:

    def render(self, field: Map):
        for row in range(10):
            for column in range(10):
                c = Coordinates(row, column)
                entity_check = field.check_spot_not_empty(c)
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