import pytest
from chess_engine.piece import *
from chess_engine.board import Board

@pytest.fixture
def piece_movement_setup():
    b = Board()
    p = Piece("white")
    b.place((4, 4), p)

rook_answer_key_e5 = {(3, 4), (2, 4), (1, 4), (0, 4), (5, 4), (6, 4), (7, 4), (4, 5), (4, 6), (4, 7), (4, 3), (4, 2), (4, 1), (4, 0)}
def test_rook_valid_moves_from_e5():
    b = Board()
    rook = Rook("white")
    assert rook.movement(b, (4, 4)) == rook_answer_key_e5
    
bishop_answer_key_e5 = {(5, 5), (6, 6), (7, 7), (3, 3), (2, 2), (1, 1), (0, 0), (3, 5), (2, 6), (1, 7), (5, 3), (6, 2), (7, 1)}
def test_bishop_valid_moves_from_e5():
   b = Board()
   bishop = Bishop("white")
   assert bishop.movement(b, (4, 4)) == bishop_answer_key_e5

def test_queen_valid_moves_from_e5():
    queen_answer_key_e5 = rook_answer_key_e5 | bishop_answer_key_e5
    b = Board()
    queen = Queen("white")
    assert queen.movement(b, (4, 4)) == queen_answer_key_e5



    
