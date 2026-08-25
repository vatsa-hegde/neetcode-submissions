class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height)-1
        lm, rm = height[left], height[right]
        while left < right:
            if lm < rm:
                left+= 1
                lm = max(height[left],lm)
                res += lm - height[left]
            else:
                right -= 1
                rm = max(height[right], rm)
                res += rm - height[right]
        return res

                    




        