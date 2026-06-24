from pieces import pawn
from pieces import bishop
from pieces import rook
from pieces import king
from pieces import queen
from pieces import knight
from board import board


chess_board = board()
chess_board.starting_position()
chess_board.grid[4][7] = test_white_pawn = pawn("white", (4, 7))
chess_board.grid[3][0] = test_black_pawn = pawn("black", (3, 0))
chess_board.board_display()

print(test_white_pawn.movement(chess_board))
print(test_black_pawn.movement(chess_board))