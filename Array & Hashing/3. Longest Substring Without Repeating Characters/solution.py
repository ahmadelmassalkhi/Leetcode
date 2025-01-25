class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        start = longest = 0

        for i,c in enumerate(s):
            if c in d and d[c] >= start:
                start = d[c]+1
            else:
                longest = max(longest, i-start+1)
            d[c] = i

        return longest