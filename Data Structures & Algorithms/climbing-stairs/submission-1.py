class Solution:
    def climbStairs(self, n: int) -> int:
        waysToReach = {}
        def findways(i:int):
            if i == 0 or i == 1:
                return 1
            if i in waysToReach:
                return waysToReach[i]
            waysToReach[i] = findways(i-1) + findways(i-2)
            return waysToReach[i]
        return findways(n)
        