class Solution:
    def trap(self, height: List[int]) -> int:
        lm, rm = 0,0
        left, right = 0, len(height)-1
        res = 0

        while left <= right:
            if lm < rm:
                res += max(lm - height[left],0)
                lm = max(lm,height[left])
                left+=1
            else:
                res += max(rm-height[right],0)
                rm = max(rm,height[right])
                right-=1
        
        return res

        