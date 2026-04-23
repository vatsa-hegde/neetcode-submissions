class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        res = False
        n = len(nums)
        def backtrack(i,left,right):
            nonlocal res,n
            if i < 0 or i > n:
                return
            if i == n:
                if left == right:
                    res = True
                return
            backtrack(i+1,left+nums[i],right)
            backtrack(i+1, left, right+nums[i])
        backtrack(0,0,0)
        return res