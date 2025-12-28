# Best Time to Buy and Sell Stock

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # max_prof = 0
        # for i in range(len(prices)-1):
        #     buy = prices[i]
        #     for j in range(i+1, len(prices)):
        #         sell = prices[j]
        #         profit = 0
        #         if sell > buy:
        #             profit = sell - buy
        #         max_prof = max(max_prof, profit)
        # return max_prof

        min_p = float('inf')
        max_prof = 0

        for i in range(len(prices)):
            if prices[i] < min_p:
                min_p = prices[i]
                continue
            if prices[i] > min_p:
                max_prof = max(max_prof, (prices[i] - min_p))
        return max_prof
        