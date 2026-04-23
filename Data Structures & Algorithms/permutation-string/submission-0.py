class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}
        k = len(s1)
        temp = {}
        for i in s1:
            d[i] = 1+ d.get(i,0)
            temp[i] = 0
        l = 0
        r = 0
        print(d)
        while r < len(s2):
            if s2[r] in temp:
                temp[s2[r]] += 1   
            # print(l , r, temp)
            if r - l + 1 >= k:
                if temp == d:
                    return True 
                if s2[l] in temp:
                    temp[s2[l]] -= 1
                l += 1
            r += 1
        return False

        