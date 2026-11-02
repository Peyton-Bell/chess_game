class Board:
    # board contructor    
    def __init__(self):
        # creates an 8x8 2d list for the chess board
        self.grid = [[None for _ in range(8)] for _ in range(8)]

    def get(self, square: tuple) -> object | None:
        col, row = square
        return self.grid[col][row]

    def place(self, square: tuple, piece: object) -> None:
        col, row = square
        self.grid[col][row] = piece