from pieces import pawn
from pieces import bishop
from pieces import rook
from pieces import king
from pieces import queen
from pieces import knight
from board import board


chess_board = board()

black_test_rook = rook("black", (0, 0))
chess_board.grid[0][0] = black_test_rook

black_test_king = king("black", (0, 1))
chess_board.grid[0][1] = black_test_king

white_test_king = king("white", (0, 4))
chess_board.grid[0][4] = white_test_king

white_test_queen = queen("white", (7, 7))
chess_board.grid[7][7] = white_test_queen

chess_board.board_display()

while True:
    chess_board.move_piece()
    chess_board.update_kings_pos()


