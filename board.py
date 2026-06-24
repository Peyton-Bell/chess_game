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
            self.grid[6][i] = pawn("white", (6, i))

        # black pawns starting spot
        for i in range(8):
            self.grid[1][i] = pawn("black", (1, i))
        
        # white rooks starting spot
        self.grid[7][0] = rook("white", (7, 0))
        self.grid[7][7] = rook("white", (7, 7))

        # black rooks starting spot
        self.grid[0][7] = rook("black", (0, 7))
        self.grid[0][0] = rook("black", (0, 0))

        # white knights starting spot
        self.grid[7][1] = knight("white", (7, 1))
        self.grid[7][6] = knight("white", (7, 6))

        # black knights starting spot
        self.grid[0][6] = knight("black", (0, 6))
        self.grid[0][1] = knight("black", (0, 1))

        # white bishops starting spot
        self.grid[7][2] = bishop("white", (7, 2))
        self.grid[7][5] = bishop("white", (7, 5))

        # black bishops starting spot
        self.grid[0][5] = bishop("black", (0, 5))
        self.grid[0][2] = bishop("black", (0, 2))

        # white queen starting spot
        self.grid[7][3] = queen("white", (7, 3))

        # black queen starting spot
        self.grid[0][3] = queen("black", (0, 3))

        # white king starting spot
        self.grid[7][4] = king("white", (7, 4))

        # black king starting spot
        self.grid[0][4] = king("black", (0, 4))


    def board_display(self):
        for row in self.grid:
            for column in row:
                if column != None:
                    print(column.display(), end = " ")
                else:
                    print(".", end = " ")
            print()

    def move_piece(self,):

        from_pos = input("Which piece do you want to move(row colum)?: ")
        from_pos = tuple(int(i) for i in from_pos.split())

        to_pos = input("Where do you want to move it (row column)?: ")
        to_pos = tuple(int(i) for i in to_pos.split())
        
        
        piece = self.grid[from_pos[0]][from_pos[1]]
        valid_moves = piece.movement(self)
        if to_pos in valid_moves:
            self.grid[to_pos[0]][to_pos[1]] = piece
            piece.position = to_pos
            self.grid[from_pos[0]][from_pos[1]] = None
            self.board_display()
        else:
            print("Invalid move, try again")
    

    

        

