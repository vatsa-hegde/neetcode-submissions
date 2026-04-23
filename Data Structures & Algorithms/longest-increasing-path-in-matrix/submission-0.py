class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix[0]), len(matrix)
        dp = [[0]*m for _ in range(n)]
        res = 0
        # print(dp)
        def dfs(i,j):
            # print(i,j,dp)
            nonlocal m,n
            if dp[i][j] > 0:
                return dp[i][j]
            maximum = 0
            for r,c in [(1,0),(-1,0),(0,1),(0,-1)]:
                if i+r >=0 and i+r < n and j+c >= 0 and j+c < m and matrix[i][j] < matrix[i+r][j+c]:
                    maximum = max(maximum,dfs(i+r,j+c))   
            dp[i][j] = maximum+1        
            return dp[i][j]
        for x in range(n):
            for y in range(m):
                res = max(res,dfs(x,y) if dp[x][y] == 0 else dp[x][y])
        # print(dp)
        return res
            
        