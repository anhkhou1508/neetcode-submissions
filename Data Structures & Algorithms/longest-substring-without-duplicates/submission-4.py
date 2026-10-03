class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = {}
        l = 0
        best = 0
        for i, c in enumerate(s):
            if c in lastSeen and lastSeen[c] >= l:
                l = lastSeen[c] + 1
            lastSeen[c] = i
            best = max(best, i-l+1)
        return best
