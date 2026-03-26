# Longest Palindrome

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for i in s:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        print(count)
        
        length = 0
        partial = 0
        findOdd = False
        for c in count:
            if count[c] % 2 == 0:
                length += count[c]
            else:
                partial += count[c] - 1
                findOdd = True

        if findOdd:
            length += 1

        return length + partial