class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSequence = 0
        currentSequence = 1

        num_set = set(nums)
        for num in nums:
            if num-1 not in num_set:
                while num+1 in num_set:
                    currentSequence += 1
                    num += 1
                if currentSequence > longestSequence:
                    longestSequence = currentSequence
                currentSequence = 1

        return longestSequence



