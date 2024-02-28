

import collections
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # get frequency of each number
        freq = collections.defaultdict(int)
        for i in nums:
            freq[i] += 1

        # store them in a max-heap (max frequency on top)
        heap = []
        for key in freq.keys():
            heapq.heappush(heap, (-freq[key], key)) # -ve because default is min-heap
        
        # get top k elements from heap
        l = 0
        result = []
        while heap and l<k:
            result.append(heapq.heappop(heap)[1])
            l+=1
        return result


print(Solution().topKFrequent([1,1,1,2,2,3], 2))
