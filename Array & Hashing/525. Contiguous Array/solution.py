class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0 # ones - zeroes
        
        max_l = 0
        count_map = {0 : -1}
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            
            # if `count` encountered AGAIN
            # => number of 1s & 0s inbetween i and first index of `count` is equal
            # (since we want maximum length subarray we do not override first index of `count`)
            if count in count_map:
                max_l = max(max_l, i - count_map[count])
            else:
                count_map[count] = i
        return max_l