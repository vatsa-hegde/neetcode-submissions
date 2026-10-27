class Solution:
    def climbStairs(self, n: int) -> int:
        """
        explore 2 different paths each turn 
        """
        cache = {}
        def rec(n):
            nonlocal cache
            if n == 0:
                return 1
            elif n < 0:
                return 0
            elif n in cache:
                return cache[n]
           
            cache[n] = (rec(n-1) + rec(n-2))
            return cache[n]
        return rec(n)