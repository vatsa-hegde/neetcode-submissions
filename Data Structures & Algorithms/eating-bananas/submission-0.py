class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        res = r

        while r>= l:
            mid = (l+r)//2
            hour = 0
            for pile in piles:
                hour += math.ceil(pile/mid)
            if hour <= h:
                if res > mid:
                    res = mid
                r = mid-1
            else:
                l = mid + 1
        return res

        
        