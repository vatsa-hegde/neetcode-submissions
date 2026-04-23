class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}
        def dfs(i,s):
            if (i,s) in memo:
                return memo[(i,s)]
            if i >= n:
                return 0
            if s > amount:
                return 0
            elif s == amount:
                return 1
            memo[(i,s)] = dfs(i, s+coins[i]) + dfs(i+1,s)
            return memo[(i,s)]
        return dfs(0,0)

