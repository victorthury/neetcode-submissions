class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        res = 0

        while left <= right:
            middle = (right + left) // 2
            middle_squared = middle * middle
            
            if middle_squared == x:
                return middle
            elif middle_squared > x:
                right = middle - 1
            else:
                left = middle + 1
                res = middle
        return res