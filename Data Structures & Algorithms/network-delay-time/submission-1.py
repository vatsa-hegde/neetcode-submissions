class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for ui, vi, ti in times:
            if ui not in adj:
                adj[ui] = []
            adj[ui].append([ti,vi])
        
        minHeap = []
        heapq.heappush(minHeap,[0,k])
        minT = {}
        while minHeap:
            t , v = heapq.heappop(minHeap)
            if v in minT:
                continue
            minT[v] = t
            if v in adj:
                for ti, vi in adj[v]:
                    heapq.heappush(minHeap, [ti+t, vi])
        if len(minT.keys()) != n:
            return -1
        return max(minT.values())
            
        


        