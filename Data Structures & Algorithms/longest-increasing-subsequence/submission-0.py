class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        def backtrack(i, maxele,l):
            nonlocal res
            if i == n:
                return
            backtrack(i+1,maxele, l)
            if nums[i] > maxele:
                maxele = nums[i]
                l += 1
                backtrack(i+1,maxele,l)
            if l > res:
                res = l
        backtrack(0,-1001,0)
        return res
            


        