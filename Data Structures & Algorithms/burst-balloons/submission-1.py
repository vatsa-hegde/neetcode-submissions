class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}
        def helper(nums):
            l = len(nums)
            if l == 2:
                return 0
            s = ''.join(str(nums))
            if s in dp:
                return dp[s]
            dp[s] = 1
            for i in range(1,l-1):
                x,j,k = nums[i-1],nums[i+1],nums[i]
                nums.pop(i)
                dp[s] = max(dp[s],x*j*k + helper(nums))
                nums.insert(i,k)
            return dp[s]
        nums.insert(0,1)
        nums.append(1)
        return helper(nums)

