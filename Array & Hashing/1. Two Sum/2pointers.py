


'''
    Time Complexity: O(n log n)
        The dominating factor is the sorting step, which has a time complexity of O(n log n).
        The subsequent two-pointer traversal is O(n), but it is overshadowed by the sorting.
    Space Complexity: O(n)
        Additional space is required for the sorted list of tuples.
'''



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = sorted(list(enumerate(nums)), key = lambda x : x[1])
        left = 0
        right = len(nums)-1
        while left < right:
            sum = nums[left][1] + nums[right][1]
            if sum == target:
                return [nums[left][0], nums[right][0]]
            if sum < target:
                left += 1
            else:
                right -= 1 