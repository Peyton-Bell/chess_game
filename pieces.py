# classes for all the chess pieces

# base piece class all others inherit from
class piece:
    def __init__ (self, color, position):
        self.color = color
        self.position = position


# Pawn class
class pawn(piece):
    def __init__ (self, color, position):
        super().__init__(color, position)

    # displays the P letter for each pawn
    def display(self):
        if self.color == "white":
            return "P" #display P for white
        return "p" # display p for black
        
    # method for all movement of the pawn
    def movement(self, board):
        # empty list for all valid moves
        valid_moves_pawn = []

        # Movement for White
        if self.color == "white":

            # First move logic for white
            if self.position[0] == 6:
                forward_one_square = (self.position[0] - 1, self.position[1])

                # checks if piece is in front of pawn
                if board.grid[self.position[0] - 1][self.position[1]] == None:
                    valid_moves_pawn.append(forward_one_square)               
                    forward_two_squares = (self.position[0] - 2, self.position[1])

                    # checks if piece is 2 spaces in front of pawn on first move
                    if board.grid[self.position[0] - 2][self.position[1]] == None:
                        valid_moves_pawn.append(forward_two_squares)
                return valid_moves_pawn
            
            # movement logic for white pawn when not first move
            else:
                forward_one_square = (self.position[0] - 1, self.position[1])
                # checks if piece is in front of pawn
                if board.grid[self.position[0] - 1][self.position[1]] == None:
                    valid_moves_pawn.append(forward_one_square)               
                
            
            # taking logic for white pawns
            if self.position[0] < 7 and self.position[1] < 7:
                if board.grid[self.position[0] - 1][self.position[1] + 1] != None:
                    if board.grid[self.position[0] - 1][self.position[1] + 1].color == "black":
                        valid_moves_pawn.append((self.position[0] - 1, self.position[1] + 1))
            if self.position[0] < 7 and self.position[1] > 0:
                if board.grid[self.position[0] - 1][self.position[1] - 1] != None:
                    if board.grid[self.position[0] - 1][self.position[1] - 1].color == "black":
                        valid_moves_pawn.append((self.position[0] - 1, self.position[1] - 1))

                return valid_moves_pawn

        # Movement for Black
        if self.color == "black":

            # First move logic for Black
            if self.position[0] == 1:
                forward_one_square = (self.position[0] + 1, self.position[1])

                # checks if piece is in front of pawn
                if board.grid[self.position[0] + 1][self.position[1]] == None:
                    valid_moves_pawn.append(forward_one_square)               
                    forward_two_squares = (self.position[0] + 2, self.position[1])

                    # checks if piece is 2 spaces in front of pawn on first move
                    if board.grid[self.position[0] + 2][self.position[1]] == None:
                        valid_moves_pawn.append(forward_two_squares)
                return valid_moves_pawn
            
            # movement logic for black pawn when not first move
            else:
                forward_one_square = (self.position[0] + 1, self.position[1])
                # checks if piece is in front of pawn
                if board.grid[self.position[0] + 1][self.position[1]] == None:
                    valid_moves_pawn.append(forward_one_square)               

            # taking logic for black pawns
            if self.position[0] < 7 and self.position[1] < 7:
                if board.grid[self.position[0] + 1][self.position[1] + 1] != None:
                    if board.grid[self.position[0] + 1][self.position[1] + 1].color == "white":
                        valid_moves_pawn.append((self.position[0] + 1, self.position[1] + 1))
            if self.position[0] < 7 and self.position[1] > 0:
                if board.grid[self.position[0] + 1][self.position[1] - 1] != None:
                    if board.grid[self.position[0] + 1][self.position[1] - 1].color == "white":
                        valid_moves_pawn.append((self.position[0] + 1, self.position[1] - 1))

                return valid_moves_pawn



