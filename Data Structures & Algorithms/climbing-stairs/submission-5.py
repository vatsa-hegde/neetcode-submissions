class Solution:
    def climbStairs(self, n: int) -> int:
        """
        explore 2 different paths each turn 
        """
        # recursion with memoization
        # cache = {}
        # def rec(n):
        #     nonlocal cache
        #     if n == 0:
        #         return 1
        #     elif n < 0:
        #         return 0
        #     elif n in cache:
        #         return cache[n]
           
        #     cache[n] = (rec(n-1) + rec(n-2))
        #     return cache[n]
        # return rec(n)

        prev, secoPrev = 1,1
        for i in range(2,n+1):
            temp = prev + secoPrev
            secoPrev = prev
            prev = temp
        
        return prev


