from chess_engine.board import Board

def test_new_board_has_None_on_every_square():
    b = Board()
    for i in range(8):
        for j in range(8):
            assert b.grid[i][j] is None