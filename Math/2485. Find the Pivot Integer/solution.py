class Solution(object):
    def sum_of_naturals(self, n):
        return n * (n + 1) / 2

    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0
        sum_to_n = self.sum_of_naturals(n)
        for i in range(n):
            s += i+1
            if s == sum_to_n-s+(i+1):
                return i+1
        return -1