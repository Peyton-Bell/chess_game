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
        self.current_turn = "white"
        self.white_king_pos = (7, 4)
        self.black_king_pos = (0, 4)
    

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
        print(" ", end = " ")
        for i in range(8):
            print(i, end = " ")
        print()
        for i, row in enumerate(self.grid):
            print(i, end = " ")
            for column in row:
                if column != None:
                    print(column.display(), end = " ")
                else:
                    print(".", end = " ")
            print()

    def move_piece(self):

        while True:
            # Asks user which piece they are moving
            from_pos = input(f"Which {self.current_turn} piece do you want to move(row colum)?: ")
            from_pos = tuple(int(i) for i in from_pos.split())

            # variables for logic
            piece = self.grid[from_pos[0]][from_pos[1]]
            valid_moves = piece.movement(self)

            # checks the color of the piece
            if piece.color == self.current_turn:
                
                # asks where they want to move the piece
                to_pos = input("Where do you want to move it (row column)?: ")
                to_pos = tuple(int(i) for i in to_pos.split())

                # checks to make sure destination is in valid moves list
                if to_pos in valid_moves:
                    self.grid[to_pos[0]][to_pos[1]] = piece
                    piece.position = to_pos
                    self.grid[from_pos[0]][from_pos[1]] = None
                    self.board_display()
                    if isinstance(piece, king):
                        if piece.color == "white":
                            self.white_king_pos = to_pos
                        if piece.color == "black":
                            self.black_king_pos = to_pos

                    # changes the current turn to the opposite color for next turn
                    if self.current_turn == "white":
                        self.current_turn = "black"
                        break
                    else:
                        self.current_turn = "white"
                        break

                # tells user is move is invalid
                else:
                    print("Invalid move, try again")

            # if not the same color, it tells user
            else:
                print(f"You must move a {self.current_turn} colored piece")
    
    def in_check(self):

        # make empty lists to store all valid moves for a single color
        white_valid_moves = []
        black_valid_moves = []

        # adds all valid moves to white and black lists
        for row in self.grid:
            for column in row:
                if column != None:
                    if column.color == "white":
                        white_valid_moves.extend(column.movement(self))
                    if column.color == "black":
                        black_valid_moves.extend(column.movement(self))

        # checks if king pos is in valid moves for opposite color
        if self.white_king_pos in black_valid_moves:
            print("white is in check")
            return "white"
        if self.black_king_pos in white_valid_moves:
            print("black is in check")
            return "black"
