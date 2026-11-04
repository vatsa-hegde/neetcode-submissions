class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        For each dp[i][j] the unique path would be the sum of dp[i-1][j] and dp[i][j-1]
        for all dp[0][*] and dp[*][0] the only possible value is 1 since I can go either right or down
        """

        dp = [[0]*(m) for _ in range(n)]
        for i in range(m):
            dp[0][i] = 1
        
        for j in range(n):
            dp[j][0] = 1
        
        for r in range(1, n):
            for col in range(1,m):
                dp[r][col] = dp[r-1][col] + dp[r][col-1]
            
        return dp[n-1][m-1]


        