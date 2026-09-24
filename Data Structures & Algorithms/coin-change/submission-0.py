class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def findMinCoin(i: int):
            if i == 0:
                return 0
            if i < 0:                  
                return float('inf')
            if i in dp:
                return dp[i]
            best = float('inf')
            for coin in coins:
                best = min(best, 1+findMinCoin(i-coin))
            
            dp[i]=best
            return dp[i]
        result = findMinCoin(amount)
        return -1 if result == float('inf') else result
