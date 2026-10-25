from chess_engine.pieces import Pawn, Bishop, Rook, King, Queen, Knight
from chess_engine.board import Board


chess_board = Board()
chess_board.starting_position()
chess_board.board_display()

while True:
    chess_board.move_piece()
