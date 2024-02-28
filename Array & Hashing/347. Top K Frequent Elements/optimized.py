



import collections
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Count frequency using Counter
        freq = collections.Counter(nums)

        print(freq)

        # Use a max heap to keep track of the top k frequent elements
        heap = [(-count, key) for key, count in freq.items()]
        heapq.heapify(heap)

        # Extract the top k elements from the heap
        result = [heapq.heappop(heap)[1] for _ in range(k)]

        return result


