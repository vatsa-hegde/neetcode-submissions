class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        # def brute(n):
        #     if n >= len(cost):
        #         return 0
        #     return cost[n] + min(brute(n+1), brute(n+2)) 

        # return min(brute(0), brute(1))
        #memorization
        # dp = {}
        # def steps(m, dp):
        #     if m >= len(cost):
        #         return 0
        #     if m in dp:
        #         return dp[m]
            
        #     dp[m] = cost[m] + min(steps(m+1,dp), steps(m+2,dp))
        #     return dp[m]
        # return min(steps(0,dp), steps(1,dp)) 

        if n == 1:
            return cost[0]
        dp = [cost[0],cost[1]]
        i = 2
        while i < n:
            temp = dp[1]
            dp[1] = cost[i] + min(dp[0],dp[1])
            dp[0] = temp
            i+=1
        return min(dp)

        