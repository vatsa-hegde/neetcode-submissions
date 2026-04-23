class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [101]*n
        memo[n-1] = 0
        goal = n-1
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= n-1:
                memo[i] = 1
                goal = i
                continue
            if i+ nums[i] >= goal:
                memo[i] = 1+ min(memo[goal:i+nums[i]+1])
                goal = i
        return memo[0]

        