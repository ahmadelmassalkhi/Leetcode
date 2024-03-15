class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1] * len(nums)
        
        l = 1
        r = len(nums)-2
        right_product = left_product = 1
        while l<len(nums) and r>=0:
            left_product *= nums[l-1]
            right_product *= nums[r+1]

            result[l] *= left_product
            result[r] *= right_product

            l += 1
            r -= 1

        return result

