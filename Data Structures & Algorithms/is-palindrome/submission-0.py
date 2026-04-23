import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        rev = s[::-1]
        # print(rev, s)
        if s.lower() == rev.lower():
            return True
        return False
        