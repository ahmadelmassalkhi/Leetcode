


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower() # palindrome is case insensitive
        def isValid(c):
            return (ord('a')<=ord(c) and ord(c)<=ord('z')) or (ord('0')<=ord(c) and ord(c)<=ord('9'))
        left, right = 0, len(s)-1
        while left < right:
            while left<right and not isValid(s[left]): # skip non-alphanumeric characters
                left+=1
            while left<right and not isValid(s[right]): # skip non-alphanumeric characters
                right-=1
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True

s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))