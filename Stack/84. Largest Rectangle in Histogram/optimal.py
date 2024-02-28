
# beats 98.88% (time complexity)

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # sequence stops when lesser rectangle is reached
        # to calculate the width, we store indices, then subtract them (stop - start)
        max_area = 0
        stack = []

        for i,h in enumerate(heights):
            if not stack or stack[-1][1]<h:
                stack.append((i, h))
                continue
            if stack[-1][1] == h:
                continue
            start = i
            while stack and stack[-1][1]>h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i-idx))
                start = idx
            stack.append((start, h))

        # all remaining rectangles are in increasing order
        while stack:
            idx, height = stack.pop()
            max_area = max(max_area, height * (len(heights)-idx))

        return max_area
    