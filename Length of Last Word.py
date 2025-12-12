class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()  #remove leading and trailing spaces
        return len(s.split(" ")[-1]) #get the last word and return its length
        