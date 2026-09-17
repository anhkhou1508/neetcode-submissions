class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}
        for c in s:
            if c not in hm:
                hm[c] = 1
            else:
                hm[c] += 1
        for c in t:
            if c in hm:
                hm[c] -= 1
            else:
                hm[c] = 1
            
        for item in hm.values():
            if item > 0 or item < 0: 
                return False
        return True


