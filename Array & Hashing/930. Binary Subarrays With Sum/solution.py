class Solution(object):

    def atMost(self, nums, goal):
        if goal < 0:
            return 0
        start = current_sum = result = 0
        for end in range(len(nums)):
            current_sum += nums[end]
            while current_sum > goal:
                current_sum -= nums[start]
                start += 1
            result += end - start + 1
        return result

    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        return self.atMost(nums, goal) - self.atMost(nums, goal-1)