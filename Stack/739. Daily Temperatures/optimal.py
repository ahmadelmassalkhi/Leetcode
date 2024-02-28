    


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(temperatures)
        hottest = 0
        for i in range(len(temperatures)-1, -1, -1):
            if temperatures[i] >= hottest:
                hottest = temperatures[i]
                continue # keep it 0 (will never come a day AFTER it with higher temperature, because we are looping in reverse)
            days = 1
            while temperatures[i] >= temperatures[i+days]: # until temp[i]<temp[i+days]
                days += answer[i+days]
                # we know `temperatures[i] >= temperatures[i+days]` 
                # so we skip all days less hot than `temperatures[i+days]` by getting the day with hotter temperature than it
            answer[i] = days
        return answer