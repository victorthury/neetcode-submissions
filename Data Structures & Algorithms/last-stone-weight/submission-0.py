import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:    
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)

        while len(stones) > 1:
            largest_stone = heapq.heappop(stones)
            seccond_largest_stone = heapq.heappop(stones)

            if largest_stone != seccond_largest_stone:
                new_stone = largest_stone - seccond_largest_stone
                heapq.heappush(stones, new_stone)
            
        return -stones[0] if stones else 0


