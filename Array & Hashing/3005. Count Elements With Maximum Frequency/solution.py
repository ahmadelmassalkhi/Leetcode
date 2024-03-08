class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        max_freq = 1
        for i in nums:
            if i in d:
                d[i] += 1
                max_freq = max(max_freq, d[i])
            else:
                d[i] = 1
        if max_freq == 1:
            return len(nums)
        
        count = 0
        for i in d.keys():
            if d[i] == max_freq:
                count += d[i]
        
        return count