class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # def brute(i):
        #     if i >= n:
        #         return 0
        #     return nums[i] + max(brute(i+2), brute(i+3))
        # return max(brute(0), brute(1))

        memo = {}

        def dp(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = nums[i] + max(dp(i+2), dp(i+3))
            return memo[i]
        return max(dp(0), dp(1))
        