import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.k_largest = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.k_largest) < self.k:
            heapq.heappush(self.k_largest, val)
        else:
            if val > self.k_largest[0]:
                heapq.heappop(self.k_largest)
                heapq.heappush(self.k_largest, val)
        
        return self.k_largest[0]
