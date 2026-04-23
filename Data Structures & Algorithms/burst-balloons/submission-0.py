class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def helper(nums):
            res = 1
            l = len(nums)
            if l == 2:
                return 0
            for i in range(1,l-1):
                temp = nums[i-1] * nums[i+1] * nums[i]
                # print(nums[i-1], nums[i+1], nums[i], temp)
                ele = nums.pop(i)
                # print("nums",nums)
                res = max(res,temp + helper(nums))
                nums.insert(i,ele)
            return res
        nums.insert(0,1)
        nums.append(1)
        return helper(nums)

