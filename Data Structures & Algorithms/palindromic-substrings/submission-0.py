class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromeCount = 0
        def expand(l, r):
            nonlocal palindromeCount
            while l>=0 and r<len(s) and s[l]==s[r]:
                palindromeCount += 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            expand(i, i) #odd
            expand(i, i+1) #even
        
        return palindromeCount

# i = 3
# count = 9
#     0 1 2 3 4
#     a a a a
#           l    
#           r

    