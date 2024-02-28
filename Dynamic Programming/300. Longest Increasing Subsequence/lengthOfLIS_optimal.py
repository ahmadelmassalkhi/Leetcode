from bisect import bisect_left


class Solution(object):

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = [nums[0]]
        for num in nums[1:]:
            if num < s[0]:
                s[0] = num
            elif num > s[-1]:
                s.append(num)
            else:
                s[bisect_left(s, num)] = num
        return len(s)
    

nums = [0,1,0,3,2,3]
print(Solution().lengthOfLIS(nums))