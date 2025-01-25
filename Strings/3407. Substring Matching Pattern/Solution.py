class Solution(object):
    def hasMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # get left and right of '*'
        parts = p.split('*', 1)
        left, right = parts[0], parts[1]
        
        if left=="": return right in s
        if right=="": return left in s
        
        left_idx = s.find(left)
        if left_idx!=-1 and right in s[left_idx+len(left):]: return True
        return False
        
print(Solution().hasMatch("ckckkk", "ck*kc"))