class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1 or len(prices) == 0:
            return 0

        lowestBuyPriceSoFar = prices [0]
        bestProfit = 0
        for i in range(1, len(prices)):
            lowestBuyPriceSoFar = min(prices[i-1], lowestBuyPriceSoFar)
            profit = prices[i] - lowestBuyPriceSoFar
            if profit > bestProfit:
                bestProfit = profit
        
        return bestProfit

