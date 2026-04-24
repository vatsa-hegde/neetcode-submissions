class Solution:
    def trap(self, height: List[int]) -> int:
        pm = [0]*(len(height)+1)
        sm = [0]*(len(height)+1)
        res = 0
        for i in range(1,len(height)):
            pm[i] = (max(pm[i-1],height[i-1]))
        for i in range(len(height)-2,0,-1):
            sm[i] = max(sm[i+1], height[i+1])
        for i in range(len(height)):
            val = min(pm[i], sm[i]) - height[i]
            if val >0:
                res+= val
        return res

        