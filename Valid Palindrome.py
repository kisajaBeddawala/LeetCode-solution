class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1
            elif not s[left].isalnum() and s[right].isalnum():
                left += 1
                continue
            elif s[left].isalnum() and not s[right].isalnum():
                right -= 1
                continue
            else:
                left += 1
                right -= 1
                continue
        return True
        