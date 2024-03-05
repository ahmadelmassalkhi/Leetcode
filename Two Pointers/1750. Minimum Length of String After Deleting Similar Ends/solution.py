class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                break
            value = s[left]
            while left<=right and s[left] == value:
                left += 1
            while left<=right and s[right] == value:
                right -= 1
        return right-left+1