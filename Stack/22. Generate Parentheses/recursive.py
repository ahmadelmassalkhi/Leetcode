class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==0:
            return []
        result = []
        def generate(open, close, s): # open/close = number of open/close brackets left
            if open==0 and close==0:
                result.append(s)
                return                
            if open > 0: # no restrictions on open brackets
                generate(open-1, close, s+"(")
            if close > 0 and close>open: # only add if exists an open bracket without a closing
                generate(open, close-1, s+")")
        generate(n, n, "")
        return result
    
print(Solution().generateParenthesis(3))