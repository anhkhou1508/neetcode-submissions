class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def maxRobLinear(arr: List[int]) -> int:
            if not arr:
                return 0
            if len(arr) == 1:
                 return arr[0]
            seen = {}
            def maxRob(i: int) -> int:
                if i == 0:
                    return arr[0]
                if i == 1:
                    return max(arr[0], arr[1])
                if i in seen:
                    return seen[i]
                seen[i] = max(maxRob(i-1), maxRob(i-2) + arr[i])
                return seen[i]
            return maxRob(len(arr)-1)
        return max(maxRobLinear(nums[1:]), maxRobLinear(nums[:-1]))
        


