class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # convert binary to int, add them, convert back to binary and remove '0b' prefix
        return bin(int(a,2)+int(b,2))[2:]  
        