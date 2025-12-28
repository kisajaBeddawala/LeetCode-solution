# Merge Intervals

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        new = [intervals[0]] # first interval added to new list

        # iterate through intervals starting from second interval
        for i in range(1,len(intervals)):
            if intervals[i][0] <= new[-1][1]:
                new[-1][1] = max(intervals[i][1], new[-1][1]) # find max end time
            else:
                new.append(intervals[i])  # if can't merge, add to new list
        return new  
        