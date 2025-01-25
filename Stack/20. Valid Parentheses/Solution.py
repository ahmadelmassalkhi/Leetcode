class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        symbols = {'(':')', '{':'}', '[':']'}
        stack = []
        
        for c in s:
            if c in symbols:
                stack.append(c)
            else:
                if not stack or c!=symbols[stack.pop()]: return False
        
        return len(stack)==0