class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        prefixP = [1] * n
        suffixP = [1] * n

        for i in range(1, n):
            prefixP[i] = (nums[i-1] * prefixP[i-1])

        for i in range(n-2, -1, -1):
            suffixP[i] = (nums[i+1] * suffixP[i+1])
        
        for i in range(n):
            result.append(prefixP[i] * suffixP[i])
        
        return result

