class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        closeBrackets = {')': '(','}':'{',']':'['}

        for bracket in s:
            if bracket in closeBrackets:
                if not stack or stack[-1] != closeBrackets[bracket]:
                    return False
                stack.pop()
                continue
            stack.append(bracket)
        if stack:
            return False

        return True



