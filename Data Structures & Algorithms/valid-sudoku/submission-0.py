from collections import defaultdict
from typing import List


class Solution:
    """
    You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

    Each row must contain the digits 1-9 without duplicates.
    Each column must contain the digits 1-9 without duplicates.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
    Return true if the Sudoku board is valid, otherwise return false

    Note: A board does not need to be full or be solvable to be valid.
    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        The most rudimentary way of solving this is check if
        - any of the rows has duplicate
        - any of the cols has duplicate
        - any of the [3 x 3] grids have duplicate

        Key ignore placeholder "." from input
        """

        """
        Following Code checks for both Rows and Cols
        """
        rowset = defaultdict(set)  # Key is row number
        colset = defaultdict(set)  # Key is col number
        grids = defaultdict(set)  # Key is grid (row // 3, col // 3)

        for row in range(0, 9):
            for col in range(0, 9):
                if board[row][col] == ".":
                    continue

                if (
                    board[row][col] in rowset[row]
                    or board[row][col] in colset[col]
                    or board[row][col] in grids[(row // 3, col // 3)]
                ):
                    return False

                rowset[row].add(board[row][col])
                colset[col].add(board[row][col])
                grids[(row // 3, col // 3)].add(board[row][col])

        return True


if __name__ == "__main__":
    s = Solution()
    ans = s.isValidSudoku(
        [
            ["1", "2", ".", ".", "3", ".", ".", ".", "."],
            ["4", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", ".", "3"],
            ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
            [".", ".", ".", "8", ".", "3", ".", ".", "5"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", ".", ".", ".", ".", ".", "2", ".", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "8"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
    print(ans)
