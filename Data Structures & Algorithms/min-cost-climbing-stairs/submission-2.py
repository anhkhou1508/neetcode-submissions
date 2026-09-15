class Solution:
    def minCostClimbingStairs(self, cost):
        minCostToReach = {}
        l = len(cost)
        def minCost(i:int):
            if i == 0 or i == 1:
                return cost[i]
            if i in minCostToReach:
                return minCostToReach[i]
            minCostToReach[i] = cost[i] + min(minCost(i-1),minCost(i-2))
            return minCostToReach[i]
        return min(minCost(l-1),minCost(l-2))
        


