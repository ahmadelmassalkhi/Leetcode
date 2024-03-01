class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = 0
        i = 1
        for m in num1[::-1]:
            result += int(m) * int(num2) * i
            i *= 10
        return str(result)