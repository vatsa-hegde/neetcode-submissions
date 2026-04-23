class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        def dfs(i, cur):
            if cur >= n:
                return 0
            skip = dfs(i,cur+1)
            profit = 0
            if i < 0:
                profit = dfs(cur,cur+1)
            else:
                profit = prices[cur] - prices[i] + dfs(-2,cur+2)
            return max(skip, profit)
        return dfs(-2, 0)
