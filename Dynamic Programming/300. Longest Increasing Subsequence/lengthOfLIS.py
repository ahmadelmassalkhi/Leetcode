class Solution(object):

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        d[len(nums)-1] = 1
        result = 1
        for i in range(len(nums)-1, -1, -1):
            d[i] = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    d[i] = max(d[i], 1+d[j])
            result = max(d[i], result)
        return result
    

nums = [0,1,0,3,2,3]
print(Solution().lengthOfLIS(nums))