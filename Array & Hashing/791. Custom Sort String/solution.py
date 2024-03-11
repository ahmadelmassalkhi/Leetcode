class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        d = {}
        for idx, letter in enumerate(order):
            d[letter] = idx

        def custom_sort_function(letter):
            if letter not in d:
                return len(order)
            return d[letter]
        
        return ''.join(sorted(s, key=custom_sort_function))
