class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            print(diff, d, diff in d)

            if nums[i] in d:
                return list((d[nums[i]], i))
            else:
                d[diff] = i
        return []