class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        d = {}
        temp = {}
        res = ""
        length = float("inf") 
        have = 0
        need = 0
        for i in t:
            d[i] = 1+ d.get(i,0)
            temp[i] = 0
            need += 1
        l = 0
        r = 0
        print(d)
        while r < len(s):
            # print(need, have, have < need,  s[r])
            if s[r] in d:
                if have < need and temp[s[r]] < d[s[r]]:
                    have += 1
                temp[s[r]] += 1
            while need <= have:
                print(need , have)
                if r-l+1  < length:
                    length = r-l+1
                    res = s[l:r+1]
                if s[l] in temp:
                    temp[s[l]] -= 1
                if s[l] in temp and temp[s[l]] < d[s[l]]:
                    have -= 1
                l+=1
            r+=1
        return res
        