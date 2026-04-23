class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap)
        self.k = k
        

    def add(self, val: int) -> int:
        # print(self.heap,val)
        heapq.heappush(self.heap,val)
        return heapq.nlargest(self.k,self.heap)[-1]
        
