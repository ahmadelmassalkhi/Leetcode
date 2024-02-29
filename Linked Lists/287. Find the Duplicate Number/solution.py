class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        for number in nums:
            if number in seen:
                return number
            seen.add(number)
