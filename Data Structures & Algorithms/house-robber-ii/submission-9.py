class Solution:
    """
    Need to keep track of whether I have robbed the first house to avoid robbing the last house.
    The same choices as house robber 1. rob i+2 or i+3
    """
    # Top down with memoization
    # def rob(self, nums: List[int]) -> int:
    #     if len(nums) == 0:
    #         return 0
    #     if len(nums) == 1:
    #         return nums[0]
    #     if len(nums) == 2:
    #         return max(nums)
        
    #     cache = {}
        
    #     def maximizeProfit(houseIdx, first):
    #         if houseIdx == len(nums)-1:
    #             if first:
    #                 return 0
    #             return nums[houseIdx]
    #         if (houseIdx,first) in cache:
    #             return cache[(houseIdx,first)]
    #         profit = 0

    #         if (houseIdx+2) < len(nums):
    #             profit += maximizeProfit(houseIdx+2,first)
    #         if  (houseIdx+3) < len(nums):
    #             profit = max(profit, maximizeProfit(houseIdx+3,first))
    #         cache[(houseIdx,first)] =  nums[houseIdx] + profit
    #         # print(cache)
    #         return cache[(houseIdx,first)]
    #     return max(maximizeProfit(0,True), maximizeProfit(1,False), maximizeProfit(2,False))

    # BottomUp
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(nums):
            if len(nums) == 0:
                return 0
            if len(nums) == 1:
                return nums[0]
            
            dp = [0]* len(nums)
            dp[0], dp[1] = nums[0],max(nums[0],nums[1])

            for idx in range(2,len(nums)):
                dp[idx] = max(dp[idx-1], nums[idx]+ dp[idx-2])
            return dp[len(nums)-1]
        return max(helper(nums[1:]), helper(nums[:-1]))




        