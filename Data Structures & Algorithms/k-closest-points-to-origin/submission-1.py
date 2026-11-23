class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getDist(x,y):
            return math.sqrt((x**2)+ (y**2))
        
        heap = []
        result = []

        for x,y in points:
            dist = getDist(x,y)
            heapq.heappush(heap,(dist,x,y))
        
        for dist,x,y in heapq.nsmallest(k,heap):
            result.append([x,y])
        return result
        