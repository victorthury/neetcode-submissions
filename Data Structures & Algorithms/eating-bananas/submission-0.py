from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(k):
            totalTimeElapsed = 0
            for pile in piles:
                totalTimeElapsed += ceil(pile / k)
            return totalTimeElapsed <= h


        left = 1
        right = max(piles)

        while left < right:
            middle = (left + right) // 2
            if canEat(middle):
                right = middle
            else:
                left = middle + 1
        
        return right

