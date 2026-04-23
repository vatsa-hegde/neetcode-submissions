class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}
        def backtrack(i):
            if i == n-1:
                return True
            if nums[i] == 0:
                memo[i] = False
                return False
            if i in memo:
                return memo[i]
            memo[i] = False
            # print(memo,i)
            for j in range(1,nums[i]+1):
                # print(nums[i], j)
                memo[i] = memo[i] or backtrack(i+j)
            return memo[i]
        return backtrack(0)

        