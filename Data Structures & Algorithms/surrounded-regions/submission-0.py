class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n,m = len(board), len(board[0])

        def dfs(r,c):
            if r < 0 or r >= n or c < 0 or c >= m or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(n):
            for c in range(m):
                if board[r][c] == 'O' and (r in [0,n-1] or c in [0,m-1]):
                    dfs(r,c)
        
        for r in range(n):
            for c in range(m):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'

    

        