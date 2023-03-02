class Coordinates():
    def __init__(self, row: int, column: int) -> None:
        if (type(row) in (int,) and row > 0) and (type(column) in (int,) and column > 0):
            self.row = row
            self.column = column

    def __eq__(self, other) -> bool:
        return self.row == other.row and self.column == other.column

    def __hash__(self) -> int:
        return hash((self.row, self.column))
