





class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_l = 0 # initial max length
        s = set(nums) # remove duplicates
        for num in s: 
            if num-1 not in s:
                l = 1
                while num+l in s:
                    l+=1
                max_l = max(max_l, l)
        return max_l
                
        