class Solution:
    """
    1 5 10
    12
    [111111111111, 11111 5 11, 5 5 1 1, 10 1 1]

    Keep on adding the same coing
    go to next coin without adding any coin
    consider this coin once and go to next coin 

    minimize the total number of coins
    """
    # Top down approach
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     if amount == 0:
    #         return 0
    #     cache = {}
    #     def recursion(remaining):
    #         nonlocal coins, cache
    #         if remaining == 0:
    #             return 0
    #         if remaining in cache:
    #             return cache[remaining]
    #         cache[remaining] = float('inf')
    #         for coin in coins:
    #             if remaining - coin >= 0:
    #                 cache[remaining] = min(cache[remaining], 1+recursion(remaining-coin))
    #         return cache[remaining]
    #     result = recursion(amount)
    #     return -1 if result == float('inf') else result
    # Time O(n*t) space o(t) where t is the amount and n in the length of coins
    # Without memoization time O(n**t) space O(t)
    
    # Bottom Up Approach
    """
    Thiught process: For each amount a and a coin c, if we know the amount of coings required for amount (a-c) then we know to make the amount a it minimum number of coins would be 1 + minimum coins for (a-c)
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1) # reason being we can not have more than amount number of coins, even if we say the least being 1, To make the amount with 1, it will take us amount number of coins. So we are setting this with amount+1

        dp[0] = 0 # base case. to make amount 0 we need 0 coins 

        for a in range(amount+1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1+dp[a-coin])
        

        
        return -1 if dp[amount] > amount else dp[amount]



        