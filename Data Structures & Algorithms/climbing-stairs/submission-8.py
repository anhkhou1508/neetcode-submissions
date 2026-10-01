class Solution:
    def climbStairs(self, n: int) -> int:
        seen = {}
        def wayToReach(i):
            if i == 0 or i == 1:
                return 1
            if i in seen:
                return seen[i]
            seen[i] = wayToReach(i-1) + wayToReach(i-2)
            return seen[i]
        return wayToReach(n)
        


    