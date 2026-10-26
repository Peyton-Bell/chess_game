from chess_engine.board import Board
from chess_engine.pieces import Pawn, Knight, Queen, Bishop, King, Rook

def test_starting_position_has_32_pieces():
    b = Board()
    b.starting_position()
    count = sum(1 for row in b.grid for p in row if p is not None)
    assert count == 32

def test_knight_on_b1_has_2_moves():
    b = Board()
    b.starting_position()
    b1 = b.grid[7][1]
    actual_moves = b1.movement(b)

    expected_moves = [(5, 0), (5, 2)]

    assert sorted(expected_moves) == sorted(actual_moves)

def test_knight_in_center_has_8_moves():
    b = Board()
    b.grid[4][4] = Knight("white", (4, 4))
    expected_moves = [(2, 3), (2, 5), (3, 2), (3, 6), (5, 2), (5, 6), (6, 3), (6, 5)]
    actual_moves = b.grid[4][4].movement(b)

    assert sorted(expected_moves) == sorted(actual_moves)


