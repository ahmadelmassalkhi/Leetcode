




class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [1] * n

        # Calculate left products
        product_left = 1
        for i in range(n):
            result[i] *= product_left
            product_left *= nums[i]

        # Calculate right products
        product_right = 1
        for i in range(n - 1, -1, -1):
            result[i] *= product_right
            product_right *= nums[i]

        return result
