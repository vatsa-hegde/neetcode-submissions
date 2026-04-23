class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        for num in nums:
            heapq.heappush(heap,num)
        return heapq.nsmallest(len(nums),heap)
        