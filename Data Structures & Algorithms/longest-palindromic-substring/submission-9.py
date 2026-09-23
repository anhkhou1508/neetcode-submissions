class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalindrome = ""
        def expand(l, r):
            nonlocal longestPalindrome
            while l>=0 and r<len(s) and s[l] == s[r]:
                currentPalindromeLen = r-l+1
                if currentPalindromeLen > len(longestPalindrome):
                    longestPalindrome = s[l:r+1]
                l -= 1
                r += 1
            
        for i in range(len(s)):
            expand(i,i)
            expand(i,i+1)
        
        return longestPalindrome


            