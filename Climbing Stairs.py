# Climbing Stairs

class Solution(object):
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {1:1, 2:2}
        

        def ans(n):
            if n in memo:
                return memo[n]
            memo[n] = ans(n-1) + ans(n-2)
            return memo[n]

        return ans(n)
            
        