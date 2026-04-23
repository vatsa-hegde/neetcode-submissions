class MedianFinder:

    def __init__(self):
        self.n = 0
        self.nums = []
        heapq.heapify(self.nums)
        

    def addNum(self, num: int) -> None:
        self.n+=1
        heapq.heappush(self.nums,num)
        

    def findMedian(self) -> float:
        res = heapq.nsmallest(self.n//2+1,self.nums)
        print(self.nums,res)
        if self.n % 2 == 0:
            return (res[-1]+res[-2])/2
        else:
            return res[-1]
        
        