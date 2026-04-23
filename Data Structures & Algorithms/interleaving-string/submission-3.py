class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # x,y,z = len(s3),len(s1), len(s2)
        # memo = {}
        # def dfs(i,j,k,n,m,prev):
        #     if (k,prev) in memo:
        #         return memo[(k,prev)]
        #     res = False
        #     if abs(n-m) > 1:
        #         memo[(k,prev)] = False
        #         return False
        #     if k == x and i == y and z == j:
        #         memo[(k,prev)] = True
        #         return True
        #     elif k == x:
        #         memo[(k,prev)] = False
        #         return False
        #     if i< y and s3[k] == s1[i]:
        #         if prev == 1:
        #             res |= dfs(i+1,j,k+1,n,m,prev)
        #         else:
        #             res |= dfs(i+1,j,k+1,n+1,m,1)
        #     if j < z and s3[k] == s2[j]:
        #         if prev == 2:
        #             res |= dfs(i,j+1,k+1,n,m,prev)
        #         else:
        #             res |= dfs(i,j+1,k+1,n,m+1,2)
        #     memo[(k,prev)] =  res
        #     return res
        # return dfs(0,0,0,0,0,-1)

        x,y,z = len(s3),len(s1), len(s2)
        memo = {}
        def dfs(i,j,k):
            if (i,j) in memo:
                return memo[(i,j)]
            res = False
            if k == x and i == y and z == j:
                memo[(i,j)] = True
                return True
            elif k == x:
                memo[(i,j)] = False
                return False
            if i< y and s3[k] == s1[i]:
                res |= dfs(i+1,j,k+1)
            if j < z and s3[k] == s2[j]:
                res |= dfs(i,j+1,k+1)

            memo[(i,j)] =  res
            return res
        return dfs(0,0,0)

        # x,y,z = len()




        