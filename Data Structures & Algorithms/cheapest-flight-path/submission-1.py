class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for f,t,p in flights:
            adj[f].append([p,t])
        minHeap = []
        heapq.heappush(minHeap, [0,src,0])
        res = 0
        visit = set()
        while minHeap:
            p, d, i = heapq.heappop(minHeap)
            
            if d in visit:
                continue
            if i <= k+1 and d == dst:
                res = p
                break
            for ele in adj[d]:
                heapq.heappush(minHeap,[p+ele[0], ele[1], i+1])
            # print(p,d,i, minHeap)
        if res == 0:
            return -1
        return res

                
            
            


