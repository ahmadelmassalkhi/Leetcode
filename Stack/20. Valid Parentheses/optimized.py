









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
        open_brackets = set(d.keys())

        stack = []
        for c in s:
            if c in open_brackets:
                stack.append(c)
            elif not stack or c!=d[stack.pop()]:
                return False
        return not stack