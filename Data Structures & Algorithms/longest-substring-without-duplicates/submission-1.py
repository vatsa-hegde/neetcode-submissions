class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        d = {}
        l = 0
        r = 0

        while r < len(s):
            if s[r] in d:
                l = max(d[s[r]]+1, l)
            d[s[r]] = r
            if r-l+1 > res:
                res = r-l+1
            r+=1


        
        return res

