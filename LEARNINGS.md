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
