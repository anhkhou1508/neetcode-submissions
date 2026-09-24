class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedS = "".join(c.lower() for c in s if c.isalnum())
        l = 0
        r = len(cleanedS)-1
        while l<=r:
            if cleanedS[l] != cleanedS[r]:
                return False
            else:
                l += 1
                r -= 1
        
        return True


