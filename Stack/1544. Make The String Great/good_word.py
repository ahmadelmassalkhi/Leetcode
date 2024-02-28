



class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for c in s:
            if result and result[-1]!=c and (result[-1].upper()==c or result[-1].lower()==c):
                result.pop()
                continue
            result.append(c)
        return ''.join(result)
        

print(Solution().makeGood("leEeetcode"))
