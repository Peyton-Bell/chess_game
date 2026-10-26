## 2026-10-25

- Built: restructured my project with the chess_engine/ and tests/ folders. I also made my first ever pytests
- Broke: Ran into a ModuleNotFoundError becuase I forgot about the pytest.ini file needed to run tests. Also struggled with the setup and writing my first tests, but that will become better with more reps.
- Next Session: Write another test for a knight in the center of the board and a pawn in front of the king to check for bugs. Then start the move_piece split.

## 2026-10-26

- Built: Added more pytests one for knight movement logic and two for pawn check detection logic
- Broke: Mismatched the coordinates on my board when creating the piece objects. Always make sure to assert opposite behavior at first and make sure a test can fail before trusting it.
- next session: Figure out a plan on how I am going to refactor my code and start expanding on project.
