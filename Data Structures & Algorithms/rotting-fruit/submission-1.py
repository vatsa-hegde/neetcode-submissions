class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        visit = [[False for _ in range(m)] for _ in range(n)]

        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                    visit[i][j] = True
                elif grid[i][j] == 0:
                    visit[i][j] = True
        while q:
            # print(q,visit)
            r,c,time = q.popleft()
            if not q:
                res = time
            for row,col in [(r+1,c),(r-1,c),(r,c-1),(r,c+1)]:
                if row >= n or row < 0 or col >= m or col < 0:
                    continue
                if visit[row][col]:
                    continue
                if grid[row][col] == 1:
                    q.append((row,col,time+1))
                    visit[row][col] = True
                
        
        for i in range(n):
            for j in range(m):
                if not visit[i][j] and grid[i][j] == 1:
                    return -1
        return res