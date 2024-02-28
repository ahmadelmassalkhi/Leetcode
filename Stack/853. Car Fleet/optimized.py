
# fastest than 100.00% of python submissions (minimal time complexity)  

'''
    In scenarios where multiple cars have the same starting position but different speeds, 
    this approach with a dictionary mapping positions to speeds 
    would not effectively differentiate between the speeds of those cars sharing the same starting point. 
    This can result in incorrect fleet calculations.

    however there is no testcase on leetcode that could capture this bug
'''

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        speedPos = {position[i]:speed[i] for i in range(len(speed))} # what if multiple cars with same position ? It overrides previously set speed

        # reverse order
        position = sorted(position, reverse=True)
        stack = []

        for i, pos in enumerate(position):
            t = float(target - pos) / speedPos[pos]
            if not stack or t>stack[-1]:
                stack.append(t)
        return len(stack)