class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        if len(nums) < 2:
            return [1]
        pref = [x for x in nums]
        preb = [y for y in nums]
        for i in range(1,len(nums)):
            pref[i] *= pref[i-1]
        print(nums)
        print(pref)
        
        for j in range(len(nums)-2, -1,-1):
            preb[j] *= preb[j+1]
        print(preb)
        
        res = [preb[1]]
   
        for i in range(1, len(nums)-1):
            res.append(preb[i+1]*pref[i-1])
        res.append(pref[-2])
        return res