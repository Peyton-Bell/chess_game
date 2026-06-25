from pieces import pawn
from pieces import bishop
from pieces import rook
from pieces import king
from pieces import queen
from pieces import knight
from board import board


chess_board = board()
chess_board.starting_position()

test_queen = queen("white", (3, 7))
chess_board.grid[3][7] = test_queen

test_bishop = bishop("white", (4, 2))
chess_board.grid[4][2] = test_bishop

chess_board.board_display()
chess_board.move_piece()

