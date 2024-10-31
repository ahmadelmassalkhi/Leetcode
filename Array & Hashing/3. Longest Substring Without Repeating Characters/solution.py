


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        longest = start = 0

        for i,c in enumerate(s):
            # If duplicate and within the current substring
            if c in d and d[c] >= start:
                # Move the start right after the last occurrence of c
                start = d[c]+1
            d[c] = i
            # Calculate max length
            longest = max(longest, i-start+1)

        return longest