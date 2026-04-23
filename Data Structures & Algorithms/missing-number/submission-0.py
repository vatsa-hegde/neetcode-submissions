class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = n
        for i in range(0,n):
            res ^= i ^ nums[i]
        return res