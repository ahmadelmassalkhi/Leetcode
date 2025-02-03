from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(s))+"#"+s for s in strs])

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = s.find('#', i) # hash location
            length = int(s[i:j]) # length of current word
            i = j+length+1 # start of new word
            res.append(s[j+1:i])
        return res


encoded = Solution().encode(["we","say",":","yes","!@#$%^&*()"])
decoded = Solution().decode(encoded)
print(decoded)