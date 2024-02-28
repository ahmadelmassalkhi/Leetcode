

# checking each valid condition separately => many for loops


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in range(len(board)):
            s = set()
            for col in range(len(board)):
                if board[row][col]!="." and board[row][col] in s:
                    return False
                s.add(board[row][col])
        
        for row in range(len(board)):
            s = set()
            for col in range(len(board)):
                if board[col][row]!="." and board[col][row] in s:
                    return False
                s.add(board[col][row])

        d = collections.defaultdict(list)
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col]==".":
                    continue
                if board[row][col] in d[(row/3, col/3)]:
                    return False
                d[(row/3, col/3)].append(board[row][col])
        return True
        

            
        