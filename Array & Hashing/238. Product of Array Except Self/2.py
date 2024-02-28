



# uses 1 loop and 1 array


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        result = [1] * n
        product_left = product_right = 1
        left = 1
        right = n-2

        while left<n and right>=0:
            product_left *= nums[left-1]
            product_right *= nums[right+1]
            
            result[left] *= product_left
            result[right] *= product_right

            left+=1
            right-=1
        return result