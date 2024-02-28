

# too slow - O(n^2)

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height = [(i, height[i]) for i in range(len(height))]
        height = sorted(height, key = lambda x : x[1])

        max_area = 0
        for new_i, (i,h) in enumerate(height):
            for j in range(new_i+1, len(height)): # all heights after h, are greater=>
                area = abs(height[j][0]-i) * h
                max_area = max(max_area, area)
        return max_area