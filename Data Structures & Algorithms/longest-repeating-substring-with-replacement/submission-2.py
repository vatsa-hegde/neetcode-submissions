class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # d={}
        # res = 0
        # l = 0
        # f = 0
        # for r in range(len(s)):
        #     d[s[r]] = 1+ d.get(s[r], 0)
        #     f = max(f, d[s[r]])
        #     while (r-l+1) - f > k:
        #         l+=1
        #         d[s[l]] -= 1
        #     res = max(r-l+1,res)

        # return res
        count = {}
        res = 0
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

