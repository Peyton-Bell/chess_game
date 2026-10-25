from chess_engine.board import Board

def test_starting_position_has_32_pieces():
    b = Board()
    b.starting_position()
    count = sum(1 for row in b.grid for p in row if p is not None)
    assert count == 32

def test_knights_on_starting_squares_have_2_moves():
    b = Board()
    b.starting_position()
    b1 = b.grid[7][1]
    b1_moves = b1.movement(b)

    moves = [(5, 0), (5, 2)]

    assert sorted(moves) == sorted(b1_moves)

