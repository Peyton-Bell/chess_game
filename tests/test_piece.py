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

def test_king_valid_moves_from_e5():
    king_answer_key = {(5, 4), (5, 3), (4, 3), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5)}
    b = Board()
    king = King("white")
    assert king.movement(b, (4, 4)) == king_answer_key

def test_knight_valid_moves_from_e5():
    knight_answer_key = {(5, 6), (6, 5), (6, 3), (5, 2), (3, 2), (2, 3), (2, 5), (3, 6)}
    b = Board()
    knight = Knight("white")
    assert knight.movement(b, (4, 4)) == knight_answer_key

def test_black_pawn_moves_from_e5():
    black_pawn_answer_key = {(4, 3)}
    b = Board()
    black_pawn = Pawn("black")
    assert black_pawn.movement(b, (4, 4)) == black_pawn_answer_key

def test_white_pawn_moves_from_e5():
    white_pawn_answer_key = {(4, 5)}
    b = Board()
    white_pawn = Pawn("white")
    assert white_pawn.movement(b, (4, 4)) == white_pawn_answer_key


    
