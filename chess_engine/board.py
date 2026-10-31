class Board:
    # board contructor    
    def __init__(self):
        self.grid = [[None for row in range(8)] for column in range(8)]