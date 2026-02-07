#  Best time to Buy and Sell Stock
class Solution(object):
    def maxProfit(self, prices):
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP ,sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP   
