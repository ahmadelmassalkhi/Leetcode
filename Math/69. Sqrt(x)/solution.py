class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0 or x==1: return x
        i = 2
        while True:
            if i*i == x: return i
            if i*i > x: return i-1
            i += 1
