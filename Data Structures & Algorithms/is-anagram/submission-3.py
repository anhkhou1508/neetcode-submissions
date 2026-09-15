class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}
        for c in s:
            if c not in hm:
                hm[c] = 1
            else:
                hm[c] += 1
        
        for c in t:
            if c not in hm:
                return False
            else:
                if hm[c] < 0:
                    return False
                if hm[c] >= 0:
                    hm[c] -= 1
        for val in hm.values():
            if val > 0 or val < 0:
                return False
        return True
             