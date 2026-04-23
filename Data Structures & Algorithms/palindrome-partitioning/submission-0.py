class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        part = []
        def palindrome(word):
            if word == word[::-1]:
                return True
            return False
        def recurse(idx):
            if idx >= n:
                res.append(part.copy())
                return
            for i in range(idx,n):
                if palindrome(s[idx:i+1]):
                    part.append(s[idx:i+1])
                    recurse(i+1)
                    part.pop()
        recurse(0)
        return res

        