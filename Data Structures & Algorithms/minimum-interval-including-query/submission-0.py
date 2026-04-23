class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        d = {}
        for interval in intervals:
            l = interval[1] - interval[0] + 1
            for i in range(interval[0], interval[1]+1):
                if i in d:
                    if d[i] > l:
                        d[i] = l
                        continue
                else:
                    d[i] = l
        
        res = []
        for i in queries:
            if i in d:
                res.append(d[i])
            else:
                res.append(-1)

        return res


        