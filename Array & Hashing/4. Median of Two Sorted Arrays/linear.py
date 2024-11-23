# linear time complexity: O(m+n)

class Solution(object):

    def sort(self, nums1, nums2):
        result = []
        i = j = 0
        while i<len(nums1) or j<len(nums2):
            if i<len(nums1) and j<len(nums2):
                result.append(min(nums1[i], nums2[j]))
                if nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1
            elif i<len(nums1):
                result.append(nums1[i])
                i+=1
            else:
                result.append(nums2[j])
                j+=1
        return result


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = self.sort(nums1, nums2)
        n = len(merged)
        mid = n / 2

        if n % 2:
            return merged[mid]
        return (merged[mid-1] + merged[mid]) / 2.0