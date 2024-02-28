




class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        grids = collections.defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r]) or (board[r][c] in cols[c]) or (board[r][c] in grids[(r//3, c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                grids[(r//3, c//3)].add(board[r][c])

        return True