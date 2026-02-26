# Reverse Bits

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(format(n,'032b')[::-1],2)
        