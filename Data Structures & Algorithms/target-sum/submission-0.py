class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        n = len(nums)
        def dfs(i, s):
            nonlocal res,n,nums,target
            if i == n:
                if s == target:
                    res+=1
                return
            dfs(i+1, s+nums[i])
            dfs(i+1, s-nums[i])
        dfs(0,0)
        return res