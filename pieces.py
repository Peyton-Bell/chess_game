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
            if self.position[1] == 1:
                forward_one_sqaure = (self.position[0], self.position[1] + 1)
                forward_two_sqaures = (self.position[0], self.position[1] + 2)
                valid_moves_pawn.append(forward_one_sqaure)
                valid_moves_pawn.append(forward_two_sqaures)
                return valid_moves_pawn
            else:
                forward_one_sqaure = (self.position[0], self.position[1] + 1)
                valid_moves_pawn.append(forward_one_sqaure)
                return valid_moves_pawn
            

            # Movement for Black
        if self.color != "white":
            if self.position[1] == 6:
                forward_one_sqaure = (self.position[0], self.position[1] - 1)
                forward_two_sqaures = (self.position[0], self.position[1] - 2)
                valid_moves_pawn.append(forward_one_sqaure)
                valid_moves_pawn.append(forward_two_sqaures)
                return valid_moves_pawn
            else:
                forward_one_sqaure = (self.position[0], self.position[1] - 1)
                valid_moves_pawn.append(forward_one_sqaure)
                return valid_moves_pawn

class bishop(piece):
    def __init__ (self, color, position):
        super().__init__(color, position)
    
    # displays the P letter for each bishop
    def display(self):
        if self.color == "white":
            return "B" #display B for white
        return "b" # display b for black
    
    # movement mechanics for the bishop
    def movement(self, board):
        # empty list for all valid moves
        valid_moves_bishop = []
        #temporary position variables
        current_x = self.position[0]
        current_y = self.position[1]

        # tracks diagonal up to the right movement
        while current_x < 7 and current_y < 7:
            current_x += 1
            current_y += 1
            valid_moves_bishop.append((current_x, current_y))

        # tracks diagonal down to the left movement
        current_x = self.position[0]
        current_y = self.position[1]
        while current_x > 0 and current_y > 0:
            current_x -= 1
            current_y -= 1
            valid_moves_bishop.append((current_x, current_y))

        # tracks diagonal up to the left movement
        current_x = self.position[0]
        current_y = self.position[1]
        while current_x > 0 and current_y < 7:
            current_x -= 1
            current_y += 1
            valid_moves_bishop.append((current_x, current_y))

        # tracks diagonal down to the right movement
        current_x = self.position[0]
        current_y = self.position[1]
        while current_x < 7 and current_y > 0:
            current_x += 1
            current_y -= 1
            valid_moves_bishop.append((current_x, current_y))
        
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

        #create emtpy list of valid moves
        valid_moves_rook = []
        #temporary x and y values
        current_x = self.position[0]
        current_y = self.position[1]


        # all moves up
        while current_y < 7:
            current_y += 1
            valid_moves_rook.append((current_x, current_y))


        # all moves down
        current_x = self.position[0]
        current_y = self.position[1]
        while current_y > 0:
            current_y -= 1
            valid_moves_rook.append((current_x, current_y))

        # all moves right
        current_x = self.position[0]
        current_y = self.position[1]
        while current_x < 7:
            current_x += 1
            valid_moves_rook.append((current_x, current_y))

        # all moves left
        current_x = self.position[0]
        current_y = self.position[1]
        while current_x > 0:
            current_x -= 1
            valid_moves_rook.append((current_x, current_y))

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

        # up 1
        if self.position[1] < 7:
            valid_moves_king.append((self.position[0], self.position[1] + 1))

        # down 1
        if self.position[1] > 0:
            valid_moves_king.append((self.position[0], self.position[1] - 1))

        # left 1
        if self.position[0] > 0:
            valid_moves_king.append((self.position[0] - 1, self.position[1]))

        # right 1
        if self.position[0] < 7:
            valid_moves_king.append((self.position[0] + 1, self.position[1]))

        # up and right 1
        if self.position[0] < 7 and self.position[1] < 7:
            valid_moves_king.append((self.position[0] + 1, self.position[1] + 1))

        # up and left 1
        if self.position[0] > 0 and self.position[1] < 7:
            valid_moves_king.append((self.position[0] - 1, self.position[1] + 1))

        # down and right 1
        if self.position[0] < 7 and self.position[1] > 0:
            valid_moves_king.append((self.position[0] + 1, self.position[1] - 1))

        # down and left 1
        if self.position[0] > 0 and self.position[1] > 0:
            valid_moves_king.append((self.position[0] - 1, self.position[1] - 1))

        return valid_moves_king

