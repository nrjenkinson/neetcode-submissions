class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = (prices[0], 0)

        for i, price in enumerate(prices):
            if price < minBuy[0]:
                minBuy = (price, i)
            
            if i > minBuy[1]:
                maxProfit = max(maxProfit, price - minBuy[0])
        return maxProfit