class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        l = 0
        r = m * n - 1

        while l <= r:
            middle = (l + r) // 2
            
            row = middle // n
            col = middle % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = middle + 1
            else:
                r = middle - 1
        return False

