class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        n = len(grid)
        m = len(grid[0])
        visit = [[False for _ in range(m)] for _ in range(n)]

        def traverse(row,col):
            if row < 0 or row >= n or col < 0 or col >= m or visit[row][col]:
                return
            if grid[row][col] == "1":
                visit[row][col] = True
                for r,c in [(row+1,col), (row-1,col), (row,col-1), (row,col+1)]:
                    traverse(r,c)
            return
        
        for r in range(n):
            for c in range(m):
                if not visit[r][c] and grid[r][c] == "1":
                    res+=1
                    # print(r,c)
                    # print(visit)
                    traverse(r,c)
        return res
                

            
            