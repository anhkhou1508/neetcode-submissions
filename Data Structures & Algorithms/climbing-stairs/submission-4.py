class Solution:
    def climbStairs(self, n: int) -> int:
        seen = {}
        def waysToReach(i: int) -> int:
            if i == 0 or i == 1:
                return 1
            if i in seen:
                return seen[i]
            seen[i] = waysToReach(i-1) + waysToReach(i-2)
            return seen[i]
        return waysToReach(n)
        