class bishop(piece):
    def __init__ (self, color, position):
        super().__init__(color, position)
    
    # displays the B letter for each bishop
    def display(self):
        if self.color == "white":
            return "B" #display B for white
        return "b" # display b for black
    
    # movement mechanics for the bishop
    def movement(self, board):
        # empty list for all valid moves
        valid_moves_bishop = []

        # tracks diagonal up to the right movement (row decreases, column increases)
        current_row = self.position[0]
        current_column = self.position[1]
        while current_row > 0 and current_column < 7:
            current_row -= 1
            current_column += 1
            if board.grid[current_row][current_column] == None:
                valid_moves_bishop.append((current_row, current_column))
            elif board.grid[current_row][current_column].color == self.color:
                break
            else:
                valid_moves_bishop.append((current_row, current_column))
                break

        # tracks diagonal down to the left movement (row increases, column decreases)
        current_row = self.position[0]
        current_column = self.position[1]
        while current_row < 7 and current_column > 0:
            current_row += 1
            current_column -= 1
            if board.grid[current_row][current_column] == None:
                valid_moves_bishop.append((current_row, current_column))
            elif board.grid[current_row][current_column].color == self.color:
                break
            else:
                valid_moves_bishop.append((current_row, current_column))
                break

        # tracks diagonal up to the left movement (row decreases, column decreases)
        current_row = self.position[0]
        current_column = self.position[1]
        while current_row > 0 and current_column > 0:
            current_row -= 1
            current_column -= 1
            if board.grid[current_row][current_column] == None:
                valid_moves_bishop.append((current_row, current_column))
            elif board.grid[current_row][current_column].color == self.color:
                break
            else:
                valid_moves_bishop.append((current_row, current_column))
                break

        # tracks diagonal down to the right movement (row increases, column increases)
        current_row = self.position[0]
        current_column = self.position[1]
        while current_row < 7 and current_column < 7:
            current_row += 1
            current_column += 1
            if board.grid[current_row][current_column] == None:
                valid_moves_bishop.append((current_row, current_column))
            elif board.grid[current_row][current_column].color == self.color:
                break
            else:
                valid_moves_bishop.append((current_row, current_column))
                break
        
        # returns list of valid moves for the bishop
        return valid_moves_bishop


