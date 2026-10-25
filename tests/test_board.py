from chess_engine.board import Board

def test_starting_position_has_32_pieces():
    b = Board()
    b.starting_position()
    count = sum(1 for row in b.grid for p in row if p is not None)
    assert count == 32