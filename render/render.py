from map.coordinates import Coordinates

from map.maps import Map


class RenderField:

    def render(self, field: Map):
        line = ''
        for row in range(1, field.row_map + 1):
            for column in range(1, field.column_map + 1):
                entity_check = field.get_object(Coordinates(row, column))
                if entity_check is not None:
                    line += f'|_{entity_check.sprite}_|'
                else:
                    line += '|____|'
            print(line)
            line = ''
