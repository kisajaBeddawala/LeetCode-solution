class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left = 0
        right = 1
        longest = 0
        if s == "":
            return 0
        while right < len(s):
            if s[right] in s[left:right]:
                longest = max(longest, (right-left))
                left += s[left:right].index(s[right]) + 1
                right += 1
            else:
                right += 1
        longest = max(longest, (right-left))
        return longest
        