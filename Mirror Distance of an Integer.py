# Mirror Distance of an Integer

class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        return abs(n-int(str(n)[::-1]))
        