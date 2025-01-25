class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i,num in enumerate(nums):
            if num in d:
                return [i, d[num]]
            d[target-num] = i