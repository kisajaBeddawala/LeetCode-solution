# Reverse Integer

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0 :
            n = int(str(x)[::-1])
        else:
            n = -int(str(x)[:0:-1])

        if n <= 2**31 - 1 and n >= -2**31:
            return n
        else:
            return 0
            
        