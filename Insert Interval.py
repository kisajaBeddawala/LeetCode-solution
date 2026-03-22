# Insert Interval

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        finish = False
        for index in range(len(intervals)):
            start = intervals[index][0]
            end = intervals[index][1]
    
            if start <= newInterval[0] and end >= newInterval[0]:
                if end <= newInterval[1]:
                    intervals[index][1] = newInterval[1]
                    finish = True
                    break
                else:
                    finish = True
            elif start >= newInterval[0] and end <= newInterval[1]:
                intervals.insert(index,newInterval)
                finish = True
                break

        print(intervals)

        #if new Interval not merge insert it
        if not finish:
            count1 = False
            count2 = False
            idx = 0
            for index in range(len(intervals)-1,-1,-1):
                start = intervals[index][0]
                end = intervals[index][1]

                if start > newInterval[0] and end > newInterval[1]:
                    count1 = True
                    if index == 0:
                        idx = 0
                        break
                    
                elif start < newInterval[0] and end < newInterval[1]:
                    if index == len(intervals) - 1:
                        idx = index + 1
                        break
                    if count1 and index == 0:
                        idx = 1
                        break
                    elif count1:
                        idx = index + 1
                        break
                    count2 = True
                    
            intervals.insert(idx, newInterval)

        print(intervals)

        #find merge intervals
        ind = 0
        while ind < len(intervals)-1:
            if intervals[ind][1] >= intervals[ind+1][0]:
                if intervals[ind][1] >= intervals[ind+1][1]:
                    intervals.pop(ind+1)
                else:
                    intervals[ind][1] = intervals[ind+1][1]
                    intervals.pop(ind+1)
            else:
                ind += 1


        return intervals