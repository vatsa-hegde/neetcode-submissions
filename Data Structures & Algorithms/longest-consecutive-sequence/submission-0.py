class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            temp = 1
            if nums[i] + 1 in nums:
                num = nums[i]
                while num + 1 in nums:
                    temp+=1
                    num = num+1
            if temp > res:
                res = temp
        return res