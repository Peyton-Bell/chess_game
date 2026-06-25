from pieces import pawn
from pieces import bishop
from pieces import rook
from pieces import king
from pieces import queen
from pieces import knight
from board import board


chess_board = board()
chess_board.starting_position()

test_queen = queen("black", (4, 7))
chess_board.grid[4][7] = test_queen

test_bishop = bishop("black", (3, 2))
chess_board.grid[4][2] = test_bishop

chess_board.board_display()
chess_board.move_piece()
chess_board.move_piece()

