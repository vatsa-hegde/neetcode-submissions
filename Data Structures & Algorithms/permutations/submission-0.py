class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n <=1 :
            return [nums]

        res = []
        
        def recurse(perm, visit):
            if len(perm) == n:
                res.append(perm[:])
            
            for i in range(n):
                if visit[i]:
                    continue
                perm.append(nums[i])
                visit[i] = True
                recurse(perm,visit)
                visit[i] = False
                perm.pop()
        recurse([], [False]*n)
        return res
         
        