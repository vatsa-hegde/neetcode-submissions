class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        marea = 0
        while left < right:
            height = min(heights[left], heights[right])
            area = height * (right-left)
            if area > marea:
                marea = area
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return marea

        