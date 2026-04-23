class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        res = 0
        l = 0
        f = 0
        for r in range(len(s)):
            d[s[r]] = 1+ d.get(s[r], 0)
            f = max(f, d[s[r]])
            while (r-l+1) - f > k:
                d[s[l]] -= 1
                l+=1
            res = max(r-l+1,res)
        return res
        