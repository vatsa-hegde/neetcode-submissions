class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = len(nums) - 1
        l = 0
        res = 0
        while r >= l:
            mid = (l+r)// 2
            if nums[mid] > nums[r]:
                l = mid +1
            elif nums[mid] <= nums[r]:
                print(l, mid,r)
                res = nums[mid]
                if nums[mid-1] > nums[mid]:
                    break
                r = mid-1
        return res

