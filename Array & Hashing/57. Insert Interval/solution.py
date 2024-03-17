class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = []
        start_i = end_i = -1
        newStart, newEnd = newInterval
        for idx, interval in enumerate(intervals):
            start, end = interval
            if start_i == -1:
                if end < newStart:
                    result.append(interval)
                    continue
                start_i = idx
            # newStart <= end
            if newEnd <= end:
                end_i = idx
                break
        
        # newInterval's start exceeds all intervals
        if start_i == -1:
            intervals.append(newInterval)
            return intervals
        newStart = min(newStart, intervals[start_i][0])
        
        # newInterval's start exceeds all intervals
        if end_i == -1:
            result.append([newStart, newEnd])
            return result
        
        # newEnd in [start, end]
        if newEnd >= intervals[end_i][0]:
            newEnd = end # take max
            end_i += 1 # used the current interval (to merge with new interval), proceed to next

        # add new/modified interval
        result.append([newStart, newEnd])

        # re-add all preceeding intervals
        for i in range(end_i, len(intervals)):
            result.append(intervals[i])

        return result