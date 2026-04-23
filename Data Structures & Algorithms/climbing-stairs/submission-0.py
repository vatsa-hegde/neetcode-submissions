class Solution:
    def climbStairs(self, n: int) -> int:
        #Memorization
        dp = {}
        def steps(n,dp):
            if n < 3:
                return n
            if n in dp:
                return dp[n]
            dp[n] = steps(n-1,dp) + steps(n-2,dp)
            return dp[n]
        return steps(n,dp)
        