class queen(piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    #display for queen
    def display(self):
        if self.color == "white":
            return "Q" #display Q for white
        return "q" # display q for black
    
    # movement for queen
    def movement(self, board):
        # empty list for valid moves
        valid_moves_queen = []

        # temporary values for x and y
        current_x = self.position[0]
        current_y = self.position[1]

        # all moves up
        while current_y < 7:
            current_y += 1
            valid_moves_queen.append((current_x, current_y))


        # all moves down
        current_x = self.position[0]
        current_y = self.position[1]
        while current_y > 0:
            current_y -= 1
            valid_moves_queen.append((current_x, current_y))

        # all moves right
        current_x = self.position[0]
        current_y = self.position[1]
        while current_x < 7:
            current_x += 1
            valid_moves_queen.append((current_x, current_y))

        # all moves left
        current_x = self.position[0]
        current_y = self.position[1]
        while current_x > 0:
            current_x -= 1
            valid_moves_queen.append((current_x, current_y))

        # tracks diagonal up to the right movement
        current_x = self.position[0]
        current_y = self.position[1]
        while current_x < 7 and current_y < 7:
            current_x += 1
            current_y += 1
            valid_moves_queen.append((current_x, current_y))

        # tracks diagonal down to the left movement
        current_x = self.position[0]
        current_y = self.position[1]
        while current_x > 0 and current_y > 0:
            current_x -= 1
            current_y -= 1
            valid_moves_queen.append((current_x, current_y))

        # tracks diagonal up to the left movement
        current_x = self.position[0]
        current_y = self.position[1]
        while current_x > 0 and current_y < 7:
            current_x -= 1
            current_y += 1
            valid_moves_queen.append((current_x, current_y))

        # tracks diagonal down to the right movement
        current_x = self.position[0]
        current_y = self.position[1]
        while current_x < 7 and current_y > 0:
            current_x += 1
            current_y -= 1
            valid_moves_queen.append((current_x, current_y))
        
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

        # up 2 right 1
        if self.position[0] < 7 and self.position[1] < 6:
            valid_moves_knight.append((self.position[0] + 1, self.position[1] + 2))

        # up 2 left 1
        if self.position[0] > 0 and self.position[1] < 6:
            valid_moves_knight.append((self.position[0] - 1, self.position[1] + 2))

        # down 2 right 1
        if self.position[0] < 7 and self.position[1] > 1:
            valid_moves_knight.append((self.position[0] + 1, self.position[1] - 2))

        # down 2 left 1
        if self.position[0] > 0 and self.position[1] > 1:
            valid_moves_knight.append((self.position[0] - 1, self.position[1] - 2))

        # right 2 up 1
        if self.position[0] < 6 and self.position[1] < 7:
            valid_moves_knight.append((self.position[0] + 2, self.position[1] + 1))

        # right 2 down 1
        if self.position[0] < 6 and self.position[1] > 0:
            valid_moves_knight.append((self.position[0] + 2, self.position[1] - 1))

        # left 2 up 1
        if self.position[0] > 1 and self.position[1] < 7:
            valid_moves_knight.append((self.position[0] - 2, self.position[1] + 1))

        # left 2 down 1
        if self.position[0] > 1 and self.position[1] > 0:
            valid_moves_knight.append((self.position[0] - 2, self.position[1] - 1))

        return valid_moves_knight