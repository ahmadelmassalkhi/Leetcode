
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        slow = 0 # points to a zero
        for fast in range(len(nums)):
            # skip zeroes (by fast)
            if nums[fast] == 0:
                continue

            # find a zero (by slow)
            while nums[slow]!=0 and slow<fast:
                slow+=1
                
            # didn't find any zeroes to move
            if slow==fast: 
                continue

            # swap
            (nums[slow], nums[fast]) = (nums[fast], nums[slow])
        return nums


nums = [0, 1, 0, 3, 12]
nums = [1, 3, 12, 0, 0] # already done

nums = [0, 0, 0, 0, 0] # full
nums = [1, 1, 1, 1, 1] # empty

print(Solution().moveZeroes(nums))



        