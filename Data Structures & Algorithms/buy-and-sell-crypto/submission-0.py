class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = float('inf')
        for price in prices:
            minBuy = min(minBuy, price)
            maxProfit = max(maxProfit, price - minBuy)
        return maxProfit