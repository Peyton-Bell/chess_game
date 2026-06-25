from pieces import pawn
from pieces import bishop
from pieces import rook
from pieces import king
from pieces import queen
from pieces import knight
from board import board


chess_board = board()
chess_board.starting_position()

test_queen = queen("white", (1, 5))
chess_board.grid[1][5] = test_queen

test_bishop = bishop("white", (4, 2))
chess_board.grid[4][2] = test_bishop

chess_board.board_display()

print(test_bishop.movement(chess_board))
