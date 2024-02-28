



class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {
            '[':']',
            '{':'}',
            '(':')'
        }

        stack = []
        for c in s:
            if c in d: # open bracket
                stack.append(c)
            elif stack and d[stack[-1]]==c: # matching
                stack.pop() # pop the matched open bracket
            else:
                return False # not matching
        return not stack
    