class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        i = 0 
        for idx, edge in enumerate(edges):
            adj[edge[0]].append([-succProb[idx], edge[1]])
            adj[edge[1]].append([-succProb[idx], edge[0]])
        # print(adj)
        minHeap = []
        minT = {}
        heapq.heappush(minHeap, [-1,start_node])

        while minHeap:
            pos, node = heapq.heappop(minHeap)
            pos = -pos
            if node in minT:
                continue
            minT[node] = pos
            if node == end_node:
                return minT[node]
            for prob , v in adj[node]:
                prob = - prob
                heapq.heappush(minHeap, [-prob*pos, v])
        return 0
        