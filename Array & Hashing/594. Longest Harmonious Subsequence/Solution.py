import collections

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # since the difference must be exactly 1
        # the sequences accepted will contain only consecutive numbers (two numbers, 1 2, 2 3, 3 4...)
        # so the sequences accepted are at least 2 elements (if no duplicates)
        # to account for duplicates we compute the frequencies
        freq = collections.Counter(nums)
        
        maxSeq = 0
        for num in nums:
            if num-1 in freq: # consecutive => exists an accepted sequence of their sum(freq)
                maxSeq = max(maxSeq, freq[num]+freq[num-1])
        return maxSeq