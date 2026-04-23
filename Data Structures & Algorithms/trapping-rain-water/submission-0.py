class Solution:
    def trap(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        area = 0
        mleft = height[left]
        mright = height[right]

        while right >= left:
            a = 0
            if mleft > mright:
                a = mright - height[right]
                if height[right] > mright:
                    mright = height[right]
                right -= 1
            else:
                a = mleft - height[left]
                if height[left] >mleft:
                    mleft = height[left]
                left += 1
            if a > 0:
                area += a

        return area




        