class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[0])
        prev = [-50001,-50001]
        res = 0
        for interval in intervals:
            if interval[0] < prev[1]:
                res +=1 
                prev = [
                    max(interval[0],prev[0]),
                    min(interval[1],prev[1])
                ] 
            else:
                prev = interval
            # print(res,interval,prev)
        return res
        