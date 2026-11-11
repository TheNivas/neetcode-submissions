class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix) # 3
        cols = len(matrix[0]) # 4

        l, r = 0, rows * cols -1 # 0, 11

        while l <= r:
            m = (l + r) // 2
            # m = l + (r-l) // 2
            row, col = m // cols, m % cols

            if matrix[row][col] < target:
                l = m+1
            elif target < matrix[row][col]:
                r = m-1
            else:
                return True
        return False

        