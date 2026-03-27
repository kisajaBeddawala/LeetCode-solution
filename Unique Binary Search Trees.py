# Unique Binary Search Trees

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)

        dp[0] = 1
        dp[1] = 1

        for nodes in range(2,n+1):
            for i in range(1,nodes+1):
                dp[nodes] += dp[i-1] * dp[nodes-i]

        return dp[n]