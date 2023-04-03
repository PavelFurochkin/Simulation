class Coordinates():
    def __init__(self, row: int, column: int) -> None:
        self.row = row
        self.column = column

    def __eq__(self, other) -> bool:
        return self.row == other.row and self.column == other.column

    def __hash__(self) -> int:
        return hash(self.__class__ and self.row and self.column)
