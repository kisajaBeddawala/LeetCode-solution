class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = str(x)
        if num == num[::-1]:  #check if the string is the same when reversed
            return True
        else:
            return False