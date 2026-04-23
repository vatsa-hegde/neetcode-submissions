class Solution:
    def climbStairs(self, n: int) -> int:
        #Memorization
        # dp = {}
        # def steps(n,dp):
        #     if n < 3:
        #         return n
        #     if n in dp:
        #         return dp[n]
        #     dp[n] = steps(n-1,dp) + steps(n-2,dp)
        #     return dp[n]
        # return steps(n,dp)
        #bottom Up
        if n < 3:
            return n
        dp = [1,2]
        i = 3
        while i <= n:
            temp = dp[1]
            dp[1] += dp[0]
            dp[0] = temp
            i+=1
        return dp[1]