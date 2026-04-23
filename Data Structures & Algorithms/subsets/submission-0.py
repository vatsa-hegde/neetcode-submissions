class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, arr: list):
            nonlocal nums, res
            if i >= len(nums):
                return
            arr.append(nums[i])
            if arr not in res:
                res.append(arr[:])
            backtrack(i+1, arr)
            arr.pop()
            backtrack(i+1, arr)
        backtrack(0, [])
        res.append([])
        return res


        