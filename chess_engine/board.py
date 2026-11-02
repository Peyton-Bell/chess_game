class Board:
    # board contructor    
    def __init__(self):
        self.grid = [[None for row in range(8)] for column in range(8)]

    def get(self, square: tuple) -> object | None:
        x, y = square
        return self.grid[x][y]

    def place(self, square: tuple, piece: object) -> None:
        x, y = square
        self.grid[x][y] = piece