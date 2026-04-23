class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = []
        minT = {}
        heapq.heappush(minHeap, [grid[0][0],0,0])
        n = len(grid)
        while minHeap:
            t,x,y = heapq.heappop(minHeap)
            if (x,y) in minT:
                continue
            minT[(x,y)] = t
            if x== n-1 and y == n-1:
                return t
            for i,j in [(1,0),(-1,0), (0,1), (0,-1)]:
                if x+i >= 0 and y+j >=0 and x+i < n and y+j < n:
                    heapq.heappush(minHeap,[max(grid[x+i][y+j],t) , x+i, y+j])
            
