from chess_engine.errors import OffBoardError

class Board:
    def __init__(self):
        # creates an 8x8 2d list for the chess board
        self.grid = [[None for _ in range(8)] for _ in range(8)]

    def _check_out_of_bounds(self, square: tuple) -> None:
        """Helper method for detecting if an index is out of the bounds of our chess boards 8x8 grid"""
        col, row = square
        if col < 0 or col > 7:
            raise OffBoardError
        if row < 0 or row > 7:
            raise OffBoardError

    def get(self, square: tuple) -> object | None:
        """returns what is in any given sqaure on the chess board"""
        col, row = square
        self._check_out_of_bounds(square)
        return self.grid[col][row]

    def place(self, square: tuple, piece: object) -> None:
        """writes an input to any given square on the chess board."""
        col, row = square
        self._check_out_of_bounds(square)
        self.grid[col][row] = piece