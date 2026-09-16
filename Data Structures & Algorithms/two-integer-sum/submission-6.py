class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for index, val in enumerate(nums):
            if target-val in hm:
                return [hm[target-val], index]
            else:
                hm[val] = index
