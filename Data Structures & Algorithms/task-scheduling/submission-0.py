class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t = 0
        d = Counter(tasks)
        mHeap = [-cnt for cnt in d.values()]
        q = deque()

        while mHeap or q:
            # print(q,mHeap)
            if q and q[0][1] < t:
                heapq.heappush(mHeap,q.popleft()[0])
            if mHeap:
                freq = heapq.heappop(mHeap)+1
                if freq != 0:
                    q.append((freq, t+n))
            t+=1
        return t





        