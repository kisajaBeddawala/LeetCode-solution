class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        for i in range(len(s)):
            if len(l) >= 1:
                if (s[i] == ')' and l[-1] == '(') or (s[i] == '}' and l[-1] == '{') or (s[i] == ']' and l[-1] == '['):
                    l.pop()
                else:
                   l.append(s[i]) 
            else:
                l.append(s[i])
        

        if len(l) == 0:
            return True
        else:
            return False

        