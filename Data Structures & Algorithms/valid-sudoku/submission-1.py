class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            row = set()
            column = set()
            for j in range(9):
                if board[i][j] in row or board[j][i] in column:
                    return False
                else:
                    if board[i][j] != ".":
                        row.add(board[i][j])
                    if board[j][i] != ".":
                        column.add(board[j][i])
        dia = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                x = i // 3
                y = j // 3
                if board[i][j] in dia[x][y]:
                    return False
                elif board[i][j] != ".":
                    dia[x][y].add(board[i][j])
        
        return True

                