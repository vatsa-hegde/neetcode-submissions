class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        [
        1, 1, 0
        0, 1, 1
        0, 1, 2
        ]

        explore_banana(i, j) -> max_total_minutes
        
        """

        def isValid(row,col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return False
            return True
        fresh = 0
        time = 0
        q = collections.deque()
        direction = [(1,0), (-1,0), (0,1), (0,-1)]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    q.append((row,col))
        
        while fresh > 0 and q:
            length  = len(q)
            time+=1
            for i in range(length):
                r ,c = q.popleft()

                for dr,dc in direction:
                    row = r + dr
                    col = c + dc
                    if isValid(row,col) and grid[row][col] == 1:
                        fresh -=1
                        grid[row][col] = 2
                        q.append((row,col))
            
        return time if fresh == 0 else -1
                    


        

       




        



        