class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1] * len(nums)
        
        product_left = 1
        for i in range(1, len(nums)):
            product_left *= nums[i-1]
            result[i] *= product_left
        
        product_right = 1
        for i in range(len(nums)-2, -1, -1):
            product_right *= nums[i+1]
            result[i] *= product_right

        return result