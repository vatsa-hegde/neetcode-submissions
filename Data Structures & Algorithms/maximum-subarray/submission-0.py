class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -1001
        prev = -1001
        for num in nums:
            if prev > 0:
                prev += num
            else:
                prev = num
            if prev > res:
                res = prev
        return res
        