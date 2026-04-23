class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        res = 0
        if n <= 1:
            if s[0] == '0':
                return 0
            return n
        dp = {}
        def backtrack(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if s[i] == '0':
                return 0
            if i in dp:
                return dp[i]
            a = backtrack(i+1)
            b = 0
            if 26 >= int(s[i:i+2]) > 0:
                b = backtrack(i+2)
            dp[i] = a+b
            return dp[i]

        return backtrack(0)
        