from chess_engine.errors import OffBoardError

class Board:
    # board contructor    
    def __init__(self):
        # creates an 8x8 2d list for the chess board
        self.grid = [[None for _ in range(8)] for _ in range(8)]

    def _check_out_of_bounds(self, square: tuple) -> None:
        col, row = square
        if col < 0 or col > 7:
            raise OffBoardError
        if row < 0 or row > 7:
            raise OffBoardError

    def get(self, square: tuple) -> object | None:
        col, row = square
        self._check_out_of_bounds(square)
        return self.grid[col][row]

    def place(self, square: tuple, piece: object) -> None:
        col, row = square
        self._check_out_of_bounds(square)
        self.grid[col][row] = piece