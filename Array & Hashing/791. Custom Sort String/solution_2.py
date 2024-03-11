import collections

class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        freq = collections.defaultdict(int)
        for i in s:
            freq[i] += 1
        
        result = ''
        for i in order:
            if i in freq:
                result += i * freq[i]
                freq[i] = 0

        for i in freq.keys():
            if freq[i] != 0:
                result += i * freq[i]
        
        return result