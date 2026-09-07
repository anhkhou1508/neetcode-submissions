class Solution:
    def climbStairs(self, n: int) -> int:
        wayBeen = {}
        def findWay(i):
            if i == 0 or i == 1:
                return 1
            if i in wayBeen:
                return wayBeen[i]
            wayBeen[i] = findWay(i-1) + findWay(i-2)
            return wayBeen[i]
        
        return findWay(n)