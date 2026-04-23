class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        marea = 0
        stack= []
        for i in range(len(heights)):
            if not stack:
                stack.append((i,heights[i]))
                continue
            if stack[-1][1] > heights[i]:
                while stack and stack[-1][1] > heights[i]:
                    pos, h = stack.pop()
                    a = h * (i - pos )
                    if a > marea:
                        marea = a
                stack.append((pos,heights[i]))
            else:
                stack.append((i,heights[i]))
        # print(stack)
        while stack:
            pos, val = stack.pop()
            # print(stack, pos, val,  val*(len(heights)-pos))
            if val*(len(heights)-pos) > marea:
                marea = val*(len(heights)-pos)
        return marea

        