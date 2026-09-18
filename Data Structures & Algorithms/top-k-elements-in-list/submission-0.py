class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        arr = []
        for i in nums:
            if i not in hm:
                hm[i] = 1
            else:
                hm[i] += 1
        
        for val, freq in hm.items():
            arr.append((freq,val))
        
        arr.sort(reverse=True)

        result = []
        for i in range(k):
            result.append(arr[i][1])
        
        return result
