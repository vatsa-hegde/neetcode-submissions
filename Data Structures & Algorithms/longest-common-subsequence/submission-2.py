class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        text1[i] == text2[j]
        I will increament both the strings
        
        Else
        I need to check 2 cases. One where text1's index increaments and text2 stays the same and when text2's index increments and text 1 remains the same. 

        with this in mind i want to check for the Dp array.
        For Bottom up I want to have i and j as dimensions.

        """
        # cache = {}
        # def dfs(i,j):
        #     nonlocal cache
        #     if i >= len(text1) or j >= len(text2):
        #         return 0
        #     if (i,j) in cache:
        #         return cache[(i,j)]
        #     if text1[i] == text2[j]:
        #         cache[(i,j)] = 1 + dfs(i+1,j+1)
        #     else:
        #         cache[(i,j)] = max(dfs(i, j+1), dfs(i+1,j))
        #     return cache[(i,j)]
        # return dfs(0,0)

        dp = [[0]* (len(text2)+1) for _ in range(len(text1)+1)]
        # dp[len(text1)][len(text2)] = 1

        """
        [
        0 0 0 0
        0 0 0 0
        0 0 0 0
        0 0 0 0
        
        ]
        columns = text1
        rows = text2


        """

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1,-1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1+ dp[i+1][j+1]
                dp[i][j] = max(dp[i][j], dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]



