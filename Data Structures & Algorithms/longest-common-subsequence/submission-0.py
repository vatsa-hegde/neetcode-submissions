class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m = len(text1), len(text2)

        dp = [0] * (m+1)

        for i in range(n):
            cur = [0] * (m+1)
            for j in range(m):
                if text1[i] == text2[j]:
                    cur[j+1] = 1 + dp[j]
                else:
                    cur[j+1] = max(cur[j],dp[j+1]) 
            dp = cur
        return cur[m]

        