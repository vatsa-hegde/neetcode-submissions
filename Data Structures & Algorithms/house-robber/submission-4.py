"""
 2 1 1 8 9 10


 questions:
 whether everything will be profit? or positive numbers

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Top down approach
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        cache = dict()

        def maximizeProfit(house):
            nonlocal nums, cache
            if house in cache:
                return cache[house]
            cache[house] = nums[house]
            if (house+3) < len(nums):
                cache[house] += max(maximizeProfit(house+2),maximizeProfit(house+3))
            elif (house+2) < len(nums):
                cache[house] += maximizeProfit(house+2)
            return cache[house]
        return max(maximizeProfit(0), maximizeProfit(1))

        
        