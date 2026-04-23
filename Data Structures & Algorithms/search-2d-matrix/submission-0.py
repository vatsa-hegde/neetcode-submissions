class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, l = 0, 0
        b,r = len(matrix)-1, len(matrix[0])-1

        while t <= b:
            mrow = (t+b)// 2
            if matrix[mrow][l] <= target and matrix[mrow][r] >= target:
                while l <= r:
                    mid =  (l+r) // 2
                    if matrix[mrow][mid] == target:
                        return True
                    elif matrix[mrow][mid] < target:
                        l = mid+1
                    else:
                        r = mid-1
            elif matrix[mrow][l] > target:
                b = mrow - 1
            else:
                t = mrow + 1
        return False
        