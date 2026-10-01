from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        result = []
        def computeID(s: str):
            counts = [0]*26
            for c in s:
                counts[ord(c)-ord('a')] += 1
            idTuple = tuple(counts)
            return idTuple

        for word in strs:
            idTuple = computeID(word)
            hm[idTuple].append(word)

        for anagrams in hm.values():
            result.append(anagrams)
        
        return result

