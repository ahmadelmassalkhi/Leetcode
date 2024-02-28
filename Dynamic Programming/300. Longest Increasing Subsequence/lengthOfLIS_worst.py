class Solution(object):

    def __init__(self):
        self.d = {}

    def helper(self, nums, idx):
        if idx == len(nums)-1:
            return 1
        length = 1
        for i in range(idx+1, len(nums)):
            if nums[idx] < nums[i]:
                if i not in self.d:
                    self.d[i] = self.helper(nums, i)
                l = 1 + self.d[i]
                length = max(length, l)
        self.d[idx] = length
        return length

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 1
        self.d = {}
        for i in range(0, len(nums)):
            res = max(res, self.helper(nums, i))
        return res


nums = [10,9,2,5,3,7,101,18]
print(Solution().lengthOfLIS(nums))