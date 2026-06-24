from pieces import pawn
from pieces import bishop
from pieces import rook
from pieces import king
from pieces import queen
from pieces import knight
from board import board


chess_board = board()
chess_board.starting_position()
#chess_board.board_display()

piece = chess_board.grid[7][2]
print(piece.display())
print(piece.movement(chess_board))
