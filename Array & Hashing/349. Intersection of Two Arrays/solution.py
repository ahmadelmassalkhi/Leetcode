class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {v: False for v in nums1}
        result = []
        for i in nums2:
            if i in d and not d[i]:
                d[i] = True
                result.append(i)
        return result