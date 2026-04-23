class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for row in board:
            temp = []
            for val in row:
                if val in temp:
                    # print(temp, val , "row", row, col)
                    return False
                else:
                    if val != '.':
                        temp.append(val)
        for col in range(n):
            temp = []
            for row in range(n):
                if board[row][col] in temp:
                    # print(temp, val, "col", row, col)
                    return False
                else:
                    if board[row][col] != '.':
                        temp.append(board[row][col])
        for row in range(0,n,3):
            for col in range(0,n,3):
                box = []
                for i in range(row,row+3,1):
                    for j in range(col,col+3, 1):
                        if board[i][j] in box:
                            # print(box, board[i][j], "3*3")
                            return False
                        else:
                            if board[i][j] != '.':
                                box.append(board[i][j])
        return True
                        
