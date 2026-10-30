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
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        cache = {}
        def recursion(remaining):
            nonlocal coins, cache
            if remaining == 0:
                return 0
            if remaining in cache:
                return cache[remaining]
            cache[remaining] = float('inf')
            for coin in coins:
                if remaining - coin >= 0:
                    cache[remaining] = min(cache[remaining], 1+recursion(remaining-coin))
            return cache[remaining]
        result = recursion(amount)
        return -1 if result == float('inf') else result

            
            


    
    # Bottom Up Approach
    # def coinChange(self, coins: List[int], amount: int) -> int:


        