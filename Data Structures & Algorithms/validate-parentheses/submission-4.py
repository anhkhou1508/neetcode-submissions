class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        pairParen = {"}":"{", "]":"[", ")":"("}
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                if pairParen[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False
            

