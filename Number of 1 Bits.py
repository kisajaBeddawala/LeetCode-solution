# Number of 1 Bits

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        bNum = bin(n)[2:]
        for i in bNum:
            if i == '1':
                c += 1
        return c
