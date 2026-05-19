class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp = {}
        res = 0
        for i in nums:
            temp[i] = 0

        for j in nums:
            if j-1 not in temp:
                v = 1
                while j+1 in temp:
                    v+=1
                    j+=1
                if v > res:
                    res = v
        return res
                

        
