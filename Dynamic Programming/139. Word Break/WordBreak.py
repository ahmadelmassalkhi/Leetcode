class Solution(object):

    def helper(self, s, wordDict, d):
        if len(s)==0: return True
        if s in d: return d[s]

        for word in wordDict:
            if s.startswith(word) and self.helper(s[len(word):], wordDict, d):
                return True

        d[s] = False
        return False
        
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.helper(s, wordDict, {})



s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(Solution().wordBreak(s, wordDict))