class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        left, right = p.split('*', 1)
        
        l = s.find(left)
        if l!=-1 and right in s[l+len(left):]: return True
        return False