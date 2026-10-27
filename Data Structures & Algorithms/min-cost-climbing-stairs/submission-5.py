class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        Cost array 
        min cost 

        goal is to reach the final step with min cost

        min cost of laststep or a step before that and it's cost
        '''
        # TOP Down Approach
        # cache = {}
        # cache[0] = 0
        # cache[1] = 0
        # def recursion(idx):
        #     if idx in cache:
        #         return cache[idx]
        #     cache[idx] =  min((cost[idx-1] + recursion(idx-1)), (cost[idx-2])+ recursion(idx-2))
        #     return cache[idx]
        # return recursion(len(cost))

        # time: o(n) space: o(n)

        # Bottom UP
        n = len(cost)

        prev, secondPrev = 0,0

        for i in range(2,n+1):
            temp = min((cost[i-1]+prev), (cost[i-2]+secondPrev))
            secondPrev = prev
            prev = temp
        return prev



        
        