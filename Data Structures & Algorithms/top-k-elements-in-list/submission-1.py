class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        h = []
        for num,v in c.items():
            heapq.heappush(h,(v,num))
            if len(h) > k:
                heapq.heappop(h)
        return [num for v,num in h ]