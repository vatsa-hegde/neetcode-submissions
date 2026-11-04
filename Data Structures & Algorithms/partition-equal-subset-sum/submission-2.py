class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        I have to traverse the entire list and at the end I have to check whether the sum is equal or not. At Each step I will have an option to add it to either 1st subset or the second
        """
        cache = {}
        def dfs(i,sum1, sum2):
            if i == len(nums):
                if sum1 == sum2:
                    return True
                return False
            if (i,sum1) in cache:
                return cache[(i,sum1)]
            res =  (dfs(i+1, sum1+nums[i], sum2) | dfs(i+1, sum1, sum2+nums[i]))
            cache[(i, sum1)] = res
            return cache[(i,sum1)]

        
        return dfs(0,0,0)

        """
        1 2 3 4
        1 0 1
            2 2 1
                3 5 1
                    3 5 5
            2 0 3

        """
                
        
        