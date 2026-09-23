class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for index, num in enumerate(nums):
            if num not in hm:
                hm[num] = index
            else:
                hm[num] = index

        for index, num in enumerate(nums):
            if target-num in hm and index != hm[target-num]:
                return [index, hm[target-num]]
            else:
                hm[num] = index

