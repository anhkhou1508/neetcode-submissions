class Solution:
    def minCostClimbingStairs(self, cost):
        memo = {}
        def minCost(i):
            if i==0 or i==1:
                return cost[i]
            if i in memo:
                return memo[i]
            memo[i] = cost[i] + min(minCost(i-1), minCost(i-2))
            return memo[i]

        n = len(cost)
        answer = min(minCost(n-1), minCost(n-2))
        return answer
        


