class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = ["(", "[", "{"]
        close_brackets = {")":"(", "]":"[", "}":"{"}
        for char in s:
            if char in open_brackets:
                stack.append(char)
            elif char in close_brackets:
                if not stack or stack.pop() != close_brackets[char]:
                    return False
        return not stack 
