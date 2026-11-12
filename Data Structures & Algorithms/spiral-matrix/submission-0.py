class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        I go to right till the end of the list
        Once I am at the end I need to change the direction and go down
        Once I reach the bottom I need to change direction
        """

        m, n = len(matrix), len(matrix[0])
        res = []

        # append all the elements in the given direction
        def dfs(row, col, r, c, dr, dc):
            if row == 0 or col == 0:
                return

            for i in range(col):
                r += dr
                c += dc
                res.append(matrix[r][c])

            # sub-problem
            dfs(col, row - 1, r, c, dc, -dr)

        # start by going to the right
        dfs(m, n, 0, -1, 0, 1)
        return res
         
        