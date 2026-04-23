class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            print(diff,d)
            if diff in d:
                return [ d[diff],i]
            d[nums[i]] = i
        