class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        marea = 0
        n = len(grid)
        m = len(grid[0])
        visit = [[False for _ in range(m)] for _ in range(n)]

        def traversal(r,c):
            if r < 0 or r >= n or c < 0 or c >= m or visit[r][c] or grid[r][c] == 0:
                return 0
            visit[r][c] = True
            a = 1
            for row,col in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                a+= traversal(row,col)
            # print(a)
            return a
        
        for r in range(n):
            for c in range(m):
                if not visit[r][c]:
                    a = traversal(r,c)
                    # print(a)
                    if a > marea:
                        marea = a
        return marea
            
        