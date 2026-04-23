class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def regress(diff,sub,j):
            nonlocal nums, res
            if diff == 0:
                # print(sub)
                if sub not in res:
                    res.append(sub[:])
                    print(res)
            elif diff < 0 :
                return
            for i in range(j, len(nums)):
                # print(sub)
                sub.append(nums[i])
                regress(diff-nums[i], sub,i)
                sub.pop()
        regress(target, [],0)
        return res


        