from pieces import pawn
from pieces import bishop
from pieces import rook
from pieces import king
from pieces import queen
from pieces import knight
from board import board


chess_board = board()
chess_board.starting_position()
chess_board.board_display()
chess_board.in_check()