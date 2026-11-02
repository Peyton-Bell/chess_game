from chess_engine.board import Board

def test_new_board_has_None_on_every_square():
    b = Board()
    for i in range(8):
        for j in range(8):
            assert b.grid[i][j] is None

def test_get_method_reads_a_given_square():
    b = Board()
    b.grid[3][4] = "piece"

    assert b.get((3, 4)) == "piece"

def test_place_method_writes_to_a_given_square():
    b = Board()

    b.place((3, 4), "piece")
    assert b.grid[3][4] == "piece"