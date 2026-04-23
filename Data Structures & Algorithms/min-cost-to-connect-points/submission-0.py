class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minT = {}
        n = len(points)
        minHeap = []
        x, y = points[0]
        heapq.heappush(minHeap,[0,x,y])
        for x1,y1 in points[1:]:
            heapq.heappush(minHeap, [(abs(x-x1)+ abs(y-y1)),x1,y1])
        while len(minT) < n:
            c,x,y = heapq.heappop(minHeap)
            if (x,y) in minT:
                continue
            minT[(x,y)]  = c
            for x1,y1 in points:
                if (x1,y1) not in minT:
                    heapq.heappush(minHeap,[(abs(x-x1)+ abs(y-y1)),x1,y1])
        return sum(minT.values())




        