class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        memo = [[float("-inf") for _ in range(n+2)] for _ in range(n+2)]
        for i in range(n+2):
            memo[i][n], memo[n][i] = 0, 0
            memo[n+1][i], memo[i][n+1] = 0,0
        def dfs(i, cur):
            if cur > n:
                return 0
            if i >=0 and cur >= 0  and memo[i][cur] >= 0:
                return memo[i][cur]
            skip = dfs(i,cur+1)
            profit = 0
            if i < 0:
                profit = dfs(cur,cur+1)
            else:
                profit = prices[cur] - prices[i] + dfs(-2,cur+2)
            memo[i][cur] =  max(skip, profit)
            return memo[i][cur]
        return dfs(-2, 0)
