class Solution:
    def rob(self, nums: List[int]) -> int:
        seen = {}
        lens = len(nums)
        def maxAmount(i:int):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0],nums[1])
            if i in seen:
                return seen[i]
            seen[i] = max(maxAmount(i-1), maxAmount(i-2)+nums[i])
            return seen[i]
        return maxAmount(lens-1)
            
