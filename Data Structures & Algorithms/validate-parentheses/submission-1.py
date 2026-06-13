class Solution:
    def isValid(self, s: str) -> bool:
        closing = {
            "}":"{",
            "]":"[",
            ")": "("
        }
        stack = []
        for _char in s:
            if _char in closing:
                if len(stack) == 0 or closing[_char] != stack.pop():
                    return False 
            else:
                stack.append(_char)

        return True if not stack else False