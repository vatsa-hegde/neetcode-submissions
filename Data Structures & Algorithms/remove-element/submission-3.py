class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 1:
            return len(nums) if nums[0] != val else 0
        elif len(nums) == 0:
            return 0
        i = 0
        j = len(nums) - 1
        while i < j:
            while j >= 0 and nums[j] == val:
                j-=1
            if j< 0:
                break
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j-=1
            i+=1
                
        return j+1