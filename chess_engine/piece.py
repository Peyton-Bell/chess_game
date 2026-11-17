from chess_engine.board import Board

class Piece:
    """Parent Piece class in which all the other types of pieces inherit from"""
    def __init__(self, color):
        self.color = color

    def movement(self, board: object, square: tuple) -> set[tuple]:
        possible_moves = set()
        for step_col, step_row in self.directions:
            counter = 0
            col, row = square
            col += step_col
            row += step_row
            while 0 <= col < 8 and 0 <= row < 8 and counter < self.limit:
                possible_moves.add((col, row))
                counter += 1
                col += step_col
                row += step_row
            
        return possible_moves

class Bishop(Piece):
    directions = ((1, 1), (-1, 1), (1, -1), (-1, -1))
    limit = 8
        
class Rook(Piece):    
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    limit = 8

class Queen(Piece):
    directions = Bishop.directions + Rook.directions
    limit = 8

class King(Piece):
    directions = Queen.directions
    limit = 1

class Knight(Piece):
    directions = ((-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, 1), (-2, -1))
    limit = 1

