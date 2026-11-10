## 2026-10-25

- Built: restructured my project with the chess_engine/ and tests/ folders. I also made my first ever pytests
- Broke: Ran into a ModuleNotFoundError becuase I forgot about the pytest.ini file needed to run tests. Also struggled with the setup and writing my first tests, but that will become better with more reps.
- Next Session: Write another test for a knight in the center of the board and a pawn in front of the king to check for bugs. Then start the move_piece split.

## 2026-10-26

Session 1:

- Built: Added more pytests one for knight movement logic and two for pawn check detection logic
- Broke: Mismatched the coordinates on my board when creating the piece objects. Always make sure to assert opposite behavior at first and make sure a test can fail before trusting it.
- next session: Figure out a plan on how I am going to refactor my code and start expanding on project.

Session 2:

- Built: reorganized folder structure moving old chess_engine and tests into legacy/ and made a new git branch with a new chess_engine and tests to start rewriting the old code to make it better.
- Broke: I struggled with creating the branch and ideas behind it, but figured it out and learned why branches are so good for production especially in a team environment. I also learned the differences between a dict and list of lists in the context of a chess board and came to the conclusion that I will be sticking to a 2d list so that it is easier to visualize.
- Next Session: I will write out the 2d array for the board and write pytests for it to make sure it is working properly and that it stands alone. Then after that I will start to reimplement the board features, but with much better and organized code this time.

## 2026-10-31

- Built: setup the 8x8 grid for the chess board in our new rewrite branch. Ran a test to make sure every square contains None and it passed.
- Learned: I misunderstood list comprehension for this scenario and had the wrong visual in my head, after getting the test working and following it through I got the right visual down of 1[1, 2, 3, ...], 2[1, 2, 3, ...], and so on.
- Next Session: Build out the get() and place() methods. get will be the read method for the board and place will be the write method for the board.

## 2026-11-1

- Built: Started the setup for the get() and place() methods to read and write on a square for our Board class. Wrote a test for each method and made sure it failed properly.
- Next Session: Finalize these methods and begin planning for next steps

## 2026-11-02

- Built: Built and tested the get() and place() methods for the Board class. Also have board setup like a normal graph now where inputs are x, y or col, row and (0, 0) is the bottom left of the board.
- Next Session: Build a system that raises and error for negative indexes into the grid and start the Piece class in a new piece.py file

## 2026-11-09

- Built: Added a helper method and tests for detecting if the input coordinates are outside the bounds of the grid for the chess board. Also made a custom error OffBoardError in errors.py if this is raised.
- Next Session: Add tests for place using the helper method. Then start piece.py

## 2026-11-10

- Built: Added tests for the corner boundaries making sure we can read and write to them without issue. Also added tests to make sure place raises the OffBoardError when calling it outside the boundaries of the board.
- Next: Begin piece.py to start logic for piece classes
