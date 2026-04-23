class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # res = 0
        # n = len(nums)
        # memo = {}
        # def dfs(i, s):
        #     nonlocal n,nums,target
        #     if (i,s) in memo:
        #         return memo[(i,s)]
        #     if i == n:
        #         memo[(i,s)] = 1 if s == target else 0
        #         return memo[(i,s)]
        #     memo[(i,s)] =  dfs(i+1, s+nums[i]) + dfs(i+1, s-nums[i])
        #     return memo[(i,s)]

        # res = dfs(0,0)
        # return res

        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(n):
            for total, c in dp[i].items():
                dp[i+1][total+nums[i]] += c
                dp[i+1][total-nums[i]] += c
        return dp[n][target]