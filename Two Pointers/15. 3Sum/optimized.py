class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i>0 and a==nums[i-1]: # comparing with previous copy, because it might exist a solution [a, a, c] 
                continue             # if we compare with next, we skip counting this solution
            l = i+1
            r = len(nums)-1
            while l<r:
                threeSum = a + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([a, nums[l], nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    l+=1
                elif threeSum < 0:
                    l+=1
                else:
                    r-=1
        return res

nums = [-2,0,1,1,2]
print(Solution().threeSum(nums))