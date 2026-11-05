class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        To know where the current letter is a part of any subsequence, it should macth the char in the text2 and check if there is any  subsequence which is already there from i+1 to n

        c r a b t
        c a t
         dp = 
         [
            c r a b t
         c  0 0 0 0 0 0
         a  0 0 2 1 1 0
         t  1 1 1 1 1 0
            0 0 0 0 0 0
         ]
        """

        dp = [[0]*(len(text1)+1) for _ in range(len(text2)+1)]

        for i in range(len(text2)-1, -1,-1):
            for j in range(len(text1)-1, -1, -1):
                if text1[j] == text2[i]:
                    dp[i][j] = 1+dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
                
        


