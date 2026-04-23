class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        n, m = len(grid), len(grid[0])
        q = deque()

        # Add all gates (0) to queue
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    q.append((r, c))

        # BFS
        while q:
            r, c = q.popleft()
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
            
            
        