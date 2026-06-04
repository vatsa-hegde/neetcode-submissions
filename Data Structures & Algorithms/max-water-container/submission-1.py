class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        marea = 0

        while r < len(heights) and l < r:
            length = r-l
            breadth = min(heights[l],heights[r])
            if length*breadth > marea:
                marea = length*breadth
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return marea