







import collections


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = collections.defaultdict(list)
        for word in strs:
            result[''.join(sorted(word))].append(word)
        return list(result.values())


        '''
            sorted() returns a list (mutable)
            you can't use lists as dictionary keys
            so we converted to string (immutable)
        '''

        