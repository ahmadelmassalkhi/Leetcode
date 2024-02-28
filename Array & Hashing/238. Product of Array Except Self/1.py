

# inefficient because uses 3 for loops and 3 arrays


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_product = [1] * len(nums)
        for i in range(1, len(nums)):
            left_product[i] = left_product[i-1] * nums[i-1]
        
        right_product = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            right_product[i] = right_product[i+1] * nums[i+1]
        
        return [right_product[i]*left_product[i] for i in range(len(nums))]