class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        current = prices[0]
        for price in prices:
            maxprofit = max(maxprofit, price - current)
            current = min(price, current)
        return maxprofit