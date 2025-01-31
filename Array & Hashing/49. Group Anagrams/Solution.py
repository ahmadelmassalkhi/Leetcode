from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        for i,s in enumerate(strs):
            d["".join(sorted(s))].append(strs[i])
        return list(d.values())
