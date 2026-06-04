class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if target == nums[-1]:
            return True
        elif target < nums[-1]:
            i = len(nums)-1
            while i >= 0 and nums[i] <= nums[-1]:
                if nums[i] == target:
                    return True
                i-=1
        else:
            i = 0
            while i < len(nums) and nums[i] >= nums[0]:
                if nums[i] == target:
                    return True
                i+=1
        return False


        