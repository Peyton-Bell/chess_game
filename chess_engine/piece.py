from chess_engine.board import Board

class Piece:
    """Parent Piece class in which all the other types of pieces inherit from"""
    def __init__(self, color):
        self.color = color

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

class Rook(Piece):    
    def __init__(self, color):
        super().__init__(color)

    def movement(self, board: object, square: tuple) -> set[tuple]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        possible_moves = set()
        for step_col, step_row in directions:
            col, row = square
            col += step_col
            row += step_row
            while 0 <= col < 8 and 0 <= row < 8:
                possible_moves.add((col, row))
                col += step_col
                row += step_row
        return possible_moves


