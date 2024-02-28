class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==0:
            return []
        result = []
        stack = [(n-1, n, "(")]
        while stack:
            open, close, s = stack.pop() # open/close = number of open/close brackets left
            if open==0 and close==0:
                result.append(s)
            if open > 0: # no restrictions on open brackets
                stack.append((open-1, close, s+"("))
            if close > 0 and close > open: # only add if exists an open bracket without a closing
                stack.append((open, close-1, s+")"))
        return result
    
print(Solution().generateParenthesis(3))

        