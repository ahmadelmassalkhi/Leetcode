class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i,num in enumerate(nums):
            nums[i] *= num
        nums.sort()
        return nums