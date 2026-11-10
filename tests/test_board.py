from chess_engine.board import Board
import pytest
from chess_engine.errors import OffBoardError


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

@pytest.mark.parametrize("square", [(8, 0), (0, 8), (-1, 0), (0, -1)])
def test_get_raises_off_board_error(square):
    b = Board()
    with pytest.raises(OffBoardError):
        b.get(square)

@pytest.mark.parametrize("square", [(8, 0), (0, 8), (-1, 0), (0, -1)])
def test_place_raises_off_board_error(square):
    b = Board()
    with pytest.raises(OffBoardError):
        b.place(square, "piece")

@pytest.mark.parametrize("corners", [(0, 0), (7, 0), (0, 7), (7, 7)])
def test_corners_can_be_read_and_written_to(corners):
    b = Board()

    b.place(corners, "piece")

    assert b.get(corners) == "piece"


