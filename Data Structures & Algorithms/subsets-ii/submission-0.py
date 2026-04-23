class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def recurse(sub, idx):
            if sub not in res:
                res.append(sub[:])
            if idx >= len(nums):
                return
            sub.append(nums[idx])
            recurse(sub, idx+1)
            sub.pop()
            while idx+1 < len(nums) and nums[idx] == nums[idx+1]:
                idx += 1
            recurse(sub,idx+1)
        recurse([],0)
        return res


                
        