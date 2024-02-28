


'''
    Time Complexity: O(n)
        The loop iterates through the array once, and each dictionary operation (lookup and insertion) is typically O(1).
    Space Complexity: O(n)
        The dictionary can potentially store all elements in the worst case.
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in d:
                return [d[complement], i]
            d[num] = i
