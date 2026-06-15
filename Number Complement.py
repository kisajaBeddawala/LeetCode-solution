# Number Complement

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        length = num.bit_length()
        mask = (1 << length) - 1
        complement = num  ^ mask
        return int(complement) 