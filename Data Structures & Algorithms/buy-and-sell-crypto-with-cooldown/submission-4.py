class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Problem is to find max profit from the given prices

        I can not sell  a day after I have sold the current one
        I can only have one Neetcoin at a time

        dp[i][j] = price[i] - price[j] + max( dp[i+2][i+2:])
        """

        dp = {}  # key=(i, buying) val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)

