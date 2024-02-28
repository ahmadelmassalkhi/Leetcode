




import collections

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # get frequency of each number
        freq = collections.defaultdict(int)
        for i in nums:
            freq[i] += 1

        # return keys sorted by most frequency
        return sorted(freq.keys(), key=lambda x:freq[x], reverse=True)[0:k]

