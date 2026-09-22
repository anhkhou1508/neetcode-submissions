class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for string in strs:
            stringLen = len(string)
            encodedStr += str(stringLen) + "#" + string

        return encodedStr
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            wordLen = int(s[i:j])
            word = s[j+1 : j+1+wordLen]
            result.append(word)
            i = j + 1 + wordLen

        return result
