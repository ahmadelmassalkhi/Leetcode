class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        ones = 0 #number of 1s
        for letter in s:
            if letter == "1":
                ones += 1
        zeroes = len(s) - ones
        leadingOnes = ones - 1
        return "1" * leadingOnes + "0" * zeroes + "1"