class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        res = 0
        def dfs(i,path):
            if path == t:
                return 1
            elif i == n-1:
                return 0
            elif len(path) >= m:
                return 0
            temp = 0
            for j in range(i+1, n):
                temp += dfs(j, path+s[j])
            return temp
        return dfs(-1,"")


        