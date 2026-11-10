class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Problem is to find max profit from the given prices

        I can not sell  a day after I have sold the current one
        I can only have one Neetcoin at a time

        dp[i][j] = price[i] - price[j] + max( dp[i+2][i+2:])
        """
        if len(prices) < 2:
            return 0
        
        cache = {}
        def dfs(i, buyFlag):
            if i >= len(prices):
                return 0
            if (i,buyFlag) in cache:
                return cache[(i,buyFlag)]
            profit = dfs(i+1,buyFlag)
            if buyFlag:
                buy = dfs(i+1,False)-prices[i]
                profit = max(profit,buy)
            else:
                profit = max(profit, prices[i] + dfs(i+2, True))
            cache[(i,buyFlag)] = profit
            return cache[(i,buyFlag)]
        return max(0,dfs(0,True))

        

