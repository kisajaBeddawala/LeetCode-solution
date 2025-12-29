# Apple Redistribution into Boxes

class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        tot = sum(apple)
        capacity.sort()
        c = 0
        for i in range(len(capacity)-1, -1, -1):
            if (tot - capacity[i]) > 0:
                tot -= capacity[i]
                c += 1
            else:
                c += 1
                return c
        return c