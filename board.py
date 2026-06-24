from pieces import pawn
from pieces import bishop
from pieces import knight
from pieces import rook
from pieces import queen
from pieces import king
# 2d list for the board containing an 8x8 grid (column, row) numberred 1-7
class board:
    def __init__(self):
    
        self.grid = [[None for _ in range(8)] for _ in range (8)]
    

    def starting_position(self):
        # white pawns starting spot
        for i in range(8):
            self.grid[6][i] = pawn("white", (i, 1))

        # black pawns starting spot
        for i in range(8):
            self.grid[1][i] = pawn("black", (i, 6))
        
        # white rooks starting spot
        self.grid[7][0] = rook("white", (0, 0))
        self.grid[7][7] = rook("white", (7, 0))

        # black rooks starting spot
        self.grid[0][7] = rook("black", (7, 7))
        self.grid[0][0] = rook("black", (0, 7))

        # white knights starting spot
        self.grid[7][1] = knight("white", (1, 0))
        self.grid[7][6] = knight("white", (6, 0))

        # black knights starting spot
        self.grid[0][6] = knight("black", (6, 7))
        self.grid[0][1] = knight("black", (1, 7))

        # white bishops starting spot
        self.grid[7][2] = bishop("white", (2, 0))
        self.grid[7][5] = bishop("white", (5, 0))

        # black bishops starting spot
        self.grid[0][5] = bishop("black", (5, 7))
        self.grid[0][2] = bishop("black", (2, 7))

        # white queen starting spot
        self.grid[7][3] = queen("white", (3, 0))

        # black queen starting spot
        self.grid[0][3] = queen("black", (3, 7))

        # white king starting spot
        self.grid[7][4] = king("white", (4, 0))

        # black king starting spot
        self.grid[0][4] = king("black", (4, 7))


    def board_display(self):
        for rows in self.grid:
            for row in rows:
                if row != None:
                    print(row.display(), end = " ")
                else:
                    print(".", end = " ")
            print()

chess_board = board()
chess_board.starting_position()
chess_board.board_display()
    

    

        

