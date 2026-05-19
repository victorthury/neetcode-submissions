class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        n = len(nums)

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        frequency = [[] for i in range(n+1)]

        for num, freq in counter.items():
            frequency[freq].append(num)

        topK = []

        for i in range(n, 0, -1):
            if len(frequency[i]) > 0:
                for num in frequency[i]:
                    topK.append(num)
                    if len(topK) == k:
                        return topK
                    
