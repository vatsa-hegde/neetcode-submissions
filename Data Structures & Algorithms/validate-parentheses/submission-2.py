class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = {')':'(','}':'{', ']' : '['}
        
        for l in s:
            if l in closing.keys():
                if len(stack) == 0 or stack[-1] != closing[l]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(l)
        if len(stack) != 0:
            return False
        return True