class rook(piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    # display for rook
    def display(self):
        if self.color == "white":
            return "R"  #display R for white
        return "r" # display r for black
    
    # movement for rook
    def movement(self, board):
        # create empty list of valid moves
        valid_moves_rook = []

        # all moves up (row decreases)
        current_row = self.position[0]
        current_column = self.position[1]
        while current_row > 0:
            current_row -= 1
            if board.grid[current_row][current_column] == None:
                valid_moves_rook.append((current_row, current_column))
            elif board.grid[current_row][current_column].color == self.color:
                break
            else:
                valid_moves_rook.append((current_row, current_column))
                break

        # all moves down (row increases)
        current_row = self.position[0]
        current_column = self.position[1]
        while current_row < 7:
            current_row += 1
            if board.grid[current_row][current_column] == None:
                valid_moves_rook.append((current_row, current_column))
            elif board.grid[current_row][current_column].color == self.color:
                break
            else:
                valid_moves_rook.append((current_row, current_column))
                break

        # all moves right (column increases)
        current_row = self.position[0]
        current_column = self.position[1]
        while current_column < 7:
            current_column += 1
            if board.grid[current_row][current_column] == None:
                valid_moves_rook.append((current_row, current_column))
            elif board.grid[current_row][current_column].color == self.color:
                break
            else:
                valid_moves_rook.append((current_row, current_column))
                break

        # all moves left (column decreases)
        current_row = self.position[0]
        current_column = self.position[1]
        while current_column > 0:
            current_column -= 1
            if board.grid[current_row][current_column] == None:
                valid_moves_rook.append((current_row, current_column))
            elif board.grid[current_row][current_column].color == self.color:
                break
            else:
                valid_moves_rook.append((current_row, current_column))
                break

        return valid_moves_rook


class king(piece):
    def __init__(self, color, position):
        super().__init__(color, position)
    
    # display for king
    def display(self):
        if self.color == "white":
            return "K" #display K for white
        return "k" # display k for black
    
    # movement for king
    def movement(self, board):
        # empty list for valid moves
        valid_moves_king = []

        # up 1 (row decreases)
        if self.position[0] > 0:
            if board.grid[self.position[0] - 1][self.position [1]] == None:
                valid_moves_king.append((self.position[0] - 1, self.position[1]))
            elif board.grid[self.position[0] - 1][self.position [1]].color != self.color:
                valid_moves_king.append((self.position[0] - 1, self.position[1]))

        # down 1 (row increases)
        if self.position[0] < 7:
            if board.grid[self.position[0] + 1][self.position [1]] == None:
                valid_moves_king.append((self.position[0] + 1, self.position[1]))
            elif board.grid[self.position[0] + 1][self.position [1]].color != self.color:
                valid_moves_king.append((self.position[0] + 1, self.position[1]))

        # left 1 (column decreases)
        if self.position[1] > 0:
            if board.grid[self.position[0]][self.position [1] - 1] == None:
                valid_moves_king.append((self.position[0], self.position[1] - 1))
            elif board.grid[self.position[0]][self.position [1] - 1].color != self.color:
                valid_moves_king.append((self.position[0], self.position[1] - 1))

        # right 1 (column increases)
        if self.position[1] < 7:
            if board.grid[self.position[0]][self.position [1] + 1] == None:
                valid_moves_king.append((self.position[0], self.position[1] + 1))
            elif board.grid[self.position[0]][self.position [1] + 1].color != self.color:
                valid_moves_king.append((self.position[0], self.position[1] + 1))

        # up and right 1
        if self.position[0] > 0 and self.position[1] < 7:
            if board.grid[self.position[0] - 1][self.position [1] + 1] == None:
                valid_moves_king.append((self.position[0] - 1, self.position[1] + 1))
            elif board.grid[self.position[0] - 1][self.position [1] + 1].color != self.color:
                valid_moves_king.append((self.position[0] - 1, self.position[1] + 1))

        # up and left 1
        if self.position[0] > 0 and self.position[1] > 0:
            if board.grid[self.position[0] - 1][self.position [1] - 1] == None:
                valid_moves_king.append((self.position[0] - 1, self.position[1] - 1))
            elif board.grid[self.position[0] - 1][self.position [1] - 1].color != self.color:
                valid_moves_king.append((self.position[0] - 1, self.position[1] - 1))

        # down and right 1
        if self.position[0] < 7 and self.position[1] < 7:
            if board.grid[self.position[0] + 1][self.position [1] + 1] == None:
                valid_moves_king.append((self.position[0] + 1, self.position[1] + 1))
            elif board.grid[self.position[0] + 1][self.position [1] + 1].color != self.color:
                valid_moves_king.append((self.position[0] + 1, self.position[1] + 1))

        # down and left 1
        if self.position[0] < 7 and self.position[1] > 0:
            if board.grid[self.position[0] + 1][self.position [1] - 1] == None:
                valid_moves_king.append((self.position[0] + 1, self.position[1] - 1))
            elif board.grid[self.position[0] + 1][self.position [1] - 1].color != self.color:
                valid_moves_king.append((self.position[0] + 1, self.position[1] - 1))

        return valid_moves_king


class queen(piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    # display for queen
    def display(self):
        if self.color == "white":
            return "Q" #display Q for white
        return "q" # display q for black
    
    # movement for queen
    def movement(self, board):
        # empty list for valid moves
        valid_moves_queen = []

        # all moves up (row decreases)
        current_row = self.position[0]
        current_column = self.position[1]
        while current_row > 0:
            current_row -= 1
            if board.grid[current_row][current_column] == None:
                valid_moves_queen.append((current_row, current_column))
            elif board.grid[current_row][current_column].color == self.color:
                break
            else:
                valid_moves_queen.append((current_row, current_column))
                break

        # all moves down (row increases)
        current_row = self.position[0]
        current_column = self.position[1]
        while current_row < 7:
            current_row += 1
            if board.grid[current_row][current_column] == None:
                valid_moves_queen.append((current_row, current_column))
            elif board.grid[current_row][current_column].color == self.color:
                break
            else:
                valid_moves_queen.append((current_row, current_column))
                break

        # all moves right (column increases)
        current_row = self.position[0]
        current_column = self.position[1]
        while current_column < 7:
            current_column += 1
            if board.grid[current_row][current_column] == None:
                valid_moves_queen.append((current_row, current_column))
            elif board.grid[current_row][current_column].color == self.color:
                break
            else:
                valid_moves_queen.append((current_row, current_column))
                break

        # all moves left (column decreases)
        current_row = self.position[0]
        current_column = self.position[1]
        while current_column > 0:
            current_column -= 1
            if board.grid[current_row][current_column] == None:
                valid_moves_queen.append((current_row, current_column))
            elif board.grid[current_row][current_column].color == self.color:
                break
            else:
                valid_moves_queen.append((current_row, current_column))
                break

        # diagonal up to the right (row decreases, column increases)
        current_row = self.position[0]
        current_column = self.position[1]
        while current_row > 0 and current_column < 7:
            current_row -= 1
            current_column += 1
            if board.grid[current_row][current_column] == None:
                valid_moves_queen.append((current_row, current_column))
            elif board.grid[current_row][current_column].color == self.color:
                break
            else:
                valid_moves_queen.append((current_row, current_column))
                break

        # diagonal down to the left (row increases, column decreases)
        current_row = self.position[0]
        current_column = self.position[1]
        while current_row < 7 and current_column > 0:
            current_row += 1
            current_column -= 1
            if board.grid[current_row][current_column] == None:
                valid_moves_queen.append((current_row, current_column))
            elif board.grid[current_row][current_column].color == self.color:
                break
            else:
                valid_moves_queen.append((current_row, current_column))
                break

        # diagonal up to the left (row decreases, column decreases)
        current_row = self.position[0]
        current_column = self.position[1]
        while current_row > 0 and current_column > 0:
            current_row -= 1
            current_column -= 1
            if board.grid[current_row][current_column] == None:
                valid_moves_queen.append((current_row, current_column))
            elif board.grid[current_row][current_column].color == self.color:
                break
            else:
                valid_moves_queen.append((current_row, current_column))
                break

        # diagonal down to the right (row increases, column increases)
        current_row = self.position[0]
        current_column = self.position[1]
        while current_row < 7 and current_column < 7:
            current_row += 1
            current_column += 1
            if board.grid[current_row][current_column] == None:
                valid_moves_queen.append((current_row, current_column))
            elif board.grid[current_row][current_column].color == self.color:
                break
            else:
                valid_moves_queen.append((current_row, current_column))
                break
        
        # returns list of valid moves for the queen
        return valid_moves_queen


class knight(piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    # display for knight
    def display(self):
        if self.color == "white":
            return "N" #display N for white
        return "n" # display n for black
    
    # movement for the knight
    def movement(self, board):
        # empty list of valid moves
        valid_moves_knight = []

        # up 2 right 1 (row decreases by 2, column increases by 1)
        if self.position[0] > 1 and self.position[1] < 7:
            valid_moves_knight.append((self.position[0] - 2, self.position[1] + 1))

        # up 2 left 1 (row decreases by 2, column decreases by 1)
        if self.position[0] > 1 and self.position[1] > 0:
            valid_moves_knight.append((self.position[0] - 2, self.position[1] - 1))

        # down 2 right 1 (row increases by 2, column increases by 1)
        if self.position[0] < 6 and self.position[1] < 7:
            valid_moves_knight.append((self.position[0] + 2, self.position[1] + 1))

        # down 2 left 1 (row increases by 2, column decreases by 1)
        if self.position[0] < 6 and self.position[1] > 0:
            valid_moves_knight.append((self.position[0] + 2, self.position[1] - 1))

        # right 2 up 1 (row decreases by 1, column increases by 2)
        if self.position[0] > 0 and self.position[1] < 6:
            valid_moves_knight.append((self.position[0] - 1, self.position[1] + 2))

        # right 2 down 1 (row increases by 1, column increases by 2)
        if self.position[0] < 7 and self.position[1] < 6:
            valid_moves_knight.append((self.position[0] + 1, self.position[1] + 2))

        # left 2 up 1 (row decreases by 1, column decreases by 2)
        if self.position[0] > 0 and self.position[1] > 1:
            valid_moves_knight.append((self.position[0] - 1, self.position[1] - 2))

        # left 2 down 1 (row increases by 1, column decreases by 2)
        if self.position[0] < 7 and self.position[1] > 1:
            valid_moves_knight.append((self.position[0] + 1, self.position[1] - 2))

        return valid_moves_knight
