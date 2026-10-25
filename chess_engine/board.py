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
        self.white_king_pos = None
        self.black_king_pos = None
        self.white_king_moved = False
        self.black_king_moved = False
        self.white_kingside_rook_moved = False
        self.black_kingside_rook_moved = False
        self.white_queenside_rook_moved = False
        self.black_queenside_rook_moved = False
        # make empty lists to store all valid moves for a single color
        self.white_valid_moves = []
        self.black_valid_moves = []
      
    
    def update_kings_pos(self):
        for row in self.grid:
            for piece in row:
                if isinstance (piece, king):
                    if piece.color == "white":
                        self.white_king_pos = piece.position
                    if piece.color == "black":
                        self.black_king_pos = piece.position
                    
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
        self.update_kings_pos()

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
            try:
                from_pos = tuple(int(i) for i in from_pos.split())
            except ValueError:
                print("Invalid input, please enter 2 numbers separated by a space.")
                continue


            # variables for logic
            try:
                piece = self.grid[from_pos[0]][from_pos[1]]
                try:
                    valid_moves = piece.movement(self)
                except AttributeError:
                    print("There is no piece on that square.")
                    continue
            except IndexError:
                print("Invalid input, please enter 2 numbers 0-7 separated by a space.")
                continue


            # checks the color of the piece
            if piece.color == self.current_turn:
                
                # asks where they want to move the piece
                to_pos = input("Where do you want to move it (row column)?: ")

                try:
                    to_pos = tuple(int(i) for i in to_pos.split())
                except ValueError:
                    print("Invalid input, please enter 2 numbers 0-7 separated by a space.")
                    continue
                try:
                    old_piece = self.grid[to_pos[0]][to_pos[1]]
                except:
                    print("Invalid input, please enter 2 numbers 0-7 separated by a space.")

                # checks to make sure destination is in valid moves list
                if to_pos in valid_moves:
                    self.grid[to_pos[0]][to_pos[1]] = piece
                    piece.position = to_pos
                    self.grid[from_pos[0]][from_pos[1]] = None
                    self.update_kings_pos()

                    # checks for if castling is still available

                    # white king
                    if from_pos == (7, 4):
                        self.white_king_moved = True

                    # white kingside rook
                    if from_pos == (7, 7):
                        self.white_kingside_rook_moved = True

                    # white queenside rook
                    if from_pos == (7, 0):
                        self.white_queenside_rook_moved = True
                    
                    # black king
                    if from_pos == (0, 4):
                        self.black_king_moved = True
                    
                    # black kingside rook
                    if from_pos == (0, 7):
                        self.black_kingside_rook_moved = True

                    # black queenside rook
                    if from_pos == (0, 0):
                        self.black_queenside_rook_moved = True

                    # moves rook if castling happened
                    # white castling
                    if isinstance (piece, king) and piece.color == "white":
                        kingside_rook = self.grid[7][7]
                        queenside_rook = self.grid[7][0]
                        # kingside
                        if to_pos == (7, 6):
                            kingside_rook.position = (7, 5)
                            self.grid[7][5] = kingside_rook
                            self.grid[7][7] = None
                        # queenside
                        if to_pos == (7, 2):
                            queenside_rook.position = (7, 3)
                            self.grid[7][3] = queenside_rook
                            self.grid[7][0] = None
                    # black castling
                    if isinstance (piece, king) and piece.color == "black":
                        kingside_rook = self.grid[0][7]
                        queenside_rook = self.grid[0][0]
                        # kingside
                        if to_pos == (0, 6):
                            kingside_rook.position = (0, 6)
                            self.grid[0][5] = kingside_rook
                            self.grid[0][7] = None
                        # queenside
                        if to_pos == (0, 2):
                            queenside_rook.position = (0, 2)
                            self.grid[0][3] = queenside_rook
                            self.grid[0][0] = None
                            


                    # helps figure out if en passant is allowed
                    row_diff = abs(to_pos[0] - from_pos[0])
                    col_diff = abs(to_pos[1] - from_pos[1])

                    # checks for en passant
                    if isinstance (piece, pawn) and row_diff == 2:
                        self.last_move = (pawn, to_pos)
                    else:
                        self.last_move = None

                    # removes pawn when en passant happens
                    if isinstance (piece, pawn) and col_diff == 1 and old_piece == None:
                        if piece.color == "white":
                            self.grid[to_pos[0] + 1][ to_pos[1]] = None
                        if piece.color == "black":
                            self.grid[to_pos[0] - 1][ to_pos[1]] = None



                    # makes sure kings aren't next to eachother
                    king_row_diff = abs(self.white_king_pos[0] - self.black_king_pos[0])
                    king_col_diff = abs(self.white_king_pos[1] - self.black_king_pos[1])
                    if king_row_diff <= 1 and king_col_diff <= 1:
                        self.grid[from_pos[0]][from_pos[1]] = piece
                        piece.position = from_pos
                        self.grid[to_pos[0]][to_pos[1]] = old_piece
                        print("You can't move kings next to eachother.")
                        continue

                    # checks if you are still in check
                    check_status = self.in_check()
                    if check_status == self.current_turn:
                        self.grid[from_pos[0]][from_pos[1]] = piece
                        piece.position = from_pos
                        self.grid[to_pos[0]][to_pos[1]] = old_piece
                        print("You are still in check, that move is invalid.")
                        continue

                    # checks if you put the king in check 
                    elif check_status == "white":
                        if self.in_checkmate() == True:
                            print("Black wins!")
                            exit()
                        else:
                            print("White is in check!")
                    elif check_status == "black":
                        if self.in_checkmate() == True:
                            print("White wins!")
                            exit()
                        else:
                            print("Black is in check!")


                    # prints updated board display
                    self.board_display()

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

        self.white_valid_moves = []
        self.black_valid_moves = []

        # adds all valid moves to white and black lists
        for row in self.grid:
            for column in row:
                if column != None:
                    if column.color == "white":
                        self.white_valid_moves.extend(column.movement(self))
                    if column.color == "black":
                        self.black_valid_moves.extend(column.movement(self))

        # checks if king pos is in valid moves for opposite color
        if self.white_king_pos in self.black_valid_moves:
            return "white"
        if self.black_king_pos in self.white_valid_moves:
            return "black"

    def in_checkmate(self):

        # checks if someone is in check or not
        check_status = self.in_check()
        if check_status is None:
            return False

        # iterate over every piece
        for row in self.grid:
            for piece in row:
                if piece != None:

                    # run every move for each white piece
                    if piece.color == "white" and check_status == "white":
                        for move in piece.movement(self):                      
                            # run the move
                            from_pos = piece.position
                            to_pos = move
                            old_piece = self.grid[to_pos[0]][to_pos[1]]
                            self.grid[to_pos[0]][to_pos[1]] = piece
                            piece.position = to_pos
                            if isinstance (piece, king):
                                self.white_king_pos = to_pos
                            self.grid[from_pos[0]][from_pos[1]] = None


                            # check if move got them out of check
                            if self.in_check() is None:
                                self.grid[from_pos[0]][from_pos[1]] = piece
                                piece.position = from_pos
                                if isinstance (piece, king):
                                    self.white_king_pos = from_pos
                                self.grid[to_pos[0]][to_pos[1]] = old_piece
                                return False
                            else:
                                self.grid[from_pos[0]][from_pos[1]] = piece
                                piece.position = from_pos
                                if isinstance (piece, king):
                                    self.white_king_pos = from_pos
                                self.grid[to_pos[0]][to_pos[1]] = old_piece
                                continue
                    
                    # do same logic for black
                    if piece.color == "black" and check_status == "black":
                        for move in piece.movement(self):                      
                            # run the move
                            from_pos = piece.position
                            to_pos = move
                            old_piece = self.grid[to_pos[0]][to_pos[1]]
                            self.grid[to_pos[0]][to_pos[1]] = piece
                            piece.position = to_pos
                            if isinstance (piece, king):
                                self.black_king_pos = to_pos
                            self.grid[from_pos[0]][from_pos[1]] = None

                            # check if move got them out of check
                            if self.in_check() is None:
                                self.grid[from_pos[0]][from_pos[1]] = piece
                                piece.position = from_pos
                                if isinstance (piece, king):
                                    self.black_king_pos = from_pos
                                self.grid[to_pos[0]][to_pos[1]] = old_piece
                                return False
                            else:
                                self.grid[from_pos[0]][from_pos[1]] = piece
                                piece.position = from_pos
                                if isinstance (piece, king):
                                    self.black_king_pos = from_pos
                                self.grid[to_pos[0]][to_pos[1]] = old_piece
                                continue
        return True

                            



