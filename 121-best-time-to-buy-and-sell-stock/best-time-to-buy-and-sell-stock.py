class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        max_profit = 0
        min_value = float("inf")

        for i in range(0,n):
            min_value = min(min_value, prices[i])
            max_profit = max(max_profit, prices[i] - min_value )
        
        
        return max_profit