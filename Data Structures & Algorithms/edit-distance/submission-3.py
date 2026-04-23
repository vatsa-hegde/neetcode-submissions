class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = {}
        
        def dfs(i,j): 
            if j >= m:
                return n - i
            if i >= n:
                return m-j
            
            if (i,j) in dp:
                return dp[(i,j)]
                
            if word1[i] == word2[j]:
                dp[(i,j)] = dfs(i+1,j+1)
                return dp[(i,j)]
                
            dp[(i,j)] = min(
                dfs(i,j+1),
                dfs(i+1,j),
                dfs(i+1,j+1)
                ) + 1
            return dp[(i,j)]
        return dfs(0,0)
            
        