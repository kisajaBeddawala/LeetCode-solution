class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # uncomment only below line to use Counter and comment rest of the code
        # return Counter(s) == Counter(t)

        # manual implementation
        if len(s) != len(t):
            return False
        else:
            s_set = set(s)

            for i in s_set:
                if s.count(i) != t.count(i):
                    return False
            return True
        