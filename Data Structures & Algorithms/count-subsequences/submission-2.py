class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        memo = {}
        def dfs(i,path):
            if (i,path) in memo:
                return memo[(i,path)]
            if path == t:
                return 1
            elif i == n-1:
                return 0
            elif len(path) >= m:
                return 0
            
            memo[(i,path)] = 0
            for j in range(i+1, n):
                memo[(i,path)] += dfs(j, path+s[j])
            return memo[(i,path)]
        return dfs(-1,"